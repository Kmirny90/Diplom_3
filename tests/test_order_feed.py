import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage



@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счетчик 'Выполнено за всё время' увеличивается")
    def test_completed_all_time_counter_increases(self, driver, authenticated_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.open_constructor()
        main_page.add_ingredient_to_constructor_by_index(0)
        main_page.place_order()

        main_page.close_order_modal()

        main_page.open_feed()

        new_count = feed_page.get_completed_all_time()

        assert new_count > 0

    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается")
    def test_completed_today_counter_increases(self, driver, authenticated_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.open_constructor()
        main_page.add_ingredient_to_constructor_by_index(0)
        main_page.place_order()

        main_page.close_order_modal()

        main_page.open_feed()

        new_count = feed_page.get_completed_today()

        assert new_count > 0

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver, authenticated_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.open_constructor()
        main_page.add_ingredient_to_constructor_by_index(0)
        main_page.place_order()

        order_number = main_page.get_order_number()
        main_page.close_order_modal()

        main_page.open_feed()


        feed_page.wait_for_order_in_progress(order_number)

        orders_in_progress = feed_page.get_orders_in_progress()
        order_number_clean = order_number.lstrip('0')
        orders_clean = [o.lstrip('0') for o in orders_in_progress]

        assert order_number_clean in orders_clean