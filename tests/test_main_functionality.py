import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_constructor_navigation(self, driver):
        page = MainPage(driver)
        page.open_feed()
        page.open_constructor()
        assert page.is_constructor_opened()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_feed_navigation(self, driver):
        page = MainPage(driver)
        page.open_feed()
        assert page.is_feed_opened()

    @allure.title("Клик на ингредиент открывает модальное окно")
    def test_ingredient_modal_opens(self, driver):
        page = MainPage(driver)
        page.open_ingredient_modal()
        assert page.is_modal_opened()

    @allure.title("Модальное окно открывается при клике на ингредиент")
    def test_modal_opens(self, driver):
        page = MainPage(driver)
        page.open_ingredient_modal()
        assert page.is_modal_opened()

    @allure.title("Модальное окно закрывается по крестику")
    def test_modal_closes(self, driver):
        page = MainPage(driver)
        page.open_ingredient_modal()
        page.close_modal()
        assert page.is_modal_closed()

    @allure.title("При добавлении булки счетчик увеличивается на 2")
    def test_bun_counter_increases(self, driver):
        page = MainPage(driver)
        index = 0
        initial_count = page.get_ingredient_counter_by_index(index)
        page.add_ingredient_to_constructor_by_index(index)


        WebDriverWait(driver, 5).until(
            lambda driver: page.get_ingredient_counter_by_index(index) != initial_count
        )

        new_count = page.get_ingredient_counter_by_index(index)
        assert new_count == initial_count + 2

    @allure.title("При добавлении соуса счетчик увеличивается на 1")
    def test_sauce_counter_increases(self, driver):
        page = MainPage(driver)

        index = 2
        initial_count = page.get_ingredient_counter_by_index(index)
        page.add_ingredient_to_constructor_by_index(index)


        WebDriverWait(driver, 5).until(
            lambda driver: page.get_ingredient_counter_by_index(index) != initial_count
        )

        new_count = page.get_ingredient_counter_by_index(index)
        assert new_count == initial_count + 1
