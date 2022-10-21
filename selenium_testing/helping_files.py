from __future__ import annotations

import json
import logging
import os

from typing import Optional
from datetime import datetime as dt, timedelta

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

ELEMENT_WAIT_TIMEOUT = 5

log = logging.getLogger(__name__)


def save_locator_to_coverage(locator: tuple) -> str:
    if os.environ.get('STORE_LOCATORS', False):
        if locator[0] == By.CLASS_NAME:
            result = f"//div[contains(concat(' ',normalize-space(@class),' '),' locator[1] ')]"
        elif locator[0] == By.NAME:
            result = f'//*[@name="{locator[1]}"]'
        elif locator[1] == By.ID:
            result = f'//*[@id="{locator[1]}"]'
        elif locator[0] == By.XPATH:
            result = locator[1]
        else:
            result = None

        data = {'data': []}

        locators_file_name = 'locators.json'
        try:
            with open(locators_file_name, 'r', encoding='utf-8') as file:
                data = json.loads(file.read())
        except FileNotFoundError:
            pass

        for locator in data['data']:
            if result == locator['fullPath']:
                locator['count'] = locator['count'] + 1
                break
        else:
            new = {'fullPath': result, 'count': 1}
            data['data'].append(new)

        with open(locators_file_name, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data))

        return result


class BasicElement:
    def __init__(self, driver: WebDriver, locator: tuple) -> None:
        self.driver = driver
        self.locator = locator

        self.wait = WebDriverWait(self.driver, ELEMENT_WAIT_TIMEOUT)

        self.__element = None
        self.__actions_chains = None

    def __str__(self):
        return f'Element:<{self.locator}>'

    @property
    def element(self) -> WebElement:
        if not self.__element:
            self.__element = self.driver.find_element(*self.locator)

        return self.__element

    @property
    def text(self):
        save_locator_to_coverage(self.locator)
        return self.element.text

    @property
    def action_chains(self) -> ActionChains:
        if not self.__actions_chains:
            self.__actions_chains = ActionChains(self.driver)
        return self.__actions_chains

    @property
    def size(self):
        return self.element.size

    @property
    def link(self):
        save_locator_to_coverage(self.locator)
        try:
            link = self.get_attribute('href')
        except NoSuchElementException:
            link = None
        except StaleElementReferenceException:
            link = None

        return link

    def click(self):
        log.info(f'click action on element <{self.locator}>')
        save_locator_to_coverage(self.locator)
        self.element.click()

    def is_displayed(self) -> bool:
        try:
            is_displayed = self.is_exist() and self.element.is_displayed()
        except NoSuchElementException:
            is_displayed = False
        except StaleElementReferenceException:
            is_displayed = False

        log.info(f'is displayed result is {is_displayed} for {self}')
        return is_displayed

    def wait_appearance(self) -> bool:
        # use this method when you need to implicitly wait element
        try:
            def custom_wait_condition(driver):
                condition = self.element.is_displayed()
                return condition

            try:
                self.wait.until(custom_wait_condition)
                is_displayed = self.element.is_displayed()
            except TimeoutException:
                is_displayed = False

        except NoSuchElementException:
            is_displayed = False
        except StaleElementReferenceException:
            is_displayed = False

        log.info(f'wait appearance result is {is_displayed} for {self}')
        return is_displayed

    def wait_intractable(self) -> bool:
        try:
            self.wait.until(element_to_be_clickable(self.locator))
            is_displayed = self.element.is_enabled()
        except TimeoutException:
            is_displayed = False
        except NoSuchElementException:
            is_displayed = False
        except StaleElementReferenceException:
            is_displayed = False

        log.info(f'wait intractable result is {is_displayed} for {self}')
        return is_displayed

    def is_exist(self):
        try:
            is_exist = self.element is not None
        except NoSuchElementException:
            is_exist = False

        return is_exist

    def focus(self, mode="center"):
        # mode can be: start, center, end, or nearest
        self.driver.execute_script(f'arguments[0].scrollIntoView({{block: "{mode}"}});', self.element)

    def find_element(self, *args, **kwargs):
        return self.element.find_element(*args, **kwargs)

    def find_elements(self, *args, **kwargs):
        return self.element.find_elements(*args, **kwargs)

    def type_text(self, text):
        save_locator_to_coverage(self.locator)
        self.element.send_keys(text)

    def find_child(self, locator: tuple) -> BasicElement:
        method, child_locator = locator

        if method == By.XPATH:
            if child_locator.startswith('.'):
                child_locator = child_locator.replace('.', '', 1)
            child_full_locator = method, f'({self.locator[1]}){child_locator}'
            element = BasicElement(self.driver, child_full_locator)
        else:
            raise Exception('Method find_child uses only XPATH locators!')

        return element

    def is_enabled(self):
        return self.element.is_enabled()

    def get_attribute(self, name) -> Optional[str]:
        return self.element.get_attribute(name)


def list_of_elements_from_locator(driver_object, basic_locator, elements_class) -> list:
    result_elements = []

    elements = driver_object.find_elements(*basic_locator)
    for i, elem in enumerate(elements):
        basic_locator_path = basic_locator[1]

        # very bad implementation
        if not basic_locator_path.startswith('('):
            basic_locator_path = '(' + basic_locator_path

        if not basic_locator_path.endswith(')'):
            basic_locator_path = basic_locator_path + ')'
        # very bad implementation ends here

        hotel_locator = (basic_locator[0], f'{basic_locator_path}[{i + 1}]')
        result_elements.append(elements_class(driver_object, hotel_locator))

    return result_elements


def get_day_in_days(number):
    now = dt.today()

    after_days = now + timedelta(days=number)

    return after_days


def today_day_number():
    return dt.today().day
