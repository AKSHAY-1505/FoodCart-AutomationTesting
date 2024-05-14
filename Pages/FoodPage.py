import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class FoodPage(BasePage):
    CREATE_PROMOTION_MODAL_TRIGGER = (By.ID, "create-promotion-modal-trigger")
    PROMOTION_TITLE_FIELD = (By.ID, "promotion_title")
    PROMOTION_DESCRIPTION_FIELD = (By.ID, "promotion_description")
    PROMOTION_FROM_DATE_FIELD = (By.ID, "promotion_from_date")
    PROMOTION_TO_DATE_FIELD = (By.ID, "promotion_to_date")
    PROMOTION_DISCOUNT_PERCENTAGE_FIELD = (By.ID, "promotion_discount_percentage")
    CREATE_PROMOTION_BUTTON = (By.XPATH, "//input[@value='Create Promotion']")

    def __init__(self, driver):
        super().__init__(driver)


    def create_promotion(self, title, description, from_date, to_date, discount_percentage):
        self.click_create_promotion()
        self.fill_promotion_title(title)
        self.fill_promotion_description(description)
        self.fill_promotion_from_date(from_date)
        self.fill_promotion_to_date(to_date)
        self.fill_promotion_discount_percentage(discount_percentage)
        self.submit_create_promotion_form()

    def click_create_promotion(self):
        self.click_on(self.CREATE_PROMOTION_MODAL_TRIGGER)

    def fill_promotion_title(self,title):
        self.send_to(self.PROMOTION_TITLE_FIELD, title)

    def fill_promotion_description(self, description):
        self.send_to(self.PROMOTION_DESCRIPTION_FIELD, description)

    def fill_promotion_from_date(self, date):
        self.send_to(self.PROMOTION_FROM_DATE_FIELD, date)

    def fill_promotion_to_date(self, date):
        self.send_to(self.PROMOTION_TO_DATE_FIELD, date)

    def fill_promotion_discount_percentage(self, discount_percentage):
        self.send_to(self.PROMOTION_DISCOUNT_PERCENTAGE_FIELD, discount_percentage)

    def submit_create_promotion_form(self):
        self.click_on(self.CREATE_PROMOTION_BUTTON)


