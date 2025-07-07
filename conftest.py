import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def open_firefox():
    with allure.step("Инициализация Firefox с размером окна 1280x720"):
        firefox_options = Options()
        firefox_options.add_argument("--window-size=1280,720")
        driver = webdriver.Firefox(options=firefox_options)
        yield driver
        driver.quit()
