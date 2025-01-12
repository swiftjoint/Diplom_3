from data import DataUser
from locators.locators_home_page import LocatorsHome
from locators.locators_pwd_page import LocatorsPwd
from pages.base_page import BasePage
import allure


class PwdPage(BasePage):

    @allure.step('На главной странице, кликаем на кнопку "Войти в аккаунт"')
    @allure.step('На странице входа, кликаем на кнопку "Восстановить пароль"')
    def go_to_page_pwd_recovery(self):
        self.click_to_element(LocatorsHome.BTN_LOGIN_HOME)
        self.click_to_element(LocatorsPwd.BTN_RESET_PWD)

    @allure.step('На странице восстановления пароля, вводим "email" и кликаем на кнопку "Восстановить"')
    def input_email_and_click_recover_btn(self):
        self.add_text_to_element(LocatorsPwd.FORM_EMAIL_PWD, DataUser.LOGIN)
        self.click_to_element(LocatorsPwd.BTN_RESET)

    @allure.step('На странице восстановления пароля, кликаем по кнопке показать/скрыть пароль')
    def toggle_pwd_visibility_and_actively_field(self):
        self.click_to_element(LocatorsPwd.BTN_VISIBILITY_PWD)
