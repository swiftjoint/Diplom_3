from selenium.webdriver.common.by import By


class LocatorsPwd:
    BTN_RESET_PWD = (By.XPATH, "//a[text()='Восстановить пароль']")  # Окно входа, кнопка 'Восстановить пароль'
    BTN_RESET = (By.XPATH, "//button[text()='Восстановить']")  # Окно восстановления пароля, кнопка 'Восстановить'
    FORM_EMAIL_PWD = (
        By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']"
    )  # Окно восстановление пароля, поле для ввода 'email'
    BTN_SAVE_PWD = (By.XPATH, "//button[text()='Сохранить']")  # Окно восстановления пароля, кнопка 'Сохранить'
    BTN_VISIBILITY_PWD = (
        By.XPATH, ".//div[@class ='input__icon input__icon-action']"
    )  # Окно восстановления пароля, кнопка показа/скрытия пароля
    ACTIVELY_FIELD = (
        By.XPATH, "//label[contains(@class, 'placeholder-focused')]"
    )  # Окно восстановления пароля, подсветка поля 'Пароль'
