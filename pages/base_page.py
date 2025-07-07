from functools import wraps
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url) -> bool:
        """
        :param url: ссылка на ресурс
        :return: статус полной загрузки страницы
        """
        self.driver.get(url)
        return self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    @staticmethod
    def format_locator(locator, data):
        method, string = locator
        string = string.format(data)
        return method, string

    @staticmethod
    def wait_for_element_to_be_visible(func):
        """
        Декоратор для явного ожидания отображения элемента перед выполнением функции.
        Этот декоратор использует WebDriverWait для ожидания видимости элемента,
        определённого локатором, перед вызовом декорируемой функции.
        """

        @wraps(func)
        def inner(self, locator):
            WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return func(self, locator)

        return inner

    @staticmethod
    def wait_for_element_to_be_clickable(func):
        """
        Декоратор для явного ожидания отображения элемента перед выполнением функции.
        Этот декоратор использует WebDriverWait для ожидания видимости элемента,
        определённого локатором, перед вызовом декорируемой функции.
        """

        @wraps(func)
        def inner(self, locator):
            self.wait.until(expected_conditions.element_to_be_clickable(locator))
            return func(self, locator)

        return inner

    @wait_for_element_to_be_visible
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @wait_for_element_to_be_clickable
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def input_text_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', behavior: 'smooth'});", element)

    def get_current_url(self):
        return self.driver.current_url.rstrip('/')

    def switch_to_last_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def accept_cookies(self, locator):
        has_cookies = self.find_elements(locator)
        if has_cookies:
            self.click(locator)
