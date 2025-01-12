from selenium.webdriver.common.by import By


class LocatorsOrder:
    HEAD_TAPE_ORDERS = (By.XPATH, "//h1[text()='Лента заказов']")  # Заголовок в ленте заказов 'Лента заказов'
    ID_ORDER_IN_WINDOWS = (
        By.XPATH, "//p[text()='идентификатор заказа']"
    )  # Окно оформленого заказа,заголовок 'идентификатор заказа'
    ID_IN_TAPE_ORDERS = (
        By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]"
    )  # ID заказа, в ленте заказов
    WINDOWS_DETAILS_ORDERS = (
        By.XPATH, "//p[contains(text(), 'Cостав') and contains(@class, 'text')]"
    )  # Слово "Состав", в окне с деталями о заказе
    HARD_ID_ORDER_IN_HISTORY_ORDERS = (
        By.XPATH, "//p[contains(text(), '#0168143')]"
    )  # Конкретный ID заказа, из истории заказов
    HARD_ID_ORDER_IN_TAPE_ORDERS = (
        By.XPATH, "//p[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(text(), '#0168143')]"
    )  # Конкретный ID заказа, из ленты заказов
    TOTAL_COUNTER_SCORE = (
        By.XPATH,"//p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text') and contains(@class, 'text_type_digits-large')]"
    )  # Общий счетчик заказов
    COUNTER_SCORE_TODAY = (
        By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text') and contains(@class, 'text_type_digits-large')])[2]"
    )  # Счетчик заказов за сегодня
    NUMBER_ORDER_IN_TAPE_ORDERS = (
        By.XPATH, "(//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')])[6]"
    )  # Номер оформленного заказа, в графе "В работе"
    NUMBER_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")  # Номер заказа, в окне
