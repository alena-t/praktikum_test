from selenium.webdriver.chrome.service import Service

from selenium_testing.students_locators import LoginPage as LP
from selenium import webdriver

fld_email = By.XPATH, '//fieldset[{}]/div/div/input'

driver = webdriver.Chrome(service=Service(executable_path='/Users/alena/Dev/praktikum_test/chromedriver'))
# method = By.XPATH, path = '//fieldset[{}]/div/div/input'
method, path = LP.fld_email
# *LP.fld_email == method = By.XPATH, path = '//fieldset[{}]/div/div/input'
path = path.format("1")
email_field = driver.find_element(method, path)
path = path.format(2)
password_field = driver.find_element(method, path)
