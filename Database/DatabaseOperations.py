import time

from Database.MySQLConnection import MySQLConnection
from Database.Foods import Foods
from Database.Promotions import Promotions
from Database.Coupons import Coupons
from Database.Orderitems import OrderItems
from Database.Orders import Orders
from Database.DeliveryAgentAssignments import DeliveryAgentAssignments



class DatabaseOperations(MySQLConnection):
    foods = Foods()
    promotions = Promotions()
    coupons = Coupons()
    order_items = OrderItems()
    orders = Orders()
    agent_assignments = DeliveryAgentAssignments()

    def assert_foods_count(self, previous_count):
        new_count = self.foods.get_foods_count()
        assert new_count == previous_count + 4

    def assert_promotions_count(self, previous_count):
        new_count = self.promotions.get_promotions_count()
        time.sleep(1)
        assert new_count == previous_count + 2

    def assert_coupons_count(self, previous_count):
        time.sleep(2)
        new_count = self.coupons.get_coupons_count()
        assert new_count == previous_count + 2

    def assert_order_items_count(self, previous_count):
        new_count = self.order_items.get_order_items_count()
        assert new_count == previous_count + 2

    def assert_orders_count(self,previous_count):
        new_count = self.orders.get_orders_count()
        assert new_count == previous_count + 1

    def assert_agent_assignments_count(self,previous_count):
        new_count = self.agent_assignments.get_agent_assignments_count()
        assert new_count == previous_count + 1

    def assert_status_of_order(self,status):
        status_in_db = self.orders.status_of_last_created_order()
        assert status_in_db == status

    def assert_foods_in_order(self,food1, food2):
        food_items = self.orders.get_order_items()
        list = []
        for tup in food_items:
            list.append(tup[0])
        assert food1 in list
        assert food2 in list


