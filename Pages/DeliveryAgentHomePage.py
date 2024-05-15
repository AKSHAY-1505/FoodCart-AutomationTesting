import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class DeliveryAgentHomePage(BasePage):
    MARK_AS_OUT_FOR_DELIVERY_BUTTON = (By.XPATH, "(//div[contains(@class, 'assigned-orders')])[1]//button[contains(text(), 'Mark as Out For Delivery')]")
    MARK_AS_DELIVERED_BUTTON = (By.XPATH, "(//div[contains(@class, 'assigned-orders')])[1]//button[contains(text(), 'Mark as Delivered')]")
    def __init__(self, driver):
        super().__init__(driver)


    def mark_as_out_for_delivery(self):
        self.click_on(self.MARK_AS_OUT_FOR_DELIVERY_BUTTON)
    def mark_as_delivered(self):
        self.click_on(self.MARK_AS_DELIVERED_BUTTON)



