import pytest


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
