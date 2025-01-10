import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import UrlPage, ExpectedText
from locators.locators_lk_page import LocatorsLK
from pages.lk_page import LkPage


class TestLk:
    @allure.title('Проверяем переход с главной страницы в личный кабинет по кнопке "Личный Кабинет", '
                  'ищем кнопку "Войти" и забираем с неё текст')
    def test_go_to_page_pwd_recovery(self, driver):
        driver.get(UrlPage.PAGE_URL)
        lk_page = LkPage(driver)
        lk_page.go_to_personal_cabinet()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsLK.BTN_LOGIN)
        )

        assert lk_page.get_text_from_element(LocatorsLK.BTN_LOGIN) == ExpectedText.TEXT_BTN_ENTER

    @allure.title('Проверяем переход из ЛК, на страницу "История заказов", ищем выполненые заказы')
    def test_go_to_history_page(self, driver):
        driver.get(UrlPage.PAGE_URL)
        lk_page = LkPage(driver)
        lk_page.go_to_history_page(driver)
        result = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsLK.ORDER_COMPLETE)
        )

        assert result.is_displayed()

    @allure.title('Проверяем выход из аккаунта')
    def test_logout_lk(self, driver):
        driver.get(UrlPage.PAGE_URL)
        lk_page = LkPage(driver)
        lk_page.logout_lk()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsLK.BTN_LOGIN)
        )

        assert lk_page.get_text_from_element(LocatorsLK.BTN_LOGIN) == ExpectedText.TEXT_BTN_ENTER
