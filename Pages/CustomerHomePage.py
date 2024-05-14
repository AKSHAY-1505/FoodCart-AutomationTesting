import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class CustomerHomePage(BasePage):
    SIGN_IN_BUTTON = (By.XPATH, "//a[contains(text(), 'Sign in')]")

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_sign_in_button(self):
        self.click_on(self.SIGN_IN_BUTTON)