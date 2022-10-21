import furl
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service

from selenium_testing.elements_to_find import TestLocators
from selenium_testing.page_files import SearchForm


def test_do_something():
    driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
    driver.get('https://ostrovok.ru/')
    search_form = SearchForm(driver, TestLocators.SEARCH_FORM_LOCATOR)
    search_form.search_input.search_with_wait('Moscow')
    search_form.search_button.click()
    region_id = 2395
    url = furl.furl(driver.current_url)
    search_page = url.args
    q_param = int(search_page['q'])
    assert q_param == region_id, \
        f'Serp q param is {q_param}, expected Moscow with id {region_id}'


def create_driver(request):
    path = str(request.fspath)
    path_0 = f"{path[:path.find('practicum_test')]}practicum_test/chromedriver"
    service = Service(path_0)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver


def do_something():
    # options = Options()
    # options.add_argument(f'window-size={DEFAULT_WINDOW_SIZE[0]},{DEFAULT_WINDOW_SIZE[1]}')
    # options.add_argument(f'lang={DEFAULT_LANG}')
    # driver creation
    # service = Service('/Users/alena/Dev/praktikum_test/chromedriver')
    # chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    driver = create_driver()
    # driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://ostrovok.ru/')
    search_form = SearchForm(driver, TestLocators.SEARCH_FORM_LOCATOR)
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
