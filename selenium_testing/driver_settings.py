import time

import furl
import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#
# from selenium_testing.elements_to_find import TestLocators
# from selenium_testing.page_files import SearchForm
# from selenium_testing.test_file_pom import BurgerLoginPage


LOCATOR_Q_1 = By.XPATH, '//*[@id="accordion__heading-0"]'
LOCATOR_Q = By.XPATH, '//*[@id="accordion__heading-{}"]'
LOCATOR_Q_3 = (By.XPATH, '//*[@id="accordion__heading-2"]')
LOCATOR_Q_4 = (By.XPATH, '//*[@id="accordion__heading-3"]')
LOCATOR_Q_5 = (By.XPATH, '//*[@id="accordion__heading-4"]')
LOCATOR_Q_6 = (By.XPATH, '//*[@id="accordion__heading-5"]')
LOCATOR_Q_7 = (By.XPATH, '//*[@id="accordion__heading-6"]')
LOCATOR_Q_8 = (By.XPATH, '//*[@id="accordion__heading-7"]')
COOKIES_BUTTON = (By.ID, "rcc-confirm-button")


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def to_go(self):
        return self.driver.get('https://qa-scooter.praktikum-services.ru/')

    def remove_cookies(self):
        cookie_button_element = self.driver.find_element(*COOKIES_BUTTON)
        cookie_button_element.click()

    def check_open_tabs(self, num):
        element = self.driver.find_element(*LOCATOR_Q_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        method, path = LOCATOR_Q
        path = path.format(num)
        seach_element = self.driver.find_element(method, path)
        seach_element.click()


def test_registration(driver):
    login_page = BurgerLoginPage(driver)
    login_page.register('name', 'email', 'password')
    assert login_page.text_login_button() == 'Выйти', (
        'Текст на кнопке не соответствует ожидаемому'
    )


@pytest.mark.parametrize('num', [0,1,2,3,4,5,6,7,8])
def test_for_damir(driver, num):
    samokat = MainPage(driver)
    # samokat.to_go()
    d
    samokat.remove_cookies()
    samokat.check_open_tabs(num)

# def test_do_something():
#     service = Service(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
#     driver = webdriver.Chrome(service=service)
#     driver.get('https://ostrovok.ru/')
#     search_form = SearchForm(driver, TestLocators.SEARCH_FORM_LOCATOR)
#     search_form.search_input.search_with_wait('Moscow')
#     search_form.search_button.click()
#     region_id = 2395
#     url = furl.furl(driver.current_url)
#     search_page = url.args
#     q_param = int(search_page['q'])
#     driver.close()
#     assert q_param == region_id, \
#         f'Serp q param is {q_param}, expected Moscow with id {region_id}'


def do_something():
    options = Options()
    # options.add_argument(windowsize={DEFAULT_WINDOW_SIZE[0]},{DEFAULT_WINDOW_SIZE[1]})
    options.add_argument('--headless')
    # driver creation
    service = Service(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
    driver = webdriver.Chrome(options=options, service=service)
    # driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
    driver.get('https://ostrovok.ru/')
    search_form = SearchForm(driver, TestLocators.SEARCH_FORM_LOCATOR)
    search_form.search_input.search_with_wait('Moscow')
    search_form.search_button.click()
    region_id = 2395
    WebDriverWait.until(expected_conditions.text_to_be_present_in_element())
    driver.implicitly_wait(3)
    url = furl.furl(driver.current_url)
    search_page = url.args
    q_param = int(search_page['q'])

    if q_param != region_id:
        print(f'Serp q param is {q_param}, expected Moscow with id {region_id}')
    else:
        print('Результат соответствует ожидаемому')

    # try:
    #     test_do_something(q_param, region_id)
    # except AssertionError:
    #     driver.close()

    driver.close()


if __name__ == '__main__':
    do_something()
