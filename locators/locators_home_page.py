from selenium.webdriver.common.by import By


class LocatorsHome:
    BTN_LOGIN_HOME = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Главная, кнопка 'Войти в аккаунт'
    BTN_LK = (By.XPATH, "//p[text()='Личный Кабинет']")  # Главная, кнопка 'Личный Кабинет'
    HIDDEN_ELEMENT = (
        By.XPATH, '//*[contains(@class, "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]'
    )  # Элемент который перекрывает кнопку 'Личный Кабинет" на firefox
    BTN_TAPE_ORDERS = (By.XPATH, "//p[text()='Лента Заказов']")  # Кнопка'Лента заказов'
    BTN_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Главная, кнопка 'Конструктор'
    ADD_INGREDIENT_ORDER = (
        By.XPATH,
        "//div[contains(@class, 'constructor-element') and contains(@class, 'constructor-element_pos_top')]//span[contains(@class, 'constructor-element__text') and text()='Перетяните булочку сюда (верх)']"
    )  # Элемент для приема ингредиетов
    BTN_ORDER_ARRANGE = (By.XPATH, "//button[text()='Оформить заказ']")  # Главная, кнопка 'Оформить Заказ'
