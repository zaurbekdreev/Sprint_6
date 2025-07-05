import allure
from data.service import qa_scooter_service
from locators.order_page_locators import OrderPageLocators
from pages.common_page import CommonPage


class OrderPage(CommonPage):

    @allure.step('Открываем главную страницу')
    def open(self):
        self.get_url(qa_scooter_service.order)
        return self

    @allure.step('Вводим имя')
    def input_first_name(self, first_name):
        self.input_text_to_element(OrderPageLocators.FIRST_NAME_INPUT, first_name)

    @allure.step('Вводим фамилию')
    def input_last_name(self, last_name):
        self.input_text_to_element(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step('Вводим адрес')
    def input_address(self, address):
        self.input_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self, metro_station):
        self.input_text_to_element(OrderPageLocators.METRO_STATIONS_INPUT, metro_station)
        self.click(OrderPageLocators.METRO_STATION_SUGGESTION)

    @allure.step('Переходим на следующую страницу заполнения формы заказа')
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Вводим номер телефона')
    def input_phone_number(self, number):
        self.input_text_to_element(OrderPageLocators.PHONE_INPUT, number)

    @allure.step('Выбираем дату доставка')
    def input_delivery_date(self, date):
        self.input_text_to_element(OrderPageLocators.DATE_INPUT, date)
        self.click(OrderPageLocators.DATE_SELECTED)

    @allure.step('Выбираем срок аренды')
    def select_rental_duration(self, duration):
        formatted_locator = self.format_locator(OrderPageLocators.RENTAL_DURATION_OPTION, duration)
        self.click(OrderPageLocators.RENTAL_DURATION)
        self.click(formatted_locator)

    @allure.step('Выбираем цвет')
    def select_color(self, color):
        formatted_locator = self.format_locator(OrderPageLocators.COLOR_CHECKBOX, color)
        self.click(formatted_locator)

    @allure.step('Вводим комментарий для курьера')
    def input_comment(self, comment):
        self.input_text_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Оформляем заказ')
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.ORDER_CONFIRMATION_BUTTON_YES)

    @allure.step('заполняем форму заказа')
    def place_order(self, order_data):
        self.input_first_name(order_data['first_name'])
        self.input_last_name(order_data['last_name'])
        self.input_address(order_data['address'])
        self.select_metro_station(order_data['metro_station'])
        self.input_phone_number(order_data['phone_number'])
        self.click_next_button()
        self.input_delivery_date(order_data['delivery_date'])
        self.select_rental_duration(order_data['duration'])
        self.select_color(order_data['color'])
        self.input_comment(order_data['comment'])
        self.click_order_button()

    @allure.step('Проверяем успешное создание заказа')
    def check_order(self):
        return self.find_element(OrderPageLocators.SUCCESS_ORDER)
