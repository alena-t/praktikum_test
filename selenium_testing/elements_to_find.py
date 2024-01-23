from selenium.webdriver.common.by import By


def contains(class_name):
    return f'//*[contains(concat(" ",normalize-space(@class)," ")," {class_name} ")]'


class TestLocators:
    SEARCH_FORM_LOCATOR = By.XPATH, '//*[@class="homepage-search-form-wrapper"]'
    SEARCH_INPUT_FIELD = \
        By.XPATH, '//*[contains(@class, "SearchForm-module__destination")]//*[contains(@class, "Input-module__wrapper")]'
    SEARCH_BUTTON = \
        By.XPATH, '//*[@data-testid="search-button"]'

    CHECK_IN_BUTTON = \
        By.XPATH, '//*[contains(@class, "SearchForm-module__dates")]//*[contains(@class, "Input-module__wrapper")][1]'
    CHECK_OUT_BUTTON = \
        By.XPATH, '//*[contains(@class, "SearchForm-module__dates")]//*[contains(@class, "Input-module__wrapper")][2]'

    SUGGEST = By.XPATH, '//*[contains(@class, "Popup-module__popup")][div[contains(@class, "Suggest-module__title")]]'
    SUGGEST_HOTELS_LIST = By.XPATH, '//*[contains(@class, "Suggest-module__hotel")]'
    SUGGEST_REGIONS_LIST = By.XPATH, '//*[contains(@class, "Suggest-module__region")]'

    CALENDAR = By.XPATH, '//*[contains(@class, "Datepicker-module__popup")]'
    CALENDAR_MONTH_LIST = \
        By.XPATH, '(//*[contains(@class, "MonthsList-module__wrapper")]//div[contains(@class, "Month-module__title")])'
    CALENDAR_LAST_DAYS = \
        By.XPATH, '//*[contains(@class, "Month-module__wrapper")][last()]' \
                  '//*[contains(@class, "Week-module__week")][last()]' \
                  '//*[contains(@class, "Day-module__wrapper")]'
    CALENDAR_DAYS = By.XPATH, '//*[contains(@class, "Day-module__wrapper")]'
    CALENDAR_GRID_MONTH = \
        By.XPATH, '//*[contains(@class, "Grid-module__wrapper")]//*[contains(@class, "Month-module__wrapper")]'

    DAY_DISABLED = By.XPATH, './/div[contains(@class, "Day-module__inner_locked")]'
    DAY_TEMPLATE = By.XPATH, '//*[contains(@class, "Day-module__wrapper")]//*[text()="{}"]'
    MONTH_TITLE = By.XPATH, './/*[contains(@class, "Month-module__title")]'

    GUESTS_SELECTOR = \
        By.XPATH, '//*[contains(@class, "SearchForm-module__guests")]//*[contains(@class, "Input-module__wrapper")]'
    GUESTS_LABEL_FOCUSED = By.XPATH, './label[contains(@class, "Input-module__label_focused")]'

    ROOM_WRAPPER = By.XPATH, './/*[contains(@class, "Room-module__wrapper")]'
    ROOM_ADULTS_PLUS = By.XPATH, './/*[contains(@class, "Room-module__controlBox")][1]//*[text()="+"]'

    ROOM_KIDS_SELECT = By.XPATH, '//*[contains(@class, "Room-module__kidsBox")]//select'
    ROOM_KIDS_UNIT = By.XPATH, './/*[contains(@class, "Room-module__kidsBox")]//*[contains(@class, "KidUnit-module__wrapper")]'

    ROOM_KIDS_REMOVE_CHILD = By.XPATH, '(.//*[contains(@class, "Room-module__kidUnit")]//*[contains(@class, "KidUnit-module__removeButton")])'
    ROOM_KID_AGE = By.XPATH, './/*[contains(@class, "Room-module__kidUnit")]//*[contains(@class, "KidUnit-module__value")]'

    ADD_MORE_ROOMS_BUTTON = By.XPATH, '//*[contains(@class, "Form-module__addRoomBtn")]'
    BOOK_MORE_ROOMS_BUTTON = By.XPATH, '//*[contains(@class, "Form-module__bookMoreBtn")]'

    CHILDREN_AGE_SELECT = By.XPATH, '(//label[contains(@class, "Input-module__label")]/select)'

    SHOW_RATES_TEXT = By.XPATH, '//div[contains(@class, "B2CExtra-module__compareto")]/label'
    SHOW_RATES_CHECKBOX_CHECKED = \
        By.XPATH, \
        '//div[contains(@class, "B2CExtra-module__compareto")]/*/div[contains(@class, "Default-module__fakeCheckbox_checked")]'
    SHOW_RATES_CHECKBOX = \
        By.XPATH, \
        '//div[contains(@class, "B2CExtra-module__compareto")]/*/div[contains(@class, "Default-module__fakeCheckbox")]'

    B2B_B2C_POPUP = By.XPATH, '//*[@class="zenB2BonB2C"]'
    B2B_BUTTON_POPUP = By.XPATH, '//*[@class="zenB2BonB2C-button button-view-primary button-size-m"]'
    B2C_BUTTON_POPUP = By.XPATH, '//*[@class="zenB2BonB2C-buttons"]//*[contains(@class, "button-view-light")]'

    MOBILE_BANNER = By.XPATH, '//*[@class="zenmobile"]'
    MOBILE_BANNER_LEGAL_LINK = By.XPATH, '//*[@class="zenmobile-content-form-privacy-link"]'
    MOBILE_BANNER_CONTAINER = By.XPATH, contains('zenforminput')
    MOBILE_BANNER_INPUT = By.XPATH, '//input'
    MOBILE_BANNER_ERROR = By.XPATH, '//*[@class="zenforminput-errormessage"]'
    MOBILE_BANNER_SEND = By.XPATH, '//button'
    MOBILE_BANNER_SUCCESS_MESSAGE = By.XPATH, '//*[@class="zenmobile-content-form-success-message"]'
    MOBILE_BANNER_APP_STORE = By.XPATH, contains('zenmobile-content-links-link-appstore')
    MOBILE_BANNER_GOOGLE_PLAY = By.XPATH, contains('zenmobile-content-links-link-googleplay')

    EMAIL_COLLECTOR_WRAPPER = By.XPATH, '//*[@class="homepage-emailcollector-wrapper"]'
    EMAIL_COLLECTOR_PRIVACY_POLICY_LINK = By.XPATH, '//*[@class="zenemailcollector-policy-link link"]'
    EMAIL_COLLECTOR_CHECKBOX = By.XPATH, '//*[@class="zencheckbox-styled-checkbox"]'
    EMAIL_COLLECTOR_SUBSCRIBE_BUTTON = By.XPATH, '//button[@type="submit"]'
    EMAIL_COLLECTOR_VALIDATION_ERROR = By.XPATH, '//*[@class="zenforminput-errormessage"]'
    EMAIL_COLLECTOR_INPUT = By.XPATH, '//input[@name="email"]'
    EMAIL_COLLECTOR_TERMS_ERROR = By.XPATH, '//*[@class="zenemailcollector-policy-error"]'
    EMAIL_COLLECTOR_CLOSE = By.XPATH, '//*[@class="zenemailcollector-close"]'

    BLOG_WRAPPER = By.XPATH, '//*[@class="homepage-blog-wrapper"]'
    BLOG_ARTICLE = By.XPATH, '//*[@class="zenblog-posts-item"]'
    BLOG_HEADER = By.XPATH, '//*[@class="zenblog-title link"]'

    DATELESS = By.XPATH, '//*[contains(@class, "SearchForm-module__destination_hidden")]'
    SEARCH_FORM = By.XPATH, '//*[contains(@class, "SearchForm-module__wrapper")]'

    GUESTS_NUMBER = By.XPATH, './/*[starts-with(@class, "Input-module__controlLine")]'
    DONE_BUTTON = By.XPATH, '//*[contains(@class, "Form-module__buttons")]/button'

    CLOSE_POPUP = By.XPATH, '//*[@class="zenreactformoverlay-close"]'

    EMPTY_SUGGEST = By.XPATH, '//*[contains(@class, "Popup-module__popup")][div[contains(@class, "Suggest-module__emptySuggest")]]'

    HIDDEN_SF = By.XPATH, '//*[@class="zen-searchbutton"]'
    HIDDEN_SF_SERP = By.XPATH, '//*[@class="zen-hotels-leftbar-regioninfo"]'

    HIDDEN_SF_DATES = By.XPATH, '//*[@class="zenregioninfo-dates"]'
    HIDDEN_SF_ROOMS = By.XPATH, '//*[@class="zenregioninfo-rooms"]'
    HIDDEN_SF_REGION = By.XPATH, '//*[@class="link zenregioninfo-region"]'

class TestLocators2:
    pass
