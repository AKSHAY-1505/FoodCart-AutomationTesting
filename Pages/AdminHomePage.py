import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class AdminHomePage(BasePage):
    VIEW_ALL_FOODS_BUTTON = (By.XPATH, "//a[contains(text(), 'View All Foods')]")

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_view_all_foods_button(self):
        view_all_foods_button = self.get_element(self.VIEW_ALL_FOODS_BUTTON)
        self.click_on(view_all_foods_button)