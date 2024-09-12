from unittest.mock import patch, Mock

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = Options()
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome()
    # driver.get(MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def some_dict():
    return {}


@pytest.fixture()
def some_dict_1():
    return 1, '', {}


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = BUN_NAME
    mock_bun.price = BUN_PRICE
    mock_bun.return_value.get_name = BUN_NAME
    mock_bun.return_value.get_price = BUN_PRICE
    return mock_bun


@pytest.mark.parametrize(
    'some',
    [
        'some_dict',
        'some_dict_1'
    ]
)
@patch('Prakticum.bun.Bun')
def test_some(some, mock_get_price):

    burger = Burger(
        ingredients=[mock_bun, mock_souce],
        price=BUN_PRICE
    )

    mock_get_price.name = some

    assert some == some_1 and some_2 != some_3, (
        f"{some=}, but {some_1=} and {some_2=}, but {some_3=}"
    )

