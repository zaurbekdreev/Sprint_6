import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data.service import qa_scooter_service
from pages.common_page import CommonPage


class TestRedirection:

    @classmethod
    def setup_class(cls):
        with allure.step("Инициализация Firefox с размером окна 1280x720"):
            firefox_options = Options()
            firefox_options.add_argument("--window-size=1280,720")
            cls.driver = webdriver.Firefox(options=firefox_options)

    @allure.title('Проверка перехода на главную при клике на лого самоката')
    def test_redirections_by_clicking_scooter_logo(self):
        page = CommonPage(self.driver).open(qa_scooter_service.order)
        page.accept_cookies()
        page.click_scooter_logo()
        assert page.check_click_scooter_logo_leads_to_scooter_main_page()

    @allure.title('Проверка перехода на главную страницу дзен при клике на лого яндекса')
    def test_redirection_by_clicking_yandex_logo(self):
        page = CommonPage(self.driver).open(qa_scooter_service.base_url)
        page.accept_cookies()
        page.click_yandex_logo()
        page.switch_to_last_tab()
        assert page.check_click_yandex_logo_leads_to_dzen_main_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
