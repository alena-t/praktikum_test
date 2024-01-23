import time
from locators import TestLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration_and_logout():
    # Регистрация
    user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
    user_password = '123456'
    driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
    driver.get("https://stellarburgers.nomoreparties.site/")
    # нашел кнопку личный кабинет/нажал на нее
    driver.find_element(TestLocators.PERSONAL_ACCOUNT).click()
    # ожидаю загрузку элемента
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
    # ввожу данные в поля для входа в аккаунт
    driver.find_element(TestLocators.FIELD_NAME).send_keys(user_mail)
    driver.find_element(TestLocators.FIELD_PASSWORD).send_keys(user_password)
    driver.find_element(TestLocators.BUTTON_ENTER).click()
    time.sleep(1)
    # перехожу в личный кабинет
    driver.find_element(TestLocators.PERSONAL_ACCOUNT).click()
    # выхожу из аккаунта
    driver.find_element(TestLocators.BUTTON_EXIT).click()
    cur_url = 'https://stellarburgers.nomoreparties.site/account'
    assert driver.current_url == cur_url
    driver.quit()
