# -*- This python file uses the following encoding : utf-8 -*-

import sqlite3



class Database:
    __instance = None

    FETCH_CLASS = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("Connecting to database...")
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print("Database connection already established")
            return cls.__instance

    def __init__(self, fetch_class=None):
        print("[*] Successfully connected to database")
        self.connection = sqlite3.connect("user/database.db")

        self.set_fetch_mode(fetch_class)

    def execute(self, statement, data=None):
        cursor = self.connection.cursor()
        if data is not None:
            cursor.execute(statement, data)
        else:
            cursor.execute(statement)
        cursor.close()
        self.connection.commit()

    def fetch(self, statement):
        cursor = self.connection.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()
        cursor.close()

         = self.FETCH_CLASS
        for query in result:
            for i, attribute in enumerate(ob.__dict__.keys()):
                ob.__dict__[attribute] = query[i]

        return ob




    @classmethod
    def set_fetch_mode(cls, fetch_class: str):
        cls.FETCH_CLASS = fetch_class



if __name__ == "__main__":
    from user import User
    from message import Message

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid VARCHAR,
        host_address VARCHAR,
        host_name VARCHAR,
        user_name VARCHAR,
        user_status VARCHAR,
        password VARCHAR,
        image_path VARCHAR DEFAULT('user/default.png'),
        department VARCHAR,
        role VARCHAR,
        created_at DATETIME,
        updated_at DATETIME,
        deleted_at DATETIME
    )
    """
    create_messages_table = """
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_id INTEGER,
        receiver_id INTEGER,
        kind VARCHAR,
        body VARCHAR,
        created_at DATETIME,
        updated_at DATETIME,
        deleted_at DATETIME
    )
    """

    db = Database(Message())

    res = db.fetch("SELECT * FROM messages WHERE id=1")
    print(res.get_body())
    # db.execute(create_users_table)
    # db.execute(create_messages_table)
