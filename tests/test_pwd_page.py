import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import ExpectedText
from data import UrlPage
from locators.locators_pwd_page import LocatorsPwd
from pages.pwd_page import PwdPage


class TestPwd:
    @allure.title('Проверяем переход с главной страницы на страницу восстановления пароля, '
                  'где ищем кнопку и забираем с неё текст "Восстановить"')
    def test_go_to_page_pwd_recovery(self, driver):
        driver.get(UrlPage.PAGE_URL)
        pwd_page = PwdPage(driver)
        pwd_page.go_to_page_pwd_recovery()
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(LocatorsPwd.BTN_RESET)
        )

        assert pwd_page.get_text_from_element(LocatorsPwd.BTN_RESET) == ExpectedText.TEXT_BTN_RECOVER

    @allure.title('Проверяем ввод почты и клик по кнопке "Восстановить", '
                  'при переходе ищем кнопку "Сохранить" и забираем с неё текст')
    def test_input_email_and_click_recover_btn(self, driver):
        driver.get(UrlPage.PAGE_URL)
        pwd_page = PwdPage(driver)
        pwd_page.go_to_page_pwd_recovery()
        pwd_page.input_email_and_click_recover_btn()
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(LocatorsPwd.BTN_SAVE_PWD)
        )

        assert pwd_page.get_text_from_element(LocatorsPwd.BTN_SAVE_PWD) == ExpectedText.TEXT_BTN_SAVE

    @allure.title('Проверяем, что при нажатии на кнопку паказать/скрыть пароль, '
                  'поле становится активным, подсвечивается')
    def test_toggle_pwd_visibility_and_actively_field(self, driver):
        driver.get(UrlPage.PAGE_URL)
        pwd_page = PwdPage(driver)
        pwd_page.go_to_page_pwd_recovery()
        pwd_page.input_email_and_click_recover_btn()
        pwd_page.toggle_pwd_visibility_and_actively_field()

        assert WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(LocatorsPwd.ACTIVELY_FIELD)
        ), 'Поле не подсветилось как активно'
