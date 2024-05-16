import time

from Database.MySQLConnection import MySQLConnection
from Database.Foods import Foods
from Database.Promotions import Promotions
from Database.Coupons import Coupons



class DatabaseOperations(MySQLConnection):
    foods = Foods()
    promotions = Promotions()
    coupons = Coupons()

    def assert_foods_count(self, previous_count):
        new_count = self.foods.get_foods_count()
        assert new_count == previous_count + 4

    def assert_promotions_count(self, previous_count):
        new_count = self.promotions.get_promotions_count()
        time.sleep(1)
        assert new_count == previous_count + 2

    def assert_coupons_count(self, previous_count):
        new_count = self.coupons.get_coupons_count()
        time.sleep(1)
        assert new_count == previous_count + 2

