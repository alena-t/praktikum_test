import pytest

from test_page_object.data import Answers, ANSWER_Q_3, MAIN_URL
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        "q_num,expected_result",
        [
            (0, Answers.ANSWER_Q_1),
            (1, ANSWER_Q_3[0]),
        ]
    )
    def test_questions(self, main_page, q_num, expected_result):
        main_page.get_url(MAIN_URL)
        result = main_page.click_to_question_and_get_answer_text(
            MainPageLocators.QUESTION_LOCATOR,
            MainPageLocators.ANSWER_LOCATOR,
            q_num
        )
        assert main_page.check_answer(result, expected_result)
