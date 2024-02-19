from test_page_object.pages.base_page import BasePage


class MainPage(BasePage):

    def get_url(self, URL):
        self.driver.get(URL)

    def click_to_question_and_get_answer_text(self, locator_q, locator_a, num):
        method, locator = locator_q
        locator = locator.format(num)
        self.click_on_element((method, locator))
        return self.get_text_from_element(locator_a)

    def check_answer(self, result, expected):
        return result == expected
