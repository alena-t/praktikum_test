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
    [0,1,2,3,4,5,6,7]
)
def test_questions(driver, num, e_result):
    main_page = MainPage(driver)
    main_page.click_on_question(num)
    assert driver.find_element(*TestLocators.SEARCH_BUTTON).text() == e_result
