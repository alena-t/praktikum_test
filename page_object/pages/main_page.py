import allure

from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_to_element(locator_q_formatted)

    @allure.step("Получение текста ответа")
    def get_text_answer(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверка результата')
    def get_answer_text(self, num):
        self.click_to_question(num)
        return self.get_text_answer(num)


    def set_order(self, station_locator, name_locator, name,
                  last_name, address, time, button_locator):
        self.click_to_element(station_locator)
        self.add_text_to_element(name_locator, name)
        self.add_text_to_element(last_name, last_name)
        self.add_text_to_element(address, address)
        self.click_to_element(time)
        self.click_to_element(button_locator)

    def check_order(self, locator):
        return self.get_text_from_element(locator)

    def set_and_check_order(self):
        self.click_to_question(1)
        return self.check_order(1)
