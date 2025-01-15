from data import UrlPage
from locators.locators_constructor_page import LocatorsConstructor
from pages.constructor_page import ConstructorPage
import allure


class TestConstructor:
    @allure.title('Проверяем переход по кнопке "Кноструктор"')
    def test_to_go_click_on_constructor(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_url(UrlPage.PAGE_URL_LOGIN)
        constructor_page.to_go_click_on_constructor()

        assert constructor_page.is_bulki_button_visible()

    @allure.title('Проверяем переход по кнопке "Лента Заказов"')
    def test_to_go_click_on_tape_orders(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_url(UrlPage.PAGE_URL)
        constructor_page.to_go_click_on_tape_orders()

        assert constructor_page.is_head_tape_order_visible()

    @allure.title('Проверяем, если кликнуть на ингредиент, откроется окно с деталями')
    def test_click_to_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_url(UrlPage.PAGE_URL)
        constructor_page.click_to_ingredient()

        assert constructor_page.is_head_details_ingredient_visible()

    @allure.title('Проверяем, что окно с деталями ингредиента, закрывается по нажатию на крестик')
    def test_close_windows_details_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_url(UrlPage.PAGE_URL)
        constructor_page.close_windows_details_ingredient()
        constructor_page.wait_element_invisibility_base(LocatorsConstructor.MODAL_WINDOWS)

        assert constructor_page.is_details_window_closed()

    @allure.title('Проверяем, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_in_order_count_rise(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_url(UrlPage.PAGE_URL)
        constructor_page.add_ingredient_in_order_count_rise()
        ingredient_count = constructor_page.get_ingredient_count()

        assert ingredient_count == 2, f'Ожидалось 2, но получено {ingredient_count}'

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_auth_user_can_place_order(self, driver):
        driver.get(UrlPage.PAGE_URL)
        constructor_page = ConstructorPage(driver)
        constructor_page.auth_user_can_place_order()

        assert constructor_page.is_id_order_visible()
