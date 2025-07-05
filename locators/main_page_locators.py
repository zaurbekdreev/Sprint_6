from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ = By.XPATH, '//div[contains(@class, "FAQ")]'
    QUESTION_COLLAPSED = By.XPATH, '//div[@id="accordion__heading-{}" and @aria-disabled="false" and @aria-expanded="false"]'
    QUESTION_EXPANDED = By.XPATH, '//div[@id="accordion__heading-{}" and @aria-disabled="true" and @aria-expanded="true"]'
    ANSWER_HIDDEN = By.XPATH, '//div[@id="accordion__panel-{}" and @hidden]/p'
    ANSWER_VISIBLE = By.XPATH, '//div[@id="accordion__panel-{}" and not(@hidden)]/p'
    SCOOTER_IMG = By.XPATH, '//img[@src="/assets/scooter.png"]'
    TOP_ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g"]'
    MIDDLE_ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
