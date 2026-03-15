from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Заголовок ленты
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    # Счетчики
    COMPLETED_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    # Заказы в работе
    ORDERS_IN_PROGRESS_ITEMS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")

    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2[contains(@class, 'digits')]")

    # Элементы заказов в ленте
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_text')]//p[contains(@class, 'digits')]")
