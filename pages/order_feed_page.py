import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Получить счетчик 'Выполнено за всё время'")
    def get_completed_all_time(self) -> int:
        text = self.get_text(OrderFeedLocators.COMPLETED_ALL_TIME)
        return int(text)

    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_completed_today(self) -> int:
        text = self.get_text(OrderFeedLocators.COMPLETED_TODAY)
        return int(text)

    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self) -> list:
        elements = self._driver.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS_ITEMS)
        return [el.text for el in elements]

    @allure.step("Получить номера заказов из ленты")
    def get_order_numbers_from_feed(self) -> list:
        elements = self._driver.find_elements(*OrderFeedLocators.ORDER_ITEMS)
        return [el.text for el in elements]

    @allure.step("Ожидать появления заказа {order_number} в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=15):
        self._wait.until(
            lambda driver: any(
                order_number in order or f"0{order_number}" in order
                for order in self.get_orders_in_progress()
            )
        )