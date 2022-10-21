from selenium.webdriver.common.by import By


class MainPage:
    url_main = 'https://stellarburgers.nomoreparties.site/'  # адрес главной страницы
    auth_button_main = By.XPATH, '//*[contains(@class, "button_button")]'  # кнопка "Войти" на главной странице
    registration_button = By.XPATH, '(//*[contains(@class, "Auth_link")])[1]'  # кнопка зарегистрироваться
    name_registration_field = By.XPATH, '(//*[contains(@class, "input__textfield")])[1]'  # инпут имени
    email_registration_field = By.XPATH, '(//*[contains(@class, "input__textfield")])[1]'  # инпут email
    password_registration_field = By.XPATH, '(//*[contains(@class, "input__textfield")])[1]'  # инпут password
























# https://stellarburgers.nomoreparties.site/login
class LoginPage:
    url_login = 'https://stellarburgers.nomoreparties.site/login' # адрес страницы авторизации
    reg_button = By.CSS_SELECTOR, '.Auth_link__1fOlj' # кнопка "Зарегистрироваться" на странице авторизации
    log_fld = By.XPATH, "//div/h2[text()='Вход']" # заголовок "Вход" на странице авторизации
    fld_email = By.XPATH, '//fieldset[1]/div/div/input' # поле email на странице авторизации
    fld_pass = By.XPATH, '//fieldset[2]/div/div/input' # поле пароля на странице авторизации
    auth_button_login = By.XPATH, '//div/form/button' # кнопка "Войти" на странице авторизации
    rec_button = By.XPATH, '//div/p[2]/a' # кнопка "Восстановить пароль" на странице авторизации
    test_email = '123@ya.ru' # тестовая почта
    test_pass = '123456' # тестовый пароль
# https://stellarburgers.nomoreparties.site/register
class RegistrationPage:
    fld_name = By.XPATH, '//fieldset[1]/div/div/input' # поле "Имя" на странице регистрации
    fld_email = By.XPATH, '//fieldset[2]/div/div/input' # поле "Email" на странице регистрации
    fld_pass = By.XPATH, '//fieldset[3]/div/div/input' # поле "Пароль" на странице регистрации
    reg_button = By.XPATH, '//div/form/button' # кнопка "Зарегистрироваться" на странице регистрации
    err_fld = By.XPATH, '//fieldset[3]/div/p[@class]' # сообщение с ошибкой на странице регистрации
    auth_button_reg = By.XPATH, '//div/p/a' # кнопка "Войти" на странице регистрации
    reg_fld = By.XPATH, '//div/h2' # заголовок "Регистрация" на странице регистрации
# https://stellarburgers.nomoreparties.site/forgot-password
class ForgotPage:
    fld_forgot_password = By.XPATH, '//div/h2' # заголовок "Восстановление пароля" на странице восстановления пароля
    auth_button_forgot = By.XPATH, '//div/p/a' # кнопка "Войти" на странице восстановления пароля
    forgot_button = By.XPATH, '//form/button' # кнопка "Восстановить" на странице восстановления пароля
#https://stellarburgers.nomoreparties.site/account/profile
class PrivateOffice:
    profile = By.XPATH, "//ul/li[1]/a[@href= '/account/profile']" # кнопка "Профиль" в личном кабинете
    history = By.XPATH, '//ul/li[2]/a[@href= "/account/order-history"]' # кнопка "История заказов" в личном кабинете
    exit_button = By.XPATH, '//ul/li[3]/button' # кнопка "Выход" в личном кабинете
    message = By.XPATH, '//div/nav/p' #сообщение "В этом разделе вы можете изменить свои персональные данны