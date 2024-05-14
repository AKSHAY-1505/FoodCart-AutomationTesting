import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class FoodManagementPage(BasePage):
    CREATE_FOOD_BUTTON = (By.ID, "food-create-modal-trigger")
    FOOD_NAME_FIELD = (By.ID, "food_name")
    FOOD_DESCRIPTION_FIELD = (By.ID, "food_description")
    FOOD_PRICE_FIELD = (By.ID, "food_price")
    FOOD_CATEGORY_DROPDOWN = (By.ID, "food_category_id")
    FOOD_IMAGES_FIELD = (By.ID, "food_images")
    FOOD_QUANTITY_FIELD = (By.ID, "food_quantity")
    CREATE_FOOD_BUTTON = (By.XPATH, "//input[@value='Create Food']")

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_create_food_button(self):
        create_food_buttion = self.get_element(self.CREATE_FOOD_BUTTON)
        self.click_on(create_food_buttion)
        time.sleep(5)

    def fill_food_name(self,name):
        food_name_field = self.get_element(self.FOOD_NAME_FIELD)
        self.send_to(food_name_field,name)

    def fill_food_description(self,description):
        food_description_field = self.get_element(self.FOOD_DESCRIPTION_FIELD)
        self.send_to(food_description_field,description)

    def fill_food_price(self,price):
        food_price_field = self.get_element(self.FOOD_PRICE_FIELD)
        self.send_to(food_price_field,price)

    def fill_food_category(self):
        food_category_drop_down = self.get_element(self.FOOD_CATEGORY_DROPDOWN)
        self.click_on(food_category_drop_down)

        select = Select(food_category_drop_down)
        select.select_by_index(0)
        # select.select_by_visible_text("Option 1")

    def upload_image(self,path):
        # file_path = '/path/to/your/file.jpg'
        food_images_field = self.get_element(self.FOOD_IMAGES_FIELD)
        food_images_field.send_keys(path)

    def fill_food_quantity(self, quantity):
        food_quantity_field = self.get_element(self.FOOD_QUANTITY_FIELD)
        self.send_to(food_quantity_field, quantity)

    def submit_form(self):
        create_food_button = self.get_element(self.CREATE_FOOD_BUTTON)
        self.click_on(create_food_button)





