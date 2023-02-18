from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium_testing.students_locators import MainPage as MP
from selenium_testing.students_locators import LoginPage as LP
from selenium.webdriver.chrome.options import Options


def test_transition_section_constructor_sauce_success():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(executable_path='/Users/alena/Dev/praktikum_test/chromedriver'), chrome_options=options)
    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.auth_button_main))
    button_main = driver.find_element(*MP.auth_button_main)
    button_main.click()
    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)
    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.user_sauce))
    element_sauce = driver.find_element(*MP.user_sauce)
    driver.execute_script(MP.scroll, element_sauce)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MP.user_sauce))
    transition_sauce = driver.find_element(*MP.active_element_constructor)
    driver.file_detector_context()
    assert transition_sauce.text == 'Соусы'
    driver.quit()


def test_transition_section_constructor_fillings_success():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver', chrome_options=options)
    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.auth_button_main))
    button_main = driver.find_element(*MP.auth_button_main)
    button_main.click()
    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)
    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.user_fillings))
    element_fillings = driver.find_element(*MP.user_fillings)
    driver.execute_script(MP.scroll, element_fillings)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MP.user_fillings))
    transition_fillings = driver.find_element(*MP.active_element_constructor)
    assert transition_fillings.text == 'Начинки'
    driver.quit()

def test_transition_section_constructor_loaf_success():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver', chrome_options=options)
    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.auth_button_main))
    button_main = driver.find_element(*MP.auth_button_main)
    button_main.click()
    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)
    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.user_loaf))
    driver.find_element(*MP.fillings).click()
    element_loaf = driver.find_element(*MP.user_loaf)
    driver.execute_script(MP.scroll, element_loaf)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MP.user_loaf))
    transition_loaf = driver.find_element(*MP.active_element_constructor)
    assert transition_loaf.text == 'Булки'
    driver.quit()


def test_buns_click(driver, example_correct_user):
    name_for_registration = example_correct_user.get('name')

    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]/span").click()


    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]/span").click()

    assert driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[1]/a[1]/p').text == 'Флюоресцентная булка R2-D3'

    driver.quit()
