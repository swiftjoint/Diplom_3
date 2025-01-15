import allure
from data import DataUser, DRIVER_NAME
from locators.locators_constructor_page import LocatorsConstructor
from locators.locators_home_page import LocatorsHome
from locators.locators_lk_page import LocatorsLK
from locators.locators_order_page import LocatorsOrder
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажимаем на заказ, в ленте заказов')
    def click_to_order_open_win_with_details(self):
        self.click_to_element(LocatorsOrder.ID_IN_TAPE_ORDERS)

    @allure.step('Проверяем, что текст "Состав" отображается')
    def is_text_structure_visible(self):
        return self.is_element_visible(LocatorsOrder.WINDOWS_DETAILS_ORDERS)

    @allure.step('Входим в учетную запись')
    @allure.step('Переходим в историю заказов и забираем id заказа')
    @allure.step('Переходим в ленту заказов, и ищем тот id который мы забрали из истории заказов')
    def show_order_history_in_tape_orders(self):
        self.click_to_element(LocatorsHome.BTN_LOGIN_HOME)
        self.add_text_to_element(LocatorsLK.EMAIL_INPUT_XPATH, DataUser.LOGIN)
        self.add_text_to_element(LocatorsLK.PWD_INPUT_XPATH, DataUser.PWD)
        self.click_to_element(LocatorsLK.BTN_LOGIN)

        if DRIVER_NAME == 'chrome':
            self.click_to_element(LocatorsHome.BTN_LK)
        else:
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
            self.click_to_element(LocatorsHome.BTN_LK)

        if DRIVER_NAME == 'chrome':
            self.click_to_element(LocatorsLK.BTN_HISTORY_ORDER)
        else:
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
            self.click_to_element(LocatorsLK.BTN_HISTORY_ORDER)

        self.scroll_to_bottom()
        order_id_in_history = self.get_text_from_element(LocatorsOrder.HARD_ID_ORDER_IN_HISTORY_ORDERS)
        self.click_to_element(LocatorsHome.BTN_TAPE_ORDERS)
        order_id_in_tape = self.get_text_from_element(LocatorsOrder.HARD_ID_ORDER_IN_TAPE_ORDERS)

        return order_id_in_history, order_id_in_tape

    @allure.step('Переходим в ленту заказов и забираем значение счетчика "Выполнено за всё время"')
    @allure.step('Переходим в ЛК и логинимся')
    @allure.step('Создаем заказ, и снова идем в ленту заказов '
                 'и забираем новое значение счетчика "Выполнено за всё время"')
    def new_create_order_total_count_rise(self):
        initial_counter_value = self.get_counter_value(LocatorsOrder.TOTAL_COUNTER_SCORE)
        self.click_to_element(LocatorsHome.BTN_LK)
        self.add_text_to_element(LocatorsLK.EMAIL_INPUT_XPATH, DataUser.LOGIN)
        self.add_text_to_element(LocatorsLK.PWD_INPUT_XPATH, DataUser.PWD)
        self.click_to_element(LocatorsLK.BTN_LOGIN)

        if DRIVER_NAME == 'chrome':
            self.move_the_element_chrome(LocatorsConstructor.ELEMENT_BULKA, LocatorsHome.ADD_INGREDIENT_ORDER)
        else:
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
            self.drag_and_drop_element_firefox(LocatorsConstructor.ELEMENT_BULKA, LocatorsHome.ADD_INGREDIENT_ORDER)
        self.click_to_element(LocatorsHome.BTN_ORDER_ARRANGE)
        self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
        self.click_to_element(LocatorsConstructor.BTN_CLOSE_WINDOWS_DETAILS_INGREDIENT)
        self.click_to_element(LocatorsHome.BTN_TAPE_ORDERS)
        new_counter_value = self.get_counter_value(LocatorsOrder.TOTAL_COUNTER_SCORE)

        return initial_counter_value, new_counter_value

    @allure.step('Переходим а ленту заказов и забираем значение счетчика "Выполнено за сегодня"')
    @allure.step('Переходим в ЛК и логинимся')
    @allure.step('Создаем заказ, и снова идем в ленту заказов '
                 'и забираем новое значение счетчика "Выполнено за сегодня"')
    def new_create_order_total_count_today_rise(self):
        initial_counter_value = self.get_counter_value(LocatorsOrder.COUNTER_SCORE_TODAY)
        self.click_to_element(LocatorsHome.BTN_LK)
        self.add_text_to_element(LocatorsLK.EMAIL_INPUT_XPATH, DataUser.LOGIN)
        self.add_text_to_element(LocatorsLK.PWD_INPUT_XPATH, DataUser.PWD)
        self.click_to_element(LocatorsLK.BTN_LOGIN)

        if DRIVER_NAME == 'chrome':
            self.move_the_element_chrome(LocatorsConstructor.ELEMENT_BULKA, LocatorsHome.ADD_INGREDIENT_ORDER)
        else:
            self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
            self.drag_and_drop_element_firefox(LocatorsConstructor.ELEMENT_BULKA, LocatorsHome.ADD_INGREDIENT_ORDER)
        self.click_to_element(LocatorsHome.BTN_ORDER_ARRANGE)
        self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
        self.click_to_element(LocatorsConstructor.BTN_CLOSE_WINDOWS_DETAILS_INGREDIENT)
        self.click_to_element(LocatorsHome.BTN_TAPE_ORDERS)
        new_counter_value = self.get_counter_value(LocatorsOrder.COUNTER_SCORE_TODAY)

        return initial_counter_value, new_counter_value

    @allure.step('Заполняем "Email" и "Пароль"')
    @allure.step('Создаем заказ, забираем номер созданного заказа')
    @allure.step('Идем в ленту заказов и забираем номер, в графе "В работе"')
    def new_create_order_displayed_in_work(self):
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
        self.wait_element_invisibility(LocatorsHome.HIDDEN_ELEMENT)
        number_order = self.get_counter_value(LocatorsOrder.NUMBER_ORDER)
        self.click_to_element(LocatorsConstructor.BTN_CLOSE_WINDOWS_DETAILS_INGREDIENT)
        self.click_to_element(LocatorsHome.BTN_TAPE_ORDERS)
        value_in_work = self.get_counter_value(LocatorsOrder.NUMBER_ORDER_IN_TAPE_ORDERS)

        return number_order, value_in_work
