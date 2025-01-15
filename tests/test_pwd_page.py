import allure
from data import ExpectedText
from data import UrlPage
from pages.pwd_page import PwdPage


class TestPwd:
    @allure.title('Проверяем переход с главной страницы на страницу восстановления пароля, '
                  'где ищем кнопку и забираем с неё текст "Восстановить"')
    def test_go_to_page_pwd_recovery(self, driver):
        pwd_page = PwdPage(driver)
        pwd_page.go_to_url(UrlPage.PAGE_URL)
        pwd_page.go_to_page_pwd_recovery()

        assert pwd_page.is_text_recovery_visible() == ExpectedText.TEXT_BTN_RECOVER

    @allure.title('Проверяем ввод почты и клик по кнопке "Восстановить", '
                  'при переходе ищем кнопку "Сохранить" и забираем с неё текст')
    def test_input_email_and_click_recover_btn(self, driver):
        pwd_page = PwdPage(driver)
        pwd_page.go_to_url(UrlPage.PAGE_URL)
        pwd_page.go_to_page_pwd_recovery()
        pwd_page.input_email_and_click_recover_btn()

        assert pwd_page.is_text_save_visible() == ExpectedText.TEXT_BTN_SAVE

    @allure.title('Проверяем, что при нажатии на кнопку паказать/скрыть пароль, '
                  'поле становится активным, подсвечивается')
    def test_toggle_pwd_visibility_and_actively_field(self, driver):
        pwd_page = PwdPage(driver)
        pwd_page.go_to_url(UrlPage.PAGE_URL)
        pwd_page.go_to_page_pwd_recovery()
        pwd_page.input_email_and_click_recover_btn()
        pwd_page.toggle_pwd_visibility_and_actively_field()

        assert pwd_page.is_field_actively_visible()
