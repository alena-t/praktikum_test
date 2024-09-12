from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@class="some-question-locator-{}"]'

    ANSWER_LOCATOR = By.XPATH, '//*[@class="some-answer-locator-{}"]'
