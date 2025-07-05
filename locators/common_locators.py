from selenium.webdriver.common.by import By


class CommonLocators:
    COOKIE_BUTTON = By.XPATH, '//button[@id="rcc-confirm-button"]'
    LOGO_SCOOTER = By.XPATH, '//img[@alt="Scooter"]'
    LOGO_YANDEX = By.XPATH, '//img[@alt="Yandex"]'
    SEARCH_DZEN_BUTTON = By.XPATH, '//button[text()="Найти" and @class="arrow__button"]'
