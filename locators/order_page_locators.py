from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_INPUT = By.XPATH, '//input[contains(@placeholder, "Имя")]'
    LAST_NAME_INPUT = By.XPATH, '//input[contains(@placeholder, "Фамилия")]'
    ADDRESS_INPUT = By.XPATH, '//input[contains(@placeholder, "Адрес")]'
    METRO_STATIONS_INPUT = By.XPATH, '//input[contains(@placeholder, "Станция")]'
    METRO_STATION_SUGGESTION = By.XPATH, '//div[@class="select-search__select"]'
    METRO_STATION = By.XPATH, '//div[contains(text(), "{}")]'
    PHONE_INPUT = By.XPATH, '//input[contains(@placeholder, "Телефон")]'
    NEXT_BUTTON = By.XPATH, '//button[contains(text(), "Далее")]'
    DATE_INPUT = By.XPATH, '//input[contains(@placeholder, "Когда")]'
    DATE_SELECTED = By.XPATH, '//div[contains(@class, "day--selected")]'
    RENTAL_DURATION = By.XPATH, '//div[contains(text(), "аренды")]'
    RENTAL_DURATION_OPTION = By.XPATH, '//div[contains(text(), "{}")]'
    COLOR_CHECKBOX = By.XPATH, '//label[contains(text(), "{}")]'
    COMMENT_INPUT = By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]'
    ORDER_BUTTON = By.XPATH, '//button[contains(text(), "Заказать") and contains(@class, "Button_Middle")]'
    ORDER_CONFIRMATION_BUTTON_YES = By.XPATH, '//button[contains(text(), "Да")]'
    SUCCESS_ORDER = By.XPATH, '//div[contains(text(), "Заказ оформлен")]'
