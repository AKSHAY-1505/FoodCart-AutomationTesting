import time

from Database.MySQLConnection import MySQLConnection


class DeliveryAgentAssignments(MySQLConnection):
    def get_order_item_by_id(self, id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM order_items WHERE id={id};")
        result = db_cursor.fetchone()
        db.close()
        time.sleep(1)
        return result

    def get_agent_assignments_count(self):
        time.sleep(1)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM order_delivery_agents")
        count = db_cursor.fetchone()[0]
        time.sleep(1)
        db.close()
        return count