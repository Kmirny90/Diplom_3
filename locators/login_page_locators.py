from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_FORM = (By.XPATH, "//form[contains(@class, 'Auth_form')]")
