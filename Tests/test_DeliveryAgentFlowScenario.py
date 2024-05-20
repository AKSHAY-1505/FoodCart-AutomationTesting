import time

import pytest
from Config.config import TestData
from Pages.CustomerHomePage import CustomerHomePage
from Pages.LoginPage import LoginPage
from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage
from Pages.AdminHomePage import AdminHomePage
from Pages.DeliveryAgentHomePage import DeliveryAgentHomePage
from Pages.AllOrdersPage import AllOrdersPage
from Database.DatabaseOperations import DatabaseOperations
from Database.DeliveryAgentAssignments import DeliveryAgentAssignments
from Database.Orders import Orders
from Tests.test_base import BaseTest


class Test_DeliveryAgentFlowScenario(BaseTest):

    def test_scenario(self):
        # Pages
        self.customer_home_page = CustomerHomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.admin_page = AdminHomePage(self.driver)
        self.delivery_agent_page = DeliveryAgentHomePage(self.driver)
        self.all_orders_page = AllOrdersPage(self.driver)

        self.db_operations = DatabaseOperations()
        self.agent_assignments = DeliveryAgentAssignments()
        self.orders = Orders()


        self.customer_home_page.click_on_sign_in_button()

        self.login_page.login_with(TestData.ADMIN_EMAIL, TestData.ADMIN_PASSWORD)

        self.admin_page.click_on_assign_agent_modal_button()

        self.admin_page.click_on_select_delivery_agent_dropdown()

        self.admin_page.choose_first_delivery_agent()

        self.previous_assignments_count = self.agent_assignments.get_agent_assignments_count()

        self.admin_page.click_on_assign_delivery_agent_button()

        self.db_operations.assert_agent_assignments_count(self.previous_assignments_count)

        self.admin_page.click_on_log_out_button()

        self.customer_home_page.click_on_sign_in_button()

        self.login_page.login_with(TestData.DELIVERY_AGENT_EMAIL, TestData.DELIVERY_AGENT_PASSWORD)

        self.delivery_agent_page.mark_as_out_for_delivery()

        self.delivery_agent_page.mark_as_delivered()

        self.admin_page.click_on_log_out_button_with_js()

        self.customer_home_page.click_on_sign_in_button()

        self.login_page.login_with(TestData.ADMIN_EMAIL, TestData.ADMIN_PASSWORD)

        self.admin_page.click_on_view_all_orders_button()

        self.all_orders_page.assert_status('Delivered')

        self.db_operations.assert_status_of_order(3)

        time.sleep(3)





