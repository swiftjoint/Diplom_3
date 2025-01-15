from data import DataUser, DRIVER_NAME
from locators.locators_home_page import LocatorsHome
from locators.locators_lk_page import LocatorsLK
from pages.base_page import BasePage
import allure


class LkPage(BasePage):
    @allure.step('На главной странице, кликаем на кнопку "Личный Кабинет"')
    def go_to_personal_cabinet(self):
        self.click_to_element(LocatorsHome.BTN_LK)

    @allure.step('Проверяем, что есть текст "Войти"')
    def is_text_on_btn(self):
        return self.get_text_from_element(LocatorsLK.BTN_LOGIN)

    @allure.step('На главной странице, кликаем на кнопку "Личный Кабинет"')
    @allure.step('Заполняем поля "Email" и "Пароль", затем нажимаем кнопку "Войти"')
    @allure.step('Переходим в ЛК, и нажимаем кнопку "История заказов"')
    def go_to_history_page(self):
        self.click_to_element(LocatorsHome.BTN_LK)
        self.add_text_to_element(LocatorsLK.EMAIL_INPUT_XPATH, DataUser.LOGIN)
        self.add_text_to_element(LocatorsLK.PWD_INPUT_XPATH, DataUser.PWD)

        if DRIVER_NAME == 'chrome':
            self.click_to_element(LocatorsLK.BTN_LOGIN)
            self.click_to_element(LocatorsHome.BTN_LK)
        else:
            self.click_to_element(LocatorsLK.BTN_LOGIN)
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
            self.click_to_element(LocatorsHome.BTN_LK)
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)

        self.click_to_element(LocatorsLK.BTN_HISTORY_ORDER)

    @allure.step('Проверяем, что теккст "Выполнен" отображается')
    def is_text_complete_visible(self):
        return self.is_element_visible(LocatorsLK.ORDER_COMPLETE)

    @allure.step('На главной странице, кликаем на кнопку "Войти в аккаунт"')
    @allure.step('В окне входа, заполняем поля "Email" и "Пароль",  затем нажимаем кнопку "Войти"')
    @allure.step('Переходим в ЛК, и нажимаем кнопку "Выход"')
    def logout_lk(self):
        self.click_to_element(LocatorsHome.BTN_LOGIN_HOME)
        self.add_text_to_element(LocatorsLK.EMAIL_INPUT_XPATH, DataUser.LOGIN)
        self.add_text_to_element(LocatorsLK.PWD_INPUT_XPATH, DataUser.PWD)
        if DRIVER_NAME == 'chrome':
            self.click_to_element(LocatorsLK.BTN_LOGIN)
            self.click_to_element(LocatorsHome.BTN_LK)
        else:
            self.click_to_element(LocatorsLK.BTN_LOGIN)
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
            self.click_to_element(LocatorsHome.BTN_LK)
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
        self.click_to_element(LocatorsLK.BTN_LOGOUT)
