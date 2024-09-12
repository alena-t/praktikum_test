from selenium_testing.test_file_pom import BasePage


class SearchPage(BasePage):

    def select_some_item(self, num_item):
        elements = self.find_elements_with_wait(SearchPageLocators.ITEM_LOCATOR)
        return elements[num_item]

    def get_count_of_items(self):
        elements = self.find_elements_with_wait(SearchPageLocators.ITEM_LOCATOR)
        return len(elements)

