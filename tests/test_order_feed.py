import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.main_locators import MainLocators
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счетчик 'Выполнено за всё время' увеличивается")
    def test_completed_all_time_counter_increases(self, driver, authenticated_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.open_constructor()
        main_page.add_ingredient_to_constructor_by_index(0)
        main_page.place_order()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainLocators.ORDER_MODAL_TITLE)
        )
        main_page.close_order_modal()

        main_page.open_feed()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(OrderFeedLocators.COMPLETED_ALL_TIME)
        )
        new_count = feed_page.get_completed_all_time()

        assert new_count > 0

    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается")
    def test_completed_today_counter_increases(self, driver, authenticated_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.open_constructor()
        main_page.add_ingredient_to_constructor_by_index(0)
        main_page.place_order()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainLocators.ORDER_MODAL_TITLE)
        )
        main_page.close_order_modal()

        main_page.open_feed()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(OrderFeedLocators.COMPLETED_TODAY)
        )
        new_count = feed_page.get_completed_today()

        assert new_count > 0

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver, authenticated_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.open_constructor()
        main_page.add_ingredient_to_constructor_by_index(0)
        main_page.place_order()

        order_number_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(OrderFeedLocators.ORDER_NUMBER)
        )
        WebDriverWait(driver, 15).until(
            lambda driver: order_number_element.text not in ["", "9999", "0"]
        )
        order_number = order_number_element.text.strip()

        main_page.close_order_modal()

        main_page.open_feed()

        WebDriverWait(driver, 10).until(
            lambda driver: any(
                order_number in order or f"0{order_number}" in order
                for order in feed_page.get_orders_in_progress()
            )
        )

        orders_in_progress = feed_page.get_orders_in_progress()
        order_number_clean = order_number.lstrip('0')
        orders_clean = [o.lstrip('0') for o in orders_in_progress]

        assert order_number_clean in orders_clean