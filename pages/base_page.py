import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._wait = WebDriverWait(driver, timeout)

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        element = self.wait_clickable(locator)
        self._driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self._driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator) -> str:
        return self.wait_visible(locator).text

    @allure.step("Проверка видимости элемента {locator}")
    def is_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    @allure.step("Перетаскивание элемента")
    def drag_and_drop(self, source_element, target_element):
        self._driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = new DragEvent('dragstart', { bubbles: true });
            source.dispatchEvent(evt);

            evt = new DragEvent('dragenter', { bubbles: true });
            target.dispatchEvent(evt);

            evt = new DragEvent('dragover', { bubbles: true });
            target.dispatchEvent(evt);

            evt = new DragEvent('drop', { bubbles: true });
            target.dispatchEvent(evt);

            evt = new DragEvent('dragend', { bubbles: true });
            source.dispatchEvent(evt);
        """, source_element, target_element)