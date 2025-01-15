import allure
from data import DRIVER_NAME, DataUser
from locators.locators_constructor_page import LocatorsConstructor
from locators.locators_lk_page import LocatorsLK
from locators.locators_order_page import LocatorsOrder
from pages.base_page import BasePage
from locators.locators_home_page import LocatorsHome


class ConstructorPage(BasePage):
    @allure.step('Кликаем на кнопку "Конструктор"')
    def to_go_click_on_constructor(self):
        if DRIVER_NAME == 'chrome':
            self.click_to_element(LocatorsHome.BTN_CONSTRUCTOR)
        else:
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
            self.click_to_element(LocatorsHome.BTN_CONSTRUCTOR)

    @allure.step('Проверяем, видна ли кнопка "Булки"')
    def is_bulki_button_visible(self):
        return self.is_element_visible(LocatorsConstructor.BTN_CONSTRUCTOR_BULKI)

    @allure.step('Кликаем на кнопку "Лента Заказов"')
    def to_go_click_on_tape_orders(self):
        self.click_to_element(LocatorsHome.BTN_TAPE_ORDERS)

    @allure.step('Проверяем, виден ли заголовок "Лента заказов"')
    def is_head_tape_order_visible(self):
        return self.is_element_visible(LocatorsOrder.HEAD_TAPE_ORDERS)

    @allure.step('Кликаем на ингредиент "Флюоресцентная булка R2-D3"')
    def click_to_ingredient(self):
        self.click_to_element(LocatorsConstructor.ELEMENT_BULKA)

    @allure.step('Проверяем, виден ли заголовок "Детали ингредиента"')
    def is_head_details_ingredient_visible(self):
        return self.is_element_visible(LocatorsConstructor.DETAILS_INGREDIENT)

    @allure.step('Кликаем на ингредиент "Флюоресцентная булка R2-D3"')
    @allure.step('На окне с деталями ингредиента, нажимаем крестик')
    def close_windows_details_ingredient(self):
        self.click_to_element(LocatorsConstructor.ELEMENT_BULKA)
        self.click_to_element(LocatorsConstructor.BTN_CLOSE_WINDOWS_DETAILS_INGREDIENT)

    @allure.step('Проверяем, что окно с деталями ингредиента закрыто')
    def is_details_window_closed(self):
        elements = self.driver.find_elements(*LocatorsConstructor.MODAL_WINDOWS)
        return len(elements) == 0

    @allure.step('Нажимаем на "Флюоресцентная булка R2-D3" и перетягиваем её в окно заказа')
    def add_ingredient_in_order_count_rise(self):
        if DRIVER_NAME == 'chrome':
            self.move_the_element_chrome(LocatorsConstructor.ELEMENT_BULKA, LocatorsHome.ADD_INGREDIENT_ORDER)
        else:
            self.drag_and_drop_element_firefox(LocatorsConstructor.ELEMENT_BULKA, LocatorsHome.ADD_INGREDIENT_ORDER)

    @allure.step('Получаем количество добавленных ингредиентов')
    def get_ingredient_count(self) -> int:
        count_text = self.get_text_from_element(LocatorsConstructor.COUNTER_INGREDIENT)
        return int(count_text) if count_text.isdigit() else 0

    @allure.step('Нажимаем на кнопку "Войти в аккаунт"')
    @allure.step('Заполняем поля, "Email" и "Пароль", затем жмен кнопку "Войти"')
    @allure.step('Перетаскиваем булку "Флюоресцентная булка R2-D3" в заказ и нажимаем кнопку "Оформить Заказ"')
    def auth_user_can_place_order(self):
        self.click_to_element(LocatorsHome.BTN_LOGIN_HOME)
        self.add_text_to_element(LocatorsLK.EMAIL_INPUT_XPATH, DataUser.LOGIN)
        self.add_text_to_element(LocatorsLK.PWD_INPUT_XPATH, DataUser.PWD)
        self.click_to_element(LocatorsLK.BTN_LOGIN)
        if DRIVER_NAME == 'chrome':
            self.move_the_element_chrome(LocatorsConstructor.ELEMENT_BULKA, LocatorsHome.ADD_INGREDIENT_ORDER)
        else:
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
            self.drag_and_drop_element_firefox(LocatorsConstructor.ELEMENT_BULKA, LocatorsHome.ADD_INGREDIENT_ORDER)
        self.click_to_element(LocatorsHome.BTN_ORDER_ARRANGE)

    @allure.step('Проверяем, что виден "Идентификатор заказа"')
    def is_id_order_visible(self):
        return self.is_element_visible(LocatorsOrder.ID_ORDER_IN_WINDOWS)
