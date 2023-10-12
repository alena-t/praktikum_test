import time

import furl
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_testing.elements_to_find import TestLocators
from selenium_testing.page_files import SearchForm

class TestSomething:

    def test_do_something(self):
        options = Options()
        service = Service(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://ostrovok.ru/')
        search_form = SearchForm(driver, TestLocators.SEARCH_FORM_LOCATOR)
        search_form.search_input.search_with_wait('Moscow')
        search_form.search_button.click()
        region_id = 2395
        url = furl.furl(driver.current_url)
        search_page = url.args
        q_param = int(search_page['q'])
        driver.close()
        assert q_param == region_id, \
            f'Serp q param is {q_param}, expected Moscow with id {region_id}'


def do_something():
    options = Options()
    # options.add_argument(windowsize={DEFAULT_WINDOW_SIZE[0]},{DEFAULT_WINDOW_SIZE[1]})
    # options.add_argument(f'lang=en')
    # driver creation
    # driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
    # options.add_argument('--headless')
    service = Service(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver',
    #                           options=options)
    driver.get('https://ostrovok.ru/')
    time.sleep(3)
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(
        TestLocators.SEARCH_BUTTON, "Найти"))
    driver.implicitly_wait(3)
    some_element = driver.find_element(*TestLocators.SEARCH_FORM)
    search_form = SearchForm(driver, TestLocators.SEARCH_FORM_LOCATOR)
    # some_element = driver.find_element(*TestLocators.SEARCH_FORM_LOCATOR)
    # driver.implicitly_wait(2)
    # WebDriverWait(driver, 5).until_not(expected_conditions.visibility_of_element_located(driver.find_element(*TestLocators.SEARCH_FORM_LOCATOR)))
    search_form.search_input.search_with_wait('Moscow')
    search_form.search_button.click()
    region_id = 2395
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
