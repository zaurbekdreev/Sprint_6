import allure
import pytest
from data.order_data import ORDER_DATA_1, ORDER_DATA_2
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize('order_data', (ORDER_DATA_1, ORDER_DATA_2))
    def test_place_order(self, order_data, open_firefox):
        order_page = OrderPage(open_firefox).open()
        order_page.accept_cookies()
        order_page.place_order(order_data)
        assert order_page.check_order()
