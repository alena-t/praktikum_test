import requests
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver


class TestGithubApi:

    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_bun(mock_bun)
        assert burger.bun.name == 'булка'



WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(
    (By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')))




COMPLETED_ORDERS_ALL_TIME = By.XPATH, '//*[contains(@class, "text_type_main-medium") and text()="Выполнено за все время:"]/following-sibling::p'
COMPLETED_ORDERS_TODAY = By.XPATH, '//*[contains(@class, "text_type_main-medium") and text()="Выполнено за сегодня:"]/following-sibling::p'
