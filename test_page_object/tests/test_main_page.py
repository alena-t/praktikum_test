import pytest

from test_page_object.data import Answers, ANSWER_Q_3, MAIN_URL, ANSWER_Q1
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        "q_num,expected_result",
        [
            (0, Answers.ANSWER_Q_1),
            (1, ANSWER_Q_3[0]),
            (2, ANSWER_Q1),
            (3, ANSWERS_DICT.get(3))
        ]
    )
    def test_questions(self, main_page, q_num, expected_result):
        switch_page = SwitchPage(driver)
        result = main_page.click_to_question_and_get_answer_text(
            q_num
        )
        assert result == expected_result
