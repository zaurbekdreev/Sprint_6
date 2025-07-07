import allure
import pytest
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка блока вопросов и ответов')
    @pytest.mark.parametrize('number', range(8))
    def test_questions_and_answers(self, number, open_firefox):
        main_page = MainPage(open_firefox).open()
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.expand_question(number)
        assert main_page.check_question_and_answer(number)

    @allure.title('Проверка открытия страницы заказа через нижнюю кнопку "Заказать"')
    def test_middle_order_button_lead_to_order_page(self, open_firefox):
        main_page = MainPage(open_firefox).open()
        main_page.accept_cookies()
        main_page.scroll_to_middle_order_button()
        assert main_page.check_middle_order_button()

    @allure.title('Проверка открытия страницы заказа через верхнюю кнопку "Заказать"')
    def test_top_order_button_lead_to_order_page(self, open_firefox):
        main_page = MainPage(open_firefox).open()
        main_page.accept_cookies()
        assert main_page.check_top_order_button()
