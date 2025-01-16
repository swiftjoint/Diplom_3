from selenium.webdriver.common.by import By


class LocatorsConstructor:
    BTN_CONSTRUCTOR_BULKI = (By.XPATH, "//span[text()='Булки']")  # Конструктор, раздел 'Булки'
    ELEMENT_BULKA = (
        By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"
    )  # Ингридиент в конструкторе 'Флюоресцентная булка R2-D3'
    DETAILS_INGREDIENT = (
        By. XPATH, "//h2[text()='Детали ингредиента']"
    )  # Заголовок всплывающего окна 'Детали ингредиента'
    BTN_CLOSE_WINDOWS_DETAILS_INGREDIENT = (
        By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS') and contains(@class, 'Modal_modal__close__TnseK')]"
    )  # Крестик закрытия окна с деталями ингредиента
    COUNTER_INGREDIENT = (
        By.XPATH, "//div[contains(@class, 'counter_counter__ZNLkj') and contains(@class, 'counter_default__28sqi')]//p"
    )  # Каунтер ингредиента

    MODAL_WINDOWS = (
        By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]"
    )  # Окно с деталями ингредиентов
