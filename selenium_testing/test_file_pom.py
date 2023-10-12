from selenium_testing.students_locators import MainPage


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def set_text_to_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)


class BurgerLoginPage(BasePage):

    # def login_button(self):
    #     return self.driver.find_element(*MainPage.auth_button_main)
    #
    # def registration_locator(self):
    #     return self.driver.find_element(*MainPage.registration_button)
    #
    # def name_registration_locator(self):
    #     return self.driver.find_element(*MainPage.name_registration_field)
    #
    # def email_registration_locator(self):
    #     return self.driver.find_element(*MainPage.email_registration_field)
    #
    # def password_registration_locator(self):
    #     return self.driver.find_element(*MainPage.password_registration_field)
    #
    # def set_name(self, name):
    #     self.name_registration_locator().send_keys(name)
    #
    # def set_email(self, email):
    #     self.email_registration_locator().send_keys(email)
    #
    # def set_password(self, password):
    #     self.password_registration_locator().send_keys(password)
    #
    # def click_login_button(self):
    #     self.login_button().click()
    #
    # def text_login_button(self):
    #     self.login_button().text()
    #
    # def click_registration_button(self):
    #     self.registration_locator().click()

    def register(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_registration_button()

    def get_question(self, number):
        method, locator = QUESTION_LOCATOR
        locator = locator.format(number)
        self.driver.find_element(method, locator)


QUESTION_LOCATOR = By.Хpath, '//*[@class="question-locator-class-{}"]'
