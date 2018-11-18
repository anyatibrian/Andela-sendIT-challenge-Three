from Api.models.users import DBConnect
from datetime import datetime


class ParcelOrders:
    """class that handles the products"""

    def __init__(self):
        self.conn = DBConnect()

    def create_parcel_order(self, name, destination, description, pickup, user_id):
        """function that create products"""
        created_at = datetime.utcnow()
        status = 'pending'
        current_location = 'None'
        delivery_price = "000"
        sql = "INSERT INTO parcel_orders(name, destination, description," \
              " pickup, status, current_location, delivery_price, created_at" \
              ", user_id) VALUES('{}','{}', '{}','{}','{}','{}','{}','{}','{}'" \
              ")".format(name, destination, description, pickup, status,
                         current_location, delivery_price, created_at, user_id)
        self.conn.cursor.execute(sql)
        return 'order created successfully created'

    def parcel_exist(self, parcel_name):
        """function that checks the parcel order exists"""
        sql = "SELECT * FROM parcel_orders WHERE name='{}'".format(parcel_name)
        self.conn.cursor.execute(sql)
        parcels = self.conn.cursor.fetchone()
        return parcels
