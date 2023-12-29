# -*- This python file uses the following encoding : utf-8 -*-

import sqlite3
import os
import utils


class Database:
    __instance = None

    MODEL = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance

        return cls.__instance


    def __init__(self, fetch_class=None):
        self.connection = sqlite3.connect(os.path.join(utils.get_storage_path(), "database.db"),
                                          detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cursor = self.connection.cursor()

        self.set_fetch_mode(fetch_class)

    def _execute(self, statement, data=None):
        """
        Executes a given statement
        """
        try:
            if data is not None:
                self.cursor.execute(statement, data)
            else:
                self.cursor.execute(statement)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"[-] SQL Error : {e}")
        finally:
            self._close()

    def _fetchone(self, statement):
        """
        Fetches one result and return it as a class object
        """
        __object = None

        try:
            self.cursor.execute(statement)
        except sqlite3.Error as e:
            print(f"[-] SQL Error : {e}")
        else:
            row = self.cursor.fetchone()

            # Assign values to the class object
            if row is not None:
                __object = self.MODEL()
                for i, attribute in enumerate(__object.__dict__.keys()):
                    __object.__dict__[attribute] = row[i]
        finally:
            self._close()

        return __object

    def _fetchall(self, statement):
        """
        Fetches all results and return it as a list of class objects
        """
        __objects = None

        try:
            self.cursor.execute(statement)
            results = self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"[-] SQL Error : {e}")
        else:
            if results is not None:
                __objects = []
                for result in results:
                    __object = self.MODEL()
                    for i, attribute in enumerate(__object.__dict__.keys()):
                        __object.__dict__[attribute] = result[i]
                    __objects.append(__object)
        finally:
            self._close()

        return __objects


    def _close(self):
        pass
        # self.cursor.close()
        # self.connection.close()

    @classmethod
    def set_fetch_mode(cls, fetch_class: str):
        cls.MODEL = fetch_class
