from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import UrlPage
from locators.locators_constructor_page import LocatorsConstructor
from locators.locators_order_page import LocatorsOrder
from pages.constructor_page import ConstructorPage
import allure


class TestConstructor:
    @allure.title('Проверяем переход по кнопке "Кноструктор"')
    def test_to_go_click_on_constructor(self, driver):
        driver.get(UrlPage.PAGE_URL_LOGIN)
        constructor_page = ConstructorPage(driver)
        constructor_page.to_go_click_on_constructor()
        result = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsConstructor.BTN_CONSTRUCTOR_BULKI)
        )
        assert result.is_displayed()

    @allure.title('Проверяем переход по кнопке "Лента Заказов"')
    def test_to_go_click_on_tape_orders(self, driver):
        driver.get(UrlPage.PAGE_URL)
        constructor_page = ConstructorPage(driver)
        constructor_page.to_go_click_on_tape_orders()
        result = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsOrder.HEAD_TAPE_ORDERS)
        )
        assert result.is_displayed()

    @allure.title('Проверяем, если кликнуть на ингредиент, откроется окно с деталями')
    def test_click_to_ingredient(self, driver):
        driver.get(UrlPage.PAGE_URL)
        constructor_page = ConstructorPage(driver)
        constructor_page.click_to_ingredient()
        result = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsConstructor.DETAILS_INGREDIENT)
        )
        assert result.is_displayed()

    @allure.title('Проверяем, что окно с деталями ингредиента, закрывается по нажатию на крестик')
    def test_click_to_ingredient(self, driver):
        driver.get(UrlPage.PAGE_URL)
        constructor_page = ConstructorPage(driver)
        constructor_page.close_windows_details_ingredient()
        result = WebDriverWait(driver, 10).until(
            expected_conditions.invisibility_of_element_located(LocatorsConstructor.MODAL_WINDOWS)
        )
        assert result is True, 'Окно, не закрылось'

    @allure.title('Проверяем, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_in_order_count_rise(self, driver):
        driver.get(UrlPage.PAGE_URL)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_in_order_count_rise()
        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(LocatorsConstructor.COUNTER_INGREDIENT, '2')
        )

        counter_element = driver.find_element(*LocatorsConstructor.COUNTER_INGREDIENT)
        counter_text = counter_element.text

        assert counter_text == '2', f"Ожидалось значение '2', но получено '{counter_text}'"

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_auth_user_can_place_order(self, driver):
        driver.get(UrlPage.PAGE_URL)
        constructor_page = ConstructorPage(driver)
        constructor_page.auth_user_can_place_order()
        result = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsOrder.ID_ORDER_IN_WINDOWS)
        )
        assert result.is_displayed()
