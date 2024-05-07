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
    driver.get(MAIN_PAGE_URL)
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
    return {1: ''}


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
def test_some(request, some):
    dict_dict = request.getfixturevalue(some)
    my_value = dict_dict[1]

    some_lst = []
    for som in some:
        mock_1 = Mock()
        some_lst.append(mock_1)

