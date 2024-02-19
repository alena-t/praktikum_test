from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@class="some-question-locator-0"]'
    QUESTION_LOCATOR_1 = By.XPATH, '//*[@class="some-question-locator-1"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@class="some-answer-locator-{}"]'
