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


    def __init__(self, fetch_class=None):
        self.connection = sqlite3.connect("user/database.db")
        self.cursor = self.connection.cursor()

        self.set_fetch_mode(fetch_class)

    def _execute(self, statement, data=None):
        """
        Executes a given statement
        """
        if data is not None:
            self.cursor.execute(statement, data)
        else:
            self.cursor.execute(statement)
        self.connection.commit()
        self._close()

    def _fetchone(self, statement):
        """
        Fetches one result and return it as a class object
        """
        self.cursor.execute(statement)
        result = self.cursor.fetchone()
        self._close()

        # Assign values to the class object
        if result is not None:
            class_object = self.FETCH_CLASS()
            for i, attribute in enumerate(class_object.__dict__.keys()):
                class_object.__dict__[attribute] = result[i]
            return class_object

        return None

    def _fetchall(self, statement):
        """
        Fetches all results and return it as a list of class objects
        """
        self.cursor.execute(statement)
        results = self.cursor.fetchall()
        self._close()

        if results is not None:
            class_objects = []
            for result in results:
                class_object = self.FETCH_CLASS()
                for i, attribute in enumerate(class_object.__dict__.keys()):
                    class_object.__dict__[attribute] = result[i]
                class_objects.append(class_object)
            return class_objects

        return None

    def _close(self):
        self.cursor.close()
        self.connection.close()

    @classmethod
    def set_fetch_mode(cls, fetch_class: str):
        cls.FETCH_CLASS = fetch_class
