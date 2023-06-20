# -*- This python file uses the following encoding : utf-8 -*-

import sqlite3


class Database:
    connection = sqlite3.connect("user/database.db")

    # def __init__(self):
    #     pass

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
        result = cursor.fetchone()
        cursor.close()

        return result


if __name__ == "__main__":
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

    db = Database()
    db.execute(create_users_table)
    db.execute(create_messages_table)
