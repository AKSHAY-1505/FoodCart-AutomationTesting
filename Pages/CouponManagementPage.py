import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class CouponManagementPage(BasePage):
    CREATE_COUPON_MODAL_TRIGGER_BUTTON = (By.ID, "coupon-create-modal-trigger")
    COUPON_CODE_FIELD = (By.ID, "coupon_code")
    COUPON_MINIMUM_AMOUNT_FIELD = (By.ID, "coupon_min_amount")
    COUPON_DISCOUNT_FIELD = (By.ID, "coupon_discount")
    COUPON_FROM_DATE_FIELD = (By.ID, "coupon_from_date")
    COUPON_TO_DATE_FIELD = (By.ID, "coupon_to_date")
    CREATE_COUPON_BUTTON = (By.XPATH, "//input[@value='Create Coupon']")

    def __init__(self, driver):
        super().__init__(driver)
    def create_new_coupon(self, code, minimum_amount, discount, from_date, to_date):
        self.click_on_create_coupon_modal_button()
        self.fill_coupon_code(code)
        self.fill_minimum_amount(minimum_amount)
        self.fill_coupon_discount(discount)
        self.fill_coupon_from_date(from_date)
        self.fill_coupon_to_date(to_date)
        self.submit_form()

    def click_on_create_coupon_modal_button(self):
        self.click_on(self.CREATE_COUPON_MODAL_TRIGGER_BUTTON)

    def fill_coupon_code(self,code):
        self.send_to(self.COUPON_CODE_FIELD, code)

    def fill_minimum_amount(self,minimum_amount):
        self.send_to(self.COUPON_MINIMUM_AMOUNT_FIELD, minimum_amount)

    def fill_coupon_discount(self,discount):
        self.send_to(self.COUPON_DISCOUNT_FIELD, discount)

    def fill_coupon_from_date(self, date):
        self.send_to(self.COUPON_FROM_DATE_FIELD, date)

    def fill_coupon_to_date(self, date):
        self.send_to(self.COUPON_TO_DATE_FIELD, date)

    def submit_form(self):
        self.click_on(self.CREATE_COUPON_BUTTON)