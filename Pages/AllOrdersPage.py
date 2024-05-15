import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class AllOrdersPage(BasePage):
    STATUS_CONTAINER = (By.XPATH, "(//div[contains(@class, 'order-entry')])[1]//div[contains(@class,'status')]/p")

    def __init__(self, driver):
        super().__init__(driver)

    def get_order_status_text(self):
        status = self.get_element(self.STATUS_CONTAINER)
        return status.text


    def assert_status(self,expected_status):
        actual_status = self.get_order_status_text()
        assert actual_status == expected_status
























