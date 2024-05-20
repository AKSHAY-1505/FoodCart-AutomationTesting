import time

from Database.MySQLConnection import MySQLConnection


class Orders(MySQLConnection):
    def status_of_last_created_order(self):
        time.sleep(1)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT status FROM orders ORDER BY created_at DESC LIMIT 1")
        status = db_cursor.fetchone()[0]
        time.sleep(1)
        db.close()
        return status

    def get_orders_count(self):
        time.sleep(1)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM orders")
        count = db_cursor.fetchone()[0]
        time.sleep(1)
        db.close()
        return count

    def get_order_items(self):
        time.sleep(1)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT f.name FROM order_items oi JOIN foods f ON oi.food_id = f.id ORDER BY oi.updated_at DESC LIMIT 2;")
        result = db_cursor.fetchall()
        time.sleep(1)
        db.close()
        return result