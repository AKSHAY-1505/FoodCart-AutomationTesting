import time

import pytest
from Config.config import TestData
from Pages.CustomerHomePage import CustomerHomePage
from Pages.LoginPage import LoginPage
from Pages.AdminHomePage import AdminHomePage
from Pages.CouponManagementPage import CouponManagementPage
from Pages.FoodManagementPage import FoodManagementPage
from Pages.FoodPage import FoodPage
from Tests.test_base import BaseTest


class Test_AdminFlowScenario(BaseTest):

    def test_scenario(self):
        # Pages
        self.customer_home_page = CustomerHomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.admin_home_page = AdminHomePage(self.driver)
        self.food_management_page = FoodManagementPage(self.driver)
        self.food_page = FoodPage(self.driver)
        self.coupon_management_page = CouponManagementPage(self.driver)



        self.customer_home_page.click_on_sign_in_button()

        self.login_page.login_with(TestData.ADMIN_EMAIL, TestData.ADMIN_PASSWORD)

        self.admin_home_page.click_on_view_all_foods_button()

        for i in range(4):
            price = 100 * (i+1)
            self.food_management_page.create_new_food(f"Test Food {i}",'Demo Description 1', price,'/home/akshay/Desktop/Akshay/FoodCart-AutomationTesting/assets/burger1.jpg',10)

        self.food_management_page.click_on_food('Test Food 2')
        self.food_page.create_promotion('Test Promo 1', 'Promo Description', '15-05-2024', '20-05-2024', 10)

        self.driver.back()

        self.food_management_page.click_on_food('Test Food 3')
        self.food_page.create_promotion('Test Promo 2', 'Promo Description 2', '15-05-2024', '20-05-2024', 20)

        self.food_management_page.click_on_create_coupons_button()

        self.coupon_management_page.create_new_coupon('COUPON150', 300, 150, '01-05-2024', '31-05-2024')
        self.coupon_management_page.create_new_coupon('COUPON20', 200, 20, '01-06-2024', '30-06-2024')
        time.sleep(5)





