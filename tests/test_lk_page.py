import allure
from data import UrlPage, ExpectedText
from pages.lk_page import LkPage


class TestLk:
    @allure.title('Проверяем переход с главной страницы в личный кабинет по кнопке "Личный Кабинет", '
                  'ищем кнопку "Войти" и забираем с неё текст')
    def test_go_to_page_pwd_recovery(self, driver):
        lk_page = LkPage(driver)
        lk_page.go_to_url(UrlPage.PAGE_URL)
        lk_page.go_to_personal_cabinet()

        assert lk_page.is_text_on_btn() == ExpectedText.TEXT_BTN_ENTER

    @allure.title('Проверяем переход из ЛК, на страницу "История заказов", ищем выполненые заказы')
    def test_go_to_history_page(self, driver):
        lk_page = LkPage(driver)
        lk_page.go_to_url(UrlPage.PAGE_URL)
        lk_page.go_to_history_page()

        assert lk_page.is_text_complete_visible()

    @allure.title('Проверяем выход из аккаунта')
    def test_logout_lk(self, driver):
        lk_page = LkPage(driver)
        lk_page.go_to_url(UrlPage.PAGE_URL)
        lk_page.logout_lk()

        assert lk_page.is_text_on_btn() == ExpectedText.TEXT_BTN_ENTER
