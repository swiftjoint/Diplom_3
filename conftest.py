import pytest
from selenium import webdriver
import data


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        data.DRIVER_NAME = 'chrome'
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver_instance = webdriver.Chrome(options=options)
    else:
        data.DRIVER_NAME = 'firefox'
        options = webdriver.FirefoxOptions()
        driver_instance = webdriver.Firefox(options=options)
        driver_instance.set_window_size(1920, 1080)

    yield driver_instance

    driver_instance.quit()
