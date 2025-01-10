from selenium.webdriver.common.by import By


class LocatorsOrder:
    HEAD_TAPE_ORDERS = (By.XPATH, "//h1[text()='Лента заказов']")  # Заголовок в ленте заказов 'Лента заказов'
    ID_ORDER_IN_WINDOWS = (
        By.XPATH, "//p[text()='идентификатор заказа']"
    )  # Окно оформленого заказа,заголовок 'идентификатор заказа'
