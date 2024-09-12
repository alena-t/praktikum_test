from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, URL):
        self.driver.get(URL)

    def find_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text()

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)

    def drag_and_drop_element(self, element_from, element_to):
        from_element = self.find_element_with_wait(element_from)
        to_element = self.find_element_with_wait(element_to)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()
