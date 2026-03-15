from selenium.webdriver.common.by import By


class MainLocators:
    # Навигация
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")

    # Заголовки
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    FEED_HEADER = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")

    # Область конструктора для drag-and-drop
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")

    # Модальное окно
    MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Модальное окно заказа
    ORDER_MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2[contains(@class, 'digits')]")
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//button")

    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2[contains(@class, 'digits-large')]")
