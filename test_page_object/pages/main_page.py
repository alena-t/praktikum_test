import allure

from test_page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_on_question(self, num):
        formatted_q_locator = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_on_element(formatted_q_locator)

    @allure.step('Получение текста ответа')
    def get_text_from_answer(self, num):
        formatted_a_locator = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(formatted_a_locator)

    def click_to_question_and_get_answer_text(self, num):
        self.click_on_question(num)
        return self.get_text_from_answer(num)

    @allure.step('Проверка соответствия результата')
    @staticmethod
    def check_answer(result, expected):
        return result == expected


