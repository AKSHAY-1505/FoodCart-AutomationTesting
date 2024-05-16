import time

from Database.MySQLConnection import MySQLConnection


class Promotions(MySQLConnection):
    def get_promotion_by_id(self, id):
        time.sleep(2)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM promotions WHERE id={id};")
        result = db_cursor.fetchone()
        db.close()
        return result

    def get_promotions_count(self):
        time.sleep(2)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM promotions")
        count = db_cursor.fetchone()[0]
        db.close()
        return count