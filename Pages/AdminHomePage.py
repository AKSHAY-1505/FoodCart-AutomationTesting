import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class AdminHomePage(BasePage):
    VIEW_ALL_FOODS_BUTTON = (By.XPATH, "//a[contains(text(), 'View All Foods')]")
    ASSIGN_AGENT_MODAL_TRIGGER_BUTTON = (By.XPATH, "//div[contains(@class, 'orders-body')]/div[1]//button[contains(text(), 'Assign Delivery Agent')]")
    SELECT_DELIVERY_AGENT_DROPDOWN = (By.XPATH, "//div[contains(@class, 'orders-body')]/div[1]//button[contains(text(), 'Assign Delivery Agent')]/following-sibling::div//select")
    ASSIGN_DELIVERY_AGENT_BUTTON = (By.XPATH, "//div[contains(@class, 'orders-body')]/div[1]//button[contains(text(), 'Assign Delivery Agent')]/following-sibling::div//select/following-sibling::div/input")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Log out']")
    VIEW_ALL_ORDERS_BUTTON = (By.XPATH, "//a[contains(text(), 'View All Orders')]")

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_view_all_foods_button(self):
        self.click_on(self.VIEW_ALL_FOODS_BUTTON)

    def click_on_view_all_orders_button(self):
        self.click_on(self.VIEW_ALL_ORDERS_BUTTON)
    def click_on_assign_agent_modal_button(self):
        self.click_on(self.ASSIGN_AGENT_MODAL_TRIGGER_BUTTON)

    def click_on_select_delivery_agent_dropdown(self):
        self.click_on(self.SELECT_DELIVERY_AGENT_DROPDOWN)

    def choose_first_delivery_agent(self):
        delivery_agent_dropdown = self.get_element(self.SELECT_DELIVERY_AGENT_DROPDOWN)
        self.click_on(self.SELECT_DELIVERY_AGENT_DROPDOWN)

        select = Select(delivery_agent_dropdown)
        select.select_by_index(0)

    def click_on_assign_delivery_agent_button(self):
        self.click_on(self.ASSIGN_DELIVERY_AGENT_BUTTON)

    def click_on_log_out_button(self):
        self.click_on(self.LOGOUT_BUTTON)

    def click_on_log_out_button_with_js(self):
        self.click_using_js(self.LOGOUT_BUTTON)


