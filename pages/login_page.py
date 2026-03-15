import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self._driver.get(f"{self._driver.current_url}login")
        return self

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        email_field = self.wait_visible(LoginPageLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        password_field = self.wait_visible(LoginPageLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        return self

    @allure.step("Кликнуть кнопку 'Войти'")
    def click_login_button(self):
        button = self.wait_visible(LoginPageLocators.LOGIN_BUTTON)
        self._driver.execute_script("arguments[0].click();", button)
        from locators.main_locators import MainLocators
        self._wait.until(EC.visibility_of_element_located(MainLocators.ORDER_BUTTON))
        return self

    @allure.step("Выполнить полный логин")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        return self