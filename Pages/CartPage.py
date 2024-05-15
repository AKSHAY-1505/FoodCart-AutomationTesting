import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class CartPage(BasePage):
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Proceed To Checkout')]")

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_proceed_to_checkout_button(self):
        self.click_on(self.PROCEED_TO_CHECKOUT_BUTTON)




