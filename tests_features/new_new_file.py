from unittest.mock import Mock, patch

import pytest
from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS_LOCATOR = By.XPATH, '//*[@class="some-class-{}"]'
    ANSWERS_LOCATOR = By.XPATH, '//*[@class="some-class-{}"]'


def click_on_question(num):
    method, locator = MainPageLocators.QUESTIONS_LOCATOR
    locator = locator.format(num)
    element = driver.find_element((method, locator)).click()


@pytest.mark.parametrize(
    'num,e_result',
    [0, 1, 2, 3, 4, 5, 6, 7]
)
def test_questions(driver, num, e_result):
    main_page = MainPage(driver)
    main_page.click_on_question(num)
    assert driver.find_element(*TestLocators.SEARCH_BUTTON).text() == e_result


@patch('prakticum_test.SomeClass')
@pytest.mark.parametrize(
    'e_result',
    [0, 1, 2]
)
def test_some_with_mock(mock_some_class, e_result):
    mock_some_class.get_some.return_value = 2
    mock_some_class.post_some.return_value = e_result
    result = requests.get("")
    assert result == e_result and some_e == some, (
        f'Result is {env.SOME}, but e_result is {e_result}'
        f'and some={some}, but some_e={some_e}'
    )
