import allure
from data.other_urls import DZEN_URL
from data.service import qa_scooter_service
from locators.common_locators import CommonLocators
from pages.base_page import BasePage


class CommonPage(BasePage):

    @allure.step('Открываем страницу')
    def open(self, url):
        self.get_url(url)
        return self

    @allure.step('Принимаем куки, если имеются')
    def accept_cookies(self):
        has_cookies = self.find_elements(CommonLocators.COOKIE_BUTTON)
        if has_cookies:
            self.click(CommonLocators.COOKIE_BUTTON)

    @allure.step('Нажимаем на лого самоката')
    def click_scooter_logo(self):
        self.click(CommonLocators.LOGO_SCOOTER)

    @allure.step('Нажимаем на лого яндекса')
    def click_yandex_logo(self):
        self.click(CommonLocators.LOGO_YANDEX)

    @allure.step('Проверяем, что нажатие на лого самоката ведет на главную страницу "Самоката"')
    def check_click_scooter_logo_leads_to_scooter_main_page(self):
        return self.get_current_url() == qa_scooter_service.base_url

    @allure.step('Проверяем, что нажатие на лого яндекса ведет на главную страницу "Дзена"')
    def check_click_yandex_logo_leads_to_dzen_main_page(self):
        return DZEN_URL in self.get_current_url()
