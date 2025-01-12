allure_report
Содержит файл index.html, который представляет собой отчет о тестах в виде веб-сайта.

allure_results
Содержит файлы JSON, созданные Allure при прогонке тестов.

locators
Содержит файлы с локаторами для различных страниц:

locators_constructor_page.py: Локаторы для страницы конструктора.
locators_home_page.py: Локаторы для главной страницы.
locators_lk_page.py: Локаторы для личного кабинета.
locators_order_page.py: Локаторы для страницы заказа.
locators_pwd_page.py: Локаторы для страницы восстановления пароля.

page
Содержит файлы с методами для взаимодействия с веб-страницами:

__init__.py: Инициализационный файл.

base_page.py: Базовый класс для всех страниц, содержащий общие методы для взаимодействия с элементами.

__init__(self, driver): Инициализация драйвера.
find_element_with_wait(self, locator): Находит элемент с ожиданием.
wait_element_invisibility(self, wait_locator): Ожидает невидимости элемента.
click_to_element(self, locator): Кликает по элементу.
get_text_from_element(self, locator): Получает текст из элемента.
add_text_to_element(self, locator, text): Добавляет текст в элемент.
move_the_element_chrome(self, locator_element, locator_target): Перемещает элемент в Chrome.
get_element(self, locator): Получает элемент.
drag_and_drop_element_firefox(self, locator_from, locator_to): Перетаскивает элемент в Firefox.
scroll_to_bottom(self, driver): Прокручивает страницу вниз.
get_counter_value(self, locator): Получает значение счетчика.

constructor_page.py: Методы для взаимодействия со страницей конструктора.

to_go_click_on_constructor(self): Кликает на кнопку "Конструктор".
to_go_click_on_tape_orders(self): Кликает на кнопку "Лента Заказов".
click_to_ingredient(self): Кликает на ингредиент "Флюоресцентная булка R2-D3".
close_windows_details_ingredient(self): Закрывает окно с деталями ингредиента.
add_ingredient_in_order_count_rise(self): Перетаскивает ингредиент в окно заказа.
auth_user_can_place_order(self): Авторизует пользователя и оформляет заказ.

lk_page.py: Методы для взаимодействия с личным кабинетом.

go_to_personal_cabinet(self): Переходит в личный кабинет.
go_to_history_page(self, driver): Переходит на страницу истории заказов.
logout_lk(self): Выходит из личного кабинета.

order_page.py: Методы для взаимодействия со страницей заказа.

click_to_order_open_win_with_details(self): Кликает на заказ в ленте заказов.
show_order_history_in_tape_orders(self, driver): Показывает историю заказов в ленте заказов.
new_create_order_total_count_rise(self): Создает новый заказ и увеличивает общий счетчик.
new_create_order_total_count_today_rise(self): Создает новый заказ и увеличивает счетчик за сегодня.
new_create_order_displayed_in_work(self): Создает новый заказ и отображает его в работе.

pwd_page.py: Методы для взаимодействия со страницей восстановления пароля.

go_to_page_pwd_recovery(self): Переходит на страницу восстановления пароля.
input_email_and_click_recover_btn(self): Вводит email и кликает на кнопку восстановления.
toggle_pwd_visibility_and_actively_field(self): Переключает видимость пароля.

tests
Содержит файлы с тестами:

__init__.py: Инициализационный файл.

test_constructor_page.py: Тесты для страницы конструктора.

test_to_go_click_on_constructor(self, driver): Проверяет переход по кнопке "Конструктор".
test_to_go_click_on_tape_orders(self, driver): Проверяет переход по кнопке "Лента Заказов".
test_click_to_ingredient(self, driver): Проверяет открытие окна с деталями ингредиента.
test_click_to_ingredient(self, driver): Проверяет закрытие окна с деталями ингредиента.
test_add_ingredient_in_order_count_rise(self, driver): Проверяет увеличение счетчика ингредиента при добавлении в заказ.
test_auth_user_can_place_order(self, driver): Проверяет возможность оформления заказа залогиненным пользователем.

test_lk_page.py: Тесты для личного кабинета.

test_go_to_page_pwd_recovery(self, driver): Проверяет переход в личный кабинет и получение текста с кнопки "Войти".
test_go_to_history_page(self, driver): Проверяет переход на страницу "История заказов".
test_logout_lk(self, driver): Проверяет выход из аккаунта.

test_order_page.py: Тесты для страницы заказа.

test_click_to_order_open_win_with_details(self, driver): Проверяет открытие окна с деталями заказа.
test_show_order_history_in_tape_orders(self, driver): Проверяет отображение заказов пользователя в ленте заказов.
test_new_create_order_total_count_rise(self, driver): Проверяет увеличение счетчика "Выполнено за всё время" при создании нового заказа.
test_new_create_order_total_count_today_rise(self, driver): Проверяет увеличение счетчика "Выполнено за сегодня" при создании нового заказа.
test_new_create_order_displayed_in_work(self, driver): Проверяет отображение номера заказа в ленте заказов "В работе".

test_pwd_page.py: Тесты для страницы восстановления пароля.

test_go_to_page_pwd_recovery(self, driver): Проверяет переход на страницу восстановления пароля и получение текста с кнопки "Восстановить".
test_input_email_and_click_recover_btn(self, driver): Проверяет ввод email и клик по кнопке "Восстановить".
test_toggle_pwd_visibility_and_actively_field(self, driver): Проверяет переключение видимости пароля и активность поля.

conftest.py
Содержит фикстуры для pytest:

driver(request): Фикстура для инициализации веб-драйвера (Chrome или Firefox) с заданными параметрами.

data.py
Содержит классы с данными и константами:

UrlPage: URL-адреса страниц.
PAGE_URL: Главная страница.
PAGE_URL_LOGIN: Страница входа.
PAGE_URL_TAPE_ORDER: Страница ленты заказов.
ExpectedText: Ожидаемые тексты для кнопок.
TEXT_BTN_RECOVER: Текст кнопки "Восстановить".
TEXT_BTN_SAVE: Текст кнопки "Сохранить".
TEXT_BTN_ENTER: Текст кнопки "Войти".
DataUser: Данные пользователя.
LOGIN: Логин пользователя.
PWD: Пароль пользователя.
DRIVER_NAME: Имя драйвера (Chrome или Firefox).

requirements.txt
Содержит список зависимостей проекта.
