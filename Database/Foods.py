import time

from Database.MySQLConnection import MySQLConnection


class Foods(MySQLConnection):
    def get_food_by_id(self, id):
        time.sleep(2)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM foods WHERE id={id};")
        result = db_cursor.fetchone()
        db.close()
        return result

    def get_foods_count(self):
        time.sleep(2)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM foods")
        count = db_cursor.fetchone()[0]
        db.close()
        return count