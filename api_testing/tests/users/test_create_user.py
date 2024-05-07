import pytest
from selenium import webdriver


@pytest.fixture(params=[0, 1], ids=['chrome', 'firefox'])
def a(request):
    return request.param


@pytest.fixture(
    params=[{webdriver.Chrome}, webdriver.Firefox],
    ids=['chrome', 'firefox'])
def driver(request):
    driver = request.param['']
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver_chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver_firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    'driver_a',
    ['driver_chrome', 'driver_firefox']
)
def test_some(request, driver_a):
    driver = request.getfixturevalue(driver_a)
    main_page = MainPage(driver)
    assert False
