import pytest

from page_object.data import ORDER_INFO_DICT, AnswerText
from page_object.helpers import generate_order_info
from page_object.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, AnswerText.ANSWER_TEXT_PRICE),
            (1, AnswerText.ANSWER_TEXT_1)
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result


class TestOrderPage:

    def test_create_order(self, driver):
        order_page = OrderPage(driver)
        switch_page = SwitchPage(driver)
        order_info = generate_order_info()
        order_page.create_order(order_info)
        assert switch_page.check_switch()
