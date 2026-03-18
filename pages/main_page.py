import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MainPage(BasePage):

    @allure.step("Открыть конструктор")
    def open_constructor(self):
        self.click(MainLocators.CONSTRUCTOR_TAB)

    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        self.click(MainLocators.FEED_TAB)

    @allure.step("Проверить, что конструктор открыт")
    def is_constructor_opened(self) -> bool:
        return self.is_visible(MainLocators.CONSTRUCTOR_HEADER)

    @allure.step("Проверить, что лента заказов открыта")
    def is_feed_opened(self) -> bool:
        return self.is_visible(MainLocators.FEED_HEADER)

    @allure.step("Открыть модальное окно ингредиента")
    def open_ingredient_modal(self):
        self.click(MainLocators.INGREDIENT_ITEM)

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self) -> bool:
        return self.is_visible(MainLocators.MODAL)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainLocators.MODAL_CLOSE_BUTTON)
        self._wait.until(EC.invisibility_of_element_located(MainLocators.MODAL))

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self) -> bool:
        try:
            self._wait.until_not(EC.visibility_of_element_located(MainLocators.MODAL))
            return True
        except:
            return False

    @allure.step("Получить счетчик ингредиента по индексу {index}")
    def get_ingredient_counter_by_index(self, index):
        ingredients = self._driver.find_elements(*MainLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            try:
                counters = ingredients[index].find_elements(*MainLocators.INGREDIENT_COUNTER)
                if counters:
                    return int(counters[0].text)
            except:
                return 0
        return 0

    @allure.step("Добавить ингредиент в конструктор по индексу {index}")
    def add_ingredient_to_constructor_by_index(self, index):
        ingredients = self._driver.find_elements(*MainLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            ingredient = ingredients[index]
            constructor_area = self._driver.find_element(*MainLocators.CONSTRUCTOR_AREA)
            self.drag_and_drop(ingredient, constructor_area)

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(MainLocators.ORDER_BUTTON)

        self._wait.until(EC.visibility_of_element_located(MainLocators.ORDER_MODAL_TITLE))

    @allure.step("Получить номер заказа")
    def get_order_number(self) -> str:

        element = self._wait.until(EC.visibility_of_element_located(MainLocators.ORDER_NUMBER))


        self._wait.until(
            lambda driver: element.text not in ["", "9999", "0"]
        )

        return element.text.replace('#', '').strip()

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click(MainLocators.ORDER_MODAL_CLOSE_BUTTON)

        self._wait.until(EC.invisibility_of_element_located(MainLocators.ORDER_MODAL_TITLE))

    @allure.step("Ожидать изменения счетчика ингредиента {index}")
    def wait_for_counter_change(self, index, initial_count, timeout=5):
        WebDriverWait(self._driver, timeout).until(
            lambda driver: self.get_ingredient_counter_by_index(index) != initial_count
        )



