import pytest

from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, 'Стоимость - 400 рублей в сутки.'),
            (1, "Ответ на вопрос 2")
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(
            MainPageLocators.QUESTION_LOCATOR,
            MainPageLocators.ANSWER_LOCATOR,
            num
        ) == result

