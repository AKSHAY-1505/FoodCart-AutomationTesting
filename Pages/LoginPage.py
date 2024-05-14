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
        email_field = self.get_element(self.EMAIL)
        password_field = self.get_element(self.PASSWORD)
        login_button = self.get_element(self.LOGIN_BUTTON)

        self.send_to(email_field, email)
        self.send_to(password_field, password)
        self.click_on(login_button)
        time.sleep(5)