import time

from Database.MySQLConnection import MySQLConnection


class Coupons(MySQLConnection):
    def get_coupon_by_coupon_code(self, code):
        time.sleep(2)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM promotions WHERE code={code};")
        result = db_cursor.fetchone()
        db.close()
        return result

    def get_coupons_count(self):
        time.sleep(2)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM coupons")
        count = db_cursor.fetchone()[0]
        db.close()
        return count