import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class CheckoutPage(BasePage):
    COUPON_CODE_FIELD = (By.ID, 'coupon_code')
    APPLY_COUPON_BUTTON = (By.ID, 'apply-coupon-button')
    COUPON_RESPONSE = (By.ID, 'coupon-response')
    DELIVERY_ADDRESS_BUTTON = (By.XPATH, "(//input[@class='hidden-radio delivery-address'])[1]/following-sibling::label")
    CHECKOUT_BUTTON = (By.ID, 'checkout-button')

    def __init__(self, driver):
        super().__init__(driver)


    def apply_coupon(self,code):
        self.send_to(self.COUPON_CODE_FIELD, code)
        self.click_on(self.APPLY_COUPON_BUTTON)
        self.get_element(self.COUPON_CODE_FIELD).clear()

    def get_coupon_response_text(self):
        coupon_response_element = self.get_element(self.COUPON_RESPONSE)
        return coupon_response_element.text


    def assert_coupon_response(self, expected_text):
        actual_text = self.get_coupon_response_text()
        assert actual_text == expected_text

    def click_on_delivery_address(self):
        self.click_on(self.DELIVERY_ADDRESS_BUTTON)

    def click_on_checkout_button(self):
        self.click_on(self.CHECKOUT_BUTTON)




