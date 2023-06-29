# -*- This python file uses the following encoding : utf-8 -*-
from database import Database


class Controller:
    """
    Database and Model controller !
    """
    db = None
    table_name = None

    def set_id(self, id: int):
        self.id = id

    def set_created_at(self):
        pass

    def set_updated_at(self):
        pass

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
    def find(cls, id: int):
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

    def save(self):
        """
        Insert data in database
        """
        self.__class__.setup_db()

        # Set created and updated datetime to now
        self.set_created_at()
        self.set_updated_at()

        sql_fields = []
        vars = []
        values = []
        for field, value in self.__dict__.items():
            sql_fields.append(field)
            vars.append("?")
            values.append(value)

        statement = f"""
            INSERT INTO {self.__class__.table_name} ({sql_fields}) VALUES {vars}  
        """

        statement = statement.replace("[", "").replace("]", "").replace("'", "")

        # Execute statement
        self.__class__.db.execute(statement, values)

        # Set object id according to the last inserted id
        self.set_id(self.__class__.db.cursor.lastrowid)

    def update(self):
        """
        Update data in database
        """
        self.__class__.setup_db()

        # Set updated datetime to now
        self.set_updated_at()

        # Build statement
        fields_values = []
        for field, value in self.__dict__.items():
            if value is not None:
                fields_values.append(f"{field} = \"{value}\"")

        statement = f"""
            UPDATE {self.__class__.table_name} SET {fields_values} WHERE {fields_values[0]} 
        """
        statement = statement.replace("[", "").replace("]", "").replace("'", "")

        # Execute statement
        self.__class__.db.execute(statement)
