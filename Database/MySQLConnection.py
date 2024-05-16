import mysql.connector

class MySQLConnection:
    def __init__(self):
        pass

    def connect_to_db(self):
        food_cart_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aaab8132",
            database='food_cart_development'
        )

        return food_cart_db