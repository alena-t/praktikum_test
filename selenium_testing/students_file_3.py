from selenium import webdriver
# from tests.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# def test_logo_transition():
#     driver = webdriver.Chrome(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/chromedriver")
#
#     driver.get("https://stellarburgers.nomoreparties.site/")
#     personal_button = driver.find_elements(*TestLocators.Search_button_personal_button_main_locator)[0]
#     personal_button.click()
#     driver.get("https://stellarburgers.nomoreparties.site/login")
#
#     email = driver.find_element(*TestLocators.Input_email_locator).send_keys("user169@yandex.ru")
#     WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='user169@yandex.ru']")))
#
#     password = driver.find_element(*TestLocators.Input_password_locator).send_keys("Mir1941@")
#     WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//input[@value='Mir1941@']")))
#
#     driver.find_element(*TestLocators.Log_in_locator).click()
#
#     driver.execute_script("scrollBy(0,250);")
#
#     personal_button = driver.find_element(*TestLocators.Search_button_personal_button_main_locator).click()
#
#     WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".svg")))
#
#     logo = driver.find_element(*TestLocators.Logo_button_locator).click()
#
#     driver.get("https://stellarburgers.nomoreparties.site/")
#     assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
#
#     driver.quit()


def test_scooter_time():
    driver = webdriver.Chrome(executable_path="/Users/alena/Dev/praktikum_test/chromedriver")

    driver.get("https://qa-scooter.praktikum-services.ru/order")
    cookie_button = driver.find_element(By.XPATH, '//*[contains(@class, "App_CookieButton")]')
    cookie_button.click()
    name_field = driver.find_element(By.XPATH, '//input[contains(@class,"Input_Responsible")])[1]')
    name_field.send_keys("Иван")
    last_name_field = driver.find_element(By.XPATH, '(//*[contains(@class,"Input_Responsible")])[2]')
    last_name_field.send_keys("Пупкин")
    address = driver.find_element(By.XPATH, '(//*[contains(@class,"Input_Responsible")])[3]')
    address.send_keys("ул. Тверская, д 5")
    phone = driver.find_element(By.XPATH, '(//*[contains(@class,"Input_Responsible")])[4]')
    phone.send_keys("+71234567890")

    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    driver.quit()
