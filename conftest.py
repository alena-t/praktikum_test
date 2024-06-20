import pytest

from test_page_object.pages.main_page import MainPage


class UserRegistration:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

@pytest.fixture
def example_correct_user():
    return {'name': 'Иван', 'login': 'IvanSukhanov3666@yandex.ru', 'password': '123456'}

@pytest.fixture
def example_not_correct_user():
    return UserRegistration(name='', login='IvanSukhanov366', password='12345')


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope='function')
def order_page(driver):
    return OrderPage(driver)


@pytest.fixture
def some_data():
    return 'some'


