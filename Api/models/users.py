from Api.models.database import DBConnect
from datetime import datetime


class Users:
    def __init__(self):
        """class responsible for registering new users and login in existing users"""
        self.conn = DBConnect()

    def register_users(self, username, email, password):
        """function that registers users """
        created_at = datetime.utcnow()
        query = "INSERT INTO users(username, email, password, created_at)" \
                " VALUES('{}','{}','{}','{}')".format(username, email, password, created_at)
        self.conn.execute(query)
