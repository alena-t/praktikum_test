from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    def set_order(self, station_locator, name_locator, name,
                  last_name, address, time, button_locator):
        self.click_to_element(station_locator)
        self.add_text_to_element(name_locator, name)
        self.add_text_to_element(last_name, last_name)
        self.add_text_to_element(address, address)
        self.click_to_element(time)
        self.click_to_element(button_locator)

    def check_order(self, locator):
        return self.get_text_from_element(locator)
