import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class CustomerHomePage(BasePage):
    SIGN_IN_BUTTON = (By.XPATH, "//a[contains(text(), 'Sign in')]")
    INCREMENT_BUTTON_TEMPLATE = "//div[@class='categories']//a[contains(text(), '{food_name}')]/ancestor::div[contains(@class, 'food_item')]//button[@class='btn btn-success increment']"
    ADD_TO_CART_BUTTON_TEMPLATE = "//div[@class='categories']//a[contains(text(), '{food_name}')]/ancestor::div[contains(@class, 'food_item')]//input[@value='Add to Cart']"
    CART_BUTTON = (By.ID, 'cart-button')

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_sign_in_button(self):
        self.click_on(self.SIGN_IN_BUTTON)

    def add_to_cart(self,food_name,quantity):
        for i in range(quantity):
            self.click_on_increment_button(food_name)
        self.click_on_add_to_cart_button(food_name)


    def click_on_increment_button(self,food_name):
        increment_button_xpath = self.INCREMENT_BUTTON_TEMPLATE.format(food_name=food_name)
        self.click_using_js((By.XPATH, increment_button_xpath)) #as the increment button is not visible without scrolling the page

    def click_on_add_to_cart_button(self,food_name):
        add_to_cart_button_xpath = self.ADD_TO_CART_BUTTON_TEMPLATE.format(food_name=food_name)
        self.click_using_js((By.XPATH,add_to_cart_button_xpath))

    def click_on_cart(self):
        self.click_on(self.CART_BUTTON)
