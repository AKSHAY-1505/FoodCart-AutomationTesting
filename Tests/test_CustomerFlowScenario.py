import time

import pytest
from Config.config import TestData
from Pages.CustomerHomePage import CustomerHomePage
from Pages.LoginPage import LoginPage
from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage
from Database.Orderitems import OrderItems
from Database.Orders import Orders
from Database.DatabaseOperations import DatabaseOperations
from Tests.test_base import BaseTest


class Test_CustomerFlowScenario(BaseTest):

    def test_scenario(self):
        # Pages
        self.customer_home_page = CustomerHomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        self.order_items = OrderItems()
        self.db_operations = DatabaseOperations()
        self.orders = Orders()

        self.customer_home_page.click_on_sign_in_button()

        self.login_page.login_with(TestData.CUSTOMER_EMAIL, TestData.CUSTOMER_PASSWORD)

        previous_order_items_count = self.order_items.get_order_items_count()

        self.customer_home_page.add_to_cart('Test Food 2', 3)
        self.customer_home_page.add_to_cart('Test Food 3', 2)

        self.db_operations.assert_order_items_count(previous_order_items_count)


        self.customer_home_page.click_on_cart()

        self.cart_page.click_on_proceed_to_checkout_button()

        self.checkout_page.apply_coupon('COUPON20')
        time.sleep(1)
        self.checkout_page.assert_coupon_response('Invalid Coupon / Minimum Requirement Not Met')

        self.checkout_page.apply_coupon('COUPON150')
        time.sleep(1)
        self.checkout_page.assert_coupon_response('Coupon Applied Successfully')

        self.checkout_page.click_on_delivery_address()

        previous_orders_count = self.orders.get_orders_count()

        self.checkout_page.click_on_checkout_button()

        self.db_operations.assert_orders_count(previous_orders_count)

        self.db_operations.assert_foods_in_order('Test Food 3','Test Food 2')

        time.sleep(2)





