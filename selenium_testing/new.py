from selenium import webdriver

from selenium_testing.test_file_pom import BurgerLoginPage


class TestBurgersLogin:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/alena/Dev/praktikum_test/chromedriver')

    def test_registration(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')

        login_page = BurgerLoginPage(self.driver)

        login_page.click_login_button()

        login_page.register('Вася', '123@ya.ru', '123456')

        current_url = self.driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/register'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
