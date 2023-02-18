import pytest
from selenium import webdriver

from selenium_testing.elements_to_find import TestLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    element = driver.find_element(*TestLocators.ROOM_WRAPPER)
    driver.execute_script(arguments[0].click(), element)
    driver.execute_script(arguments[0].location_once_scrolled_into_view(), element)
    return driver
