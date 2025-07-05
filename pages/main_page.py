import allure
from data.questions_and_answers import QUESTIONS, ANSWERS
from data.service import qa_scooter_service
from locators.main_page_locators import MainPageLocators
from pages.common_page import CommonPage


class MainPage(CommonPage):

    @allure.step('Открываем главную страницу')
    def open(self):
        self.get_url(qa_scooter_service.base_url)
        return self

    @allure.step('Прокручиваем страницу до блока с вопросами')
    def scroll_to_questions_list(self):
        self.scroll_to_element(MainPageLocators.FAQ)

    @allure.step('Раскрываем вопрос')
    def expand_question(self, n):
        formatter_locator = self.format_locator(MainPageLocators.QUESTION_COLLAPSED, n)
        self.click(formatter_locator)

    @allure.step('Получаем текст раскрытого вопроса')
    def get_text_of_question(self, n):
        formatter_locator = self.format_locator(MainPageLocators.QUESTION_EXPANDED, n)
        return self.get_text_from_element(formatter_locator)

    @allure.step('Получаем текст ответа')
    def get_text_of_answer(self, n):
        formatter_locator = self.format_locator(MainPageLocators.ANSWER_VISIBLE, n)
        return self.get_text_from_element(formatter_locator)

    @allure.step('Проверяем ответ')
    def check_question_and_answer(self, n):
        return QUESTIONS[n] == self.get_text_of_question(n) and ANSWERS[n] == self.get_text_of_answer(n)

    @allure.step('Прокручиваем страницу до кнопки "Заказать"')
    def scroll_to_middle_order_button(self):
        self.scroll_to_element(MainPageLocators.MIDDLE_ORDER_BUTTON)

    @allure.step('Нажимаем на верхнюю кнопку "Заказать"')
    def open_order_page_from_top_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажимаем на нижнюю кнопку "Заказать"')
    def open_order_page_from_middle_button(self):
        self.scroll_to_middle_order_button()
        self.click(MainPageLocators.MIDDLE_ORDER_BUTTON)

    @allure.step('Проверяем переход через нижнюю кнопку')
    def check_middle_order_button(self):
        self.open_order_page_from_middle_button()
        return self.get_current_url() == qa_scooter_service.order

    @allure.step('Проверяем переход на страницу заказов через верхнюю кнопку')
    def check_top_order_button(self):
        self.open_order_page_from_top_button()
        return self.get_current_url() == qa_scooter_service.order
