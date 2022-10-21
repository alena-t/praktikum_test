import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium_testing.driver_settings import create_driver


@pytest.mark.usefixtures('example_correct_user', 'example_not_correct_user')
class TestLogin:

    def test_successful_registration_with_correct_username_and_password(self, example_correct_user):
        driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, './/button').click()
        WebDriverWait(driver, 1)
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 1)
        name_element = driver.find_element(By.XPATH, '(//*[@class="text input__textfield text_type_main-default"])[1]')
        name_element.send_keys(example_correct_user.get("name"))
        driver.find_element(By.XPATH, ".//label[text()='Email']").send_keys(example_correct_user.get("login"))
        driver.find_element(By.XPATH, ".//label[text()='Пароль']").send_keys(example_correct_user.get("password"))
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        driver.find_element(By.XPATH, ".// p[text() = 'Личный Кабинет']").click()
        assert driver.find_element(By.XPATH, ".//input[@value='Иван']")
        driver.quit()

    def test_unsuccessful_registration_with_empty_name(self, example_correct_user, example_not_correct_user):
        driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, './/button').click()
        WebDriverWait(driver, 1)
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 1)
        driver.find_element(By.XPATH, ".//label[text()='Имя']").send_keys(example_not_correct_user.name)
        driver.find_element(By.XPATH, ".//label[text()='Email']").send_keys(example_correct_user.login)
        driver.find_element(By.XPATH, ".//label[text()='Пароль']").send_keys(example_correct_user.password)
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        assert driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        driver.quit()

    def test_unsuccessful_registration_with_incorrect_email(self, example_correct_user, example_not_correct_user):
        driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, './/button').click()
        WebDriverWait(driver, 1)
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 1)
        driver.find_element(By.XPATH, ".//label[text()='Имя']").send_keys(example_correct_user.name)
        driver.find_element(By.XPATH, ".//label[text()='Email']").send_keys(example_not_correct_user.login)
        driver.find_element(By.XPATH, ".//label[text()='Пароль']").send_keys(example_correct_user.password)
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        assert driver.find_element(By.XPATH, "//p[text()='Такой пользователь уже существует']")
        driver.quit()

    def test_unsuccessful_registration_with_incorrect_password(self, example_correct_user, example_not_correct_user):
        driver = create_driver()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, './/button').click()
        WebDriverWait(driver, 1)
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 1)
        driver.find_element(By.XPATH, ".//label[text()='Имя']").send_keys(example_correct_user.name)
        driver.find_element(By.XPATH, ".//label[text()='Email']").send_keys(example_correct_user.login)
        driver.find_element(By.XPATH, ".//label[text()='Пароль']").send_keys(example_not_correct_user.password)
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        assert driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']")
        driver.quit()
