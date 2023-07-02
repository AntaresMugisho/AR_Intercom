# -*- This python file uses the following encoding : utf-8 -*-

import sqlite3


class Database:
    __instance = None

    FETCH_CLASS = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, fetch_class):
        self.connection = sqlite3.connect("user/database.db")
        self.cursor = self.connection.cursor()

        self.set_fetch_mode(fetch_class)

    def execute(self, statement, data=None):
        """
        Executes a given statement
        """
        if data is not None:
            self.cursor.execute(statement, data)
        else:
            self.cursor.execute(statement)
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

        # print(self.cursor.lastrowid)

    def fetchone(self, statement):
        """
        Fetches one result and return it as a class object
        """
        self.cursor.execute(statement)
        result = self.cursor.fetchone()
        self.close()

        class_object = self.FETCH_CLASS()
        for i, attribute in enumerate(class_object.__dict__.keys()):
            class_object.__dict__[attribute] = result[i]

        return class_object

    def fetchall(self, statement):
        """
        Fetches all results and return it as a list of class objects
        """
        self.cursor.execute(statement)
        results = self.cursor.fetchall()
        self.close()

        class_objects = []
        for result in results:
            class_object = self.FETCH_CLASS()
            for i, attribute in enumerate(class_object.__dict__.keys()):
                class_object.__dict__[attribute] = result[i]
            class_objects.append(class_object)
        return class_objects

    def close(self):
        self.cursor.close()
        self.connection.close()

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
        body TEXT,
        received BOOLEAN,
        created_at DATETIME,
        updated_at DATETIME,
        deleted_at DATETIME
    )
    """

    # db.execute(create_users_table)
    # db.execute(create_messages_table)

    db = Database(User)
    user = db.fetchone("SELECT * FROM users WHERE id=1")
    print(user.get_user_name())

    db = Database(Message)
    messages = db.fetchall("SELECT * FROM messages")
    for message in messages:
        print(message.get_body())
