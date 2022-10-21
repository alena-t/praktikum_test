import datetime
import logging
import re
from time import sleep
from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium_testing.elements_to_find import TestLocators
from selenium_testing.helping_files import BasicElement, list_of_elements_from_locator, get_day_in_days, \
    today_day_number

log = logging.getLogger(__name__)


class SearchForm(BasicElement):
    def __init__(self, driver, locator):
        super(SearchForm, self).__init__(driver, locator)

    @property
    def calendar(self):
        return Calendar(self.driver)

    @property
    def search_input(self):
        return SearchInput(self.driver, TestLocators.SEARCH_INPUT_FIELD)

    @property
    def search_button(self):
        return BasicElement(self.driver, TestLocators.SEARCH_BUTTON)

    @property
    def check_in_button(self):
        return SearchFormButton(self.driver, TestLocators.CHECK_IN_BUTTON)

    @property
    def check_out_button(self):
        return SearchFormButton(self.driver, TestLocators.CHECK_OUT_BUTTON)

    @property
    def guests(self):
        return GuestsPanel(self.driver, TestLocators.GUESTS_SELECTOR)

    @property
    def suggest(self):
        return SearchSuggest(self.driver, TestLocators.SUGGEST)

    def get_number_of_guests(self):
        text = self.guests.find_element(*TestLocators.GUESTS_NUMBER).text
        pattern = r'\d'

        print(f'<{text}>')
        match = re.match(pattern, text)

        if match:
            number = int(match.group())
        else:
            number = None

        return number

    def close_popup(self):
        elem = BasicElement(self.driver, TestLocators.CLOSE_POPUP)
        elem.click()

    def click_outside(self):
        ac = self.action_chains

        ac.reset_actions()

        ac.move_to_element_with_offset(self.element, -50, 0)
        ac.click()

        ac.perform()

    def is_dateless(self):
        elem = BasicElement(self.driver, TestLocators.DATELESS)
        return elem.is_exist()

    def is_suggest_empty(self):
        element = BasicElement(self.driver, TestLocators.EMPTY_SUGGEST)
        element.wait_appearance()
        return element.is_displayed()


class Day(BasicElement):
    def is_enabled(self):
        try:
            disabled = self.element.find_element(*TestLocators.DAY_DISABLED) is not None
        except NoSuchElementException:
            disabled = False
        return disabled


class MonthDaysGrid(BasicElement):
    @property
    def name(self):
        title_elem = self.element.find_element(*TestLocators.MONTH_TITLE)
        return title_elem.text

    def get_day_by_number(self, number: int) -> Day:
        method, locator_template = TestLocators.DAY_TEMPLATE
        day_locator = method, self.locator[1] + locator_template.format(number)
        day_element = Day(self.driver, day_locator)

        return day_element


class Calendar(BasicElement):
    def __init__(self, driver):
        super(Calendar, self).__init__(
            driver,
            TestLocators.CALENDAR
        )

    @property
    def month_list(self) -> List[BasicElement]:
        return list_of_elements_from_locator(self.driver, TestLocators.CALENDAR_MONTH_LIST, BasicElement)

    @property
    def month_days_grid(self) -> List[MonthDaysGrid]:
        return list_of_elements_from_locator(self.driver, TestLocators.CALENDAR_GRID_MONTH, MonthDaysGrid)

    @property
    def months_count(self):
        months = len(self.month_list)
        return months

    def click_on_last_month(self):
        self.month_list[-1].click()

    def click_on_first_month(self):
        self.month_list[0].click()

    def are_last_days_disabled(self):
        days = self.driver.find_elements(*TestLocators.CALENDAR_LAST_DAYS)

        for day in days:
            try:
                day.find_element(*TestLocators.DAY_DISABLED)
                disabled = True
                break
            except NoSuchElementException:
                continue
        else:
            disabled = False

        return disabled

    def click_today(self):
        first_month = self.month_days_grid[0]
        today_day = today_day_number()

        today_day_element = first_month.get_day_by_number(today_day)
        today_day_element.click()

        return today_day

    def click_on_day(self, day: datetime):
        today_month = get_day_in_days(0).month
        today_year = get_day_in_days(0).year

        index = 12 * (day.year - today_year) + day.month - today_month

        month = self.month_list[index]
        month.wait_intractable()
        month.click()

        month_grid = self.month_days_grid[index]
        # Wait animation complete
        month_grid.wait_appearance()

        day_on_grid = month_grid.get_day_by_number(day.day)
        day_on_grid.wait_intractable()
        day_on_grid.click()


class SearchFormButton(BasicElement):
    def is_focused(self):
        try:
            elem = self.element.find_element(*TestLocators.GUESTS_LABEL_FOCUSED)
        except NoSuchElementException:
            elem = None

        log.info(f'SearchFormButton is <{elem}>')
        return elem is not None


class GuestsRoom(BasicElement):
    @property
    def adults_plus_button(self):
        return self.find_child(TestLocators.ROOM_ADULTS_PLUS)

    @property
    def children_plus_button(self):
        return self.find_child(TestLocators.ROOM_KIDS_SELECT)

    @property
    def children_list(self) -> list:
        return list_of_elements_from_locator(self.driver, TestLocators.ROOM_KIDS_UNIT, BasicElement)

    def increase_adults_number(self, by_number):
        default_adults_number = 2
        ac = self.action_chains

        ac.reset_actions()

        for i in range(by_number):
            ac.click(self.adults_plus_button.element)

        ac.perform()

        return default_adults_number + by_number

    def set_child_age(self, age):
        self.children_plus_button.click()
        child_age_selector = Select(self.children_plus_button.element)
        child_age_selector.select_by_value(str(age))

    def remove_child_button(self, child_num):
        buttons_list = list_of_elements_from_locator(self.driver, TestLocators.ROOM_KIDS_REMOVE_CHILD, BasicElement)
        return buttons_list[child_num - 1]

    @property
    def children_ages(self):
        age_text = list_of_elements_from_locator(self.driver, TestLocators.ROOM_KID_AGE, BasicElement)
        ages = []
        for element in age_text:
            ages.append(element.text.split(' ')[0])
        return ages


class GuestsPanel(SearchFormButton, BasicElement):
    @property
    def rooms(self) -> List[GuestsRoom]:
        return list_of_elements_from_locator(self.driver, TestLocators.ROOM_WRAPPER, GuestsRoom)

    @property
    def more_rooms_button(self):
        return self.find_element(*TestLocators.ADD_MORE_ROOMS_BUTTON)

    @property
    def book_more_rooms_button(self):
        return self.find_element(*TestLocators.BOOK_MORE_ROOMS_BUTTON)

    @property
    def done_button(self):
        return self.find_element(*TestLocators.DONE_BUTTON)

    def add_more_rooms(self, by_number=1):
        ac = self.action_chains

        ac.reset_actions()

        for i in range(by_number):
            ac.click(self.more_rooms_button)

        ac.perform()


class SearchInput(BasicElement):
    def search(self, input_text):
        ac = self.action_chains
        ac.reset_actions()

        ac.click(self.element)
        ac.send_keys(input_text)
        ac.send_keys(Keys.ENTER)

        ac.perform()

    def search_with_wait(self, input_text):
        ac = self.action_chains

        ac.reset_actions()
        ac.click(self.element)
        ac.send_keys(input_text)
        ac.perform()

        # explicitly wait suggest
        # but we can wait suggest result explicitly instead somehow
        sleep(2)

        ac.reset_actions()
        ac.send_keys(Keys.ENTER)
        ac.perform()

    def type(self, input_text):
        ac = self.action_chains
        ac.reset_actions()

        ac.click(self.element)
        ac.send_keys(input_text)

        ac.perform()


class SearchSuggest(BasicElement):
    @property
    def hotels_suggest(self):
        return list_of_elements_from_locator(self.driver, TestLocators.SUGGEST_HOTELS_LIST, BasicElement)

    @property
    def regions_suggest(self):
        return list_of_elements_from_locator(self.driver, TestLocators.SUGGEST_REGIONS_LIST, BasicElement)

    def choose_hotel_by_index(self, index):
        self.hotels_suggest[index].click()

    def wait_for_hotels(self):
        wait = WebDriverWait(self.driver, 5)

        _elements = wait.until(
            visibility_of_all_elements_located(TestLocators.SUGGEST_HOTELS_LIST)
            # exp_condition.visibility_of_all_elements_located(TestLocators.SUGGEST_HOTELS_LIST)
        )
