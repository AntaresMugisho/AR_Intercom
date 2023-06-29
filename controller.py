# -*- This python file uses the following encoding : utf-8 -*-
from database import Database


class Controller:
    """
    Database and Model controller !
    """
    db = None
    table_name = None

    @classmethod
    def setup_db(cls):
        cls.db = Database(cls)
        cls.table_name = cls.__name__.lower() + "s"

    @classmethod
    def all(cls):
        """
        Returns all records
        """
        cls.setup_db()
        statement = f"SELECT * FROM {cls.table_name}"
        return cls.db.fetchall(statement)

    @classmethod
    def find(cls, id):
        """
        Returns the record with the specified id
        """
        cls.setup_db()
        statement = f"SELECT * FROM {cls.table_name} WHERE id = {id}"
        return cls.db.fetchone(statement)

    @classmethod
    def where(cls, field: str, operator: str, value):
        """
        Return all records responding to the condition
        """
        cls.setup_db()
        statement = f"SELECT * FROM {cls.table_name} WHERE {field} {operator} '{value}'"
        return cls.db.fetchall(statement)

    @classmethod
    def store(cls, data: dict):
        """
        Insert data in database
        """
        cls.setup_db()

        sql_fields = []
        vars = []
        values = []
        for field, value in data.items():
            sql_fields.append(field)
            vars.append("?")
            values.append(value)

        statement = f"""
        INSERT INTO {cls.table_name} ({sql_fields}) VALUES {vars}  
        """

        print(statement)

        # cls.db.execute(statement, values)


if __name__ == "__main__":
    # controller = Controller()
    Controller.find(1)