import allure
import pytest
from selenium import webdriver
from pages.main_page import MainPage
from selenium.webdriver.firefox.options import Options


class TestMainPage:

    @classmethod
    def setup_class(cls):
        with allure.step("Инициализация Firefox с размером окна 1280x720"):
            firefox_options = Options()
            firefox_options.add_argument("--window-size=1280,720")
            cls.driver = webdriver.Firefox(options=firefox_options)

    @allure.title('Проверка блока вопросов и ответов')
    @pytest.mark.parametrize('number', range(8))
    def test_questions_and_answers(self, number):
        main_page = MainPage(self.driver).open()
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.expand_question(number)
        assert main_page.check_question_and_answer(number)

    @allure.title('Проверка открытия страницы заказа через нижнюю кнопку "Заказать"')
    def test_middle_order_button_lead_to_order_page(self):
        main_page = MainPage(self.driver).open()
        main_page.accept_cookies()
        main_page.scroll_to_middle_order_button()
        assert main_page.check_middle_order_button()

    @allure.title('Проверка открытия страницы заказа через верхнюю кнопку "Заказать"')
    def test_top_order_button_lead_to_order_page(self):
        main_page = MainPage(self.driver).open()
        main_page.accept_cookies()
        assert main_page.check_top_order_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
