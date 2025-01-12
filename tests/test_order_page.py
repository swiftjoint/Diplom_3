import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import UrlPage
from locators.locators_order_page import LocatorsOrder
from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_to_order_open_win_with_details(self, driver):
        driver.get(UrlPage.PAGE_URL_TAPE_ORDER)
        order_page = OrderPage(driver)
        order_page.click_to_order_open_win_with_details()
        result = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(LocatorsOrder.WINDOWS_DETAILS_ORDERS)
        )
        assert result.is_displayed()

    @allure.title('Проверяем, что заказы пользователя из раздела "История заказов" '
                  'отображаются на странице "Лента заказов"')
    def test_show_order_history_in_tape_orders(self, driver):
        driver.get(UrlPage.PAGE_URL)
        order_page = OrderPage(driver)
        order_id_in_history, order_id_in_tape = order_page.show_order_history_in_tape_orders(driver)

        assert order_id_in_history == order_id_in_tape, \
            f"ID заказов не совпадают: {order_id_in_history} != {order_id_in_tape}"

    @allure.title('Провермяем, что при создании нового заказа, счётчик "Выполнено за всё время" увеличивается')
    def test_new_create_order_total_count_rise(self, driver):
        driver.get(UrlPage.PAGE_URL_TAPE_ORDER)
        order_page = OrderPage(driver)
        initial_counter_value, new_counter_value = order_page.new_create_order_total_count_rise()

        assert new_counter_value > initial_counter_value, \
            f"Счетчик не увеличился: {initial_counter_value} != {new_counter_value}"

    @allure.title('Провермяем, что при создании нового заказа, счётчик "Выполнено за сегодня" увеличивается')
    def test_new_create_order_total_count_today_rise(self, driver):
        driver.get(UrlPage.PAGE_URL_TAPE_ORDER)
        order_page = OrderPage(driver)
        initial_counter_value, new_counter_value = order_page.new_create_order_total_count_today_rise()

        assert new_counter_value > initial_counter_value, \
            f"Счетчик не увеличился: {initial_counter_value} != {new_counter_value}"

    @allure.title('Провермяем, что при создании нового заказа, номер заказа отображается в ленте заказов "В работе"')
    def test_new_create_order_displayed_in_work(self, driver):
        driver.get(UrlPage.PAGE_URL)
        order_page = OrderPage(driver)
        number_order, value_in_work = order_page.new_create_order_displayed_in_work()

        assert number_order == value_in_work, \
            f"Номер заказа не отображается 'В работе': {number_order} != {value_in_work}"
