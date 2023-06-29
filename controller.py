# -*- This python file uses the following encoding : utf-8 -*-
from database import Database


class Controller:

    @classmethod
    def find(cls, id):
        cls.db = Database(cls)
        table_name = f"{cls.__name__.lower()}s"

        statement = f"SELECT * FROM {table_name} WHERE id = {id}"
        return cls.db.fetchone(statement)

    @classmethod
    def where(cls, field: str, operator: str, value):
        cls.db = Database(cls)
        table_name = f"{cls.__name__.lower()}s"

        statement = f"SELECT * FROM {table_name} WHERE {field} {operator} '{value}'"
        return cls.db.fetchall(statement)

    @classmethod
    def store(cls, data: dict):
        cls.db = Database(cls)
        table_name = f"{cls.__name__.lower()}s"

        sql_fields = []
        vars = []
        values = []
        for field, value in data.items():
            sql_fields.append(field)
            vars.append("?")
            values.append(value)

        statement = f"""
        INSERT INTO {table_name} ({sql_fields}) VALUES {vars}  
        """

        print(statement)

        # cls.db.execute(statement, values)