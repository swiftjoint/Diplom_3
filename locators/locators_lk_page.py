from selenium.webdriver.common.by import By


class LocatorsLK:
    BTN_LOGIN = (By.XPATH, "//button[text()='Войти']")  # Окно входа с полями майл и пароль, кнопка 'Войти'
    EMAIL_INPUT_XPATH = (
        By.XPATH, "//input[@name='name']")  # Окно входа, поле 'Email'
    PWD_INPUT_XPATH = (By.XPATH, "//input[@name='Пароль']")  # Окно входа, поле 'Пароль'
    BTN_HISTORY_ORDER = (By.XPATH, '//a[text()="История заказов"]')  # Окно ЛК, кнопка 'История заказов'
    ORDER_COMPLETE = (By.XPATH, '//p[text()="Выполнен"]')  # Окно истории заказов, надпись статуса заказа 'Выполнен'
    BTN_LOGOUT = (
        By.XPATH, "//button[contains(@class, 'Account_button') or text()='Выход']"
    )  # ЛК кнопка 'Выход'
