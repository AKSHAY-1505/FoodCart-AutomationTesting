import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class FoodManagementPage(BasePage):
    # CREATE_CATEGORY_MODAL_TRIGGER_BUTTON = (By.ID, "category-create-trigger-button")
    CREATE_FOOD_MODAL_TRIGGER_BUTTON = (By.ID, "food-create-modal-trigger")
    FOOD_NAME_FIELD = (By.ID, "food_name")
    FOOD_DESCRIPTION_FIELD = (By.ID, "food_description")
    FOOD_PRICE_FIELD = (By.ID, "food_price")
    FOOD_CATEGORY_DROPDOWN = (By.ID, "food_category_id")
    FOOD_IMAGES_FIELD = (By.ID, "food_images")
    FOOD_QUANTITY_FIELD = (By.ID, "food_quantity")
    CREATE_FOOD_BUTTON = (By.XPATH, "//input[@value='Create Food']")
    CREATE_COUPONS_BUTTON = (By.XPATH, "//a[contains(text(), 'Create Coupons')]")

    def __init__(self, driver):
        super().__init__(driver)
    def create_new_food(self, name, description, price, image_path, quantity):
        self.click_on_create_food_modal_button()
        self.fill_food_name(name)
        self.fill_food_description(description)

        self.fill_food_price(price)

        self.fill_food_category()

        self.upload_image(image_path)

        self.fill_food_quantity(quantity)

        self.submit_form()
    def click_on_create_food_modal_button(self):
        self.click_on(self.CREATE_FOOD_MODAL_TRIGGER_BUTTON)

    def fill_food_name(self,name):
        self.send_to(self.FOOD_NAME_FIELD, name)

    def fill_food_description(self,description):
        self.send_to(self.FOOD_DESCRIPTION_FIELD, description)

    def fill_food_price(self,price):
        self.send_to(self.FOOD_PRICE_FIELD, price)

    def fill_food_category(self):
        food_category_drop_down = self.get_element(self.FOOD_CATEGORY_DROPDOWN)
        self.click_on(self.FOOD_CATEGORY_DROPDOWN)

        select = Select(food_category_drop_down)
        select.select_by_index(1)
        # select.select_by_visible_text("Option 1")

    def upload_image(self,path):
        self.send_to(self.FOOD_IMAGES_FIELD,path)

    def fill_food_quantity(self, quantity):
        self.send_to(self.FOOD_QUANTITY_FIELD, quantity)

    def submit_form(self):
        self.click_on(self.CREATE_FOOD_BUTTON)

    def click_on_food(self,food_name):
        xpath = f'//a[contains(text(), "{food_name}")]'
        self.click_on((By.XPATH, xpath))

    def click_on_create_coupons_button(self):
        self.click_on(self.CREATE_COUPONS_BUTTON)




