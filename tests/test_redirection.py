import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestRedirection:
    pages = (MainPage, OrderPage)

    @allure.title('Проверка перехода на главную при клике на лого самоката')
    @pytest.mark.parametrize('page', pages)
    def test_redirections_by_clicking_scooter_logo(self, page, open_firefox):
        page = page(open_firefox).open()
        page.accept_cookies()
        page.click_scooter_logo()
        assert page.check_click_scooter_logo_leads_to_scooter_main_page()

    @allure.title('Проверка перехода на главную страницу дзен при клике на лого яндекса')
    @pytest.mark.parametrize('page', pages)
    def test_redirection_by_clicking_yandex_logo(self, page, open_firefox):
        page = page(open_firefox).open()
        page.accept_cookies()
        page.click_yandex_logo()
        page.switch_to_last_tab()
        assert page.check_click_yandex_logo_leads_to_dzen_main_page()
