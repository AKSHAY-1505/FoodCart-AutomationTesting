import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "user_email")
    PASSWORD = (By.ID, "user_password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log in']")

    def __init__(self, driver):
        super().__init__(driver)


    def login_with(self, email, password):
        self.send_to(self.EMAIL, email)
        self.send_to(self.PASSWORD, password)
        self.click_on(self.LOGIN_BUTTON)
