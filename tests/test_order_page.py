import pytest
import allure
from selenium import webdriver
from data.order_data import ORDER_DATA_1, ORDER_DATA_2
from pages.order_page import OrderPage
from selenium.webdriver.firefox.options import Options


class TestOrderPage:

    @classmethod
    def setup_class(cls):
        with allure.step("Инициализация Firefox с размером окна 1280x720"):
            firefox_options = Options()
            firefox_options.add_argument("--window-size=1280,720")
            cls.driver = webdriver.Firefox(options=firefox_options)

    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize('order_data', (ORDER_DATA_1, ORDER_DATA_2))
    def test_place_order(self, order_data):
        order_page = OrderPage(self.driver).open()
        order_page.accept_cookies()
        order_page.place_order(order_data)
        assert order_page.check_order()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
