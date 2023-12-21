# -*- This python file uses the following encoding : utf-8 -*-

from database import Database
from datetime import datetime


class Model:
    """
    Database and Model controller !
    """
    db = None
    table_name = None
    statement = None

    def set_id(self, id: int):
        self.id = id

    def set_created_at(self):
        self.created_at = datetime.now()

    def set_updated_at(self):
        self.updated_at = datetime.now()

    def set_deleted_at(self):
        self.deleted_at = datetime.now()

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

    def get_deleted_at(self):
        return self.deleted_at

    @classmethod
    def setup_db(cls):
        """
        Define class variable values according to the Subclass
        """
        cls.db = Database(cls)
        cls.table_name = cls.__name__.lower() + "s"

    @classmethod
    def find(cls, id: int):
        """
        Returns a record find in the database with the specified id
        """
        cls.setup_db()
        statement = f"SELECT * FROM {cls.table_name} WHERE id = {id}"
        return cls.db._fetchone(statement)

    @classmethod
    def all(cls):
        """
        Returns all records
        """
        cls.setup_db()
        statement = f"SELECT * FROM {cls.table_name} WHERE deleted_at ISNULL"
        return cls.db._fetchall(statement)

    @classmethod
    def with_trashed(cls):
        """
        Returns all records even those who were soft deleted
        """
        cls.setup_db()
        statement = f"SELECT * FROM {cls.table_name}"
        return cls.db._fetchall(statement)

    @classmethod
    def trashed(cls):
        """
        Returns all deleted records
        """
        cls.setup_db()
        statement = f"SELECT * FROM {cls.table_name} WHERE deleted_at IS NOT NULL"
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
            # if value is not None:
            sql_fields.append(field)
            vars.append("?")
            values.append(value)

        statement = f"""
            INSERT INTO {self.__class__.table_name} ({sql_fields}) VALUES ({vars})  
        """

        statement = statement.replace("[", "").replace("]", "").replace("'", "")

        # Execute statement
        self.__class__.db._execute(statement, values)

        # Set object id according to the last inserted id
        self.set_id(self.__class__.db.cursor.lastrowid)
        self.update()  # This is only to update the user uuid

    @classmethod
    def where(cls, field: str, operator: str, value):
        """
        Return all records responding to the condition
        """
        cls.setup_db()
        cls.statement = f"SELECT * FROM {cls.table_name} WHERE {field} {operator} '{value}' AND deleted_at ISNULL"
        return cls

    @classmethod
    def order_by(cls, column: str, order: str = "ASC"):
        cls.statement += f" ORDER BY {column} {order}"
        return cls

    @classmethod
    def get(cls):
        return cls.db._fetchall(cls.statement)

    @classmethod
    def first_where(cls, field: str, operator: str, value):
        """
        Return the first record responding to the condition
        """
        cls.setup_db()
        statement = f"SELECT * FROM {cls.table_name} WHERE {field} {operator} '{value}' AND deleted_at ISNULL"
        return cls.db._fetchone(statement)

    def update(self):
        """
        Update data in database
        """
        self.__class__.setup_db()

        # Set updated datetime to now
        self.set_updated_at()

        # Build statement
        sql_fields = []
        values = []
        for field, value in self.__dict__.items():
            if field != "id":
                sql_fields.append(f"{field} = ?")
                values.append(value)

        statement = f"""
            UPDATE {self.__class__.table_name} SET {sql_fields} WHERE id = {self.get_id()} 
        """
        statement = statement.replace("[", "").replace("]", "").replace("'", "")

        # Execute statement
        self.__class__.db._execute(statement, values)

    def delete(self):
        """
        Permanently delete a record from database
        """
        self.__class__.setup_db()

        statement = f"""
            DELETE FROM {self.__class__.table_name} WHERE id = {self.get_id()}
        """

        self.__class__.db._execute(statement)

    def soft_delete(self):
        """
        Soft delete a record by setting a deleted_at time
        """
        self.set_deleted_at()
        self.update()

    def restore(self):
        """
        Restore soft deleted record by setting deleted_at time to None
        """
        self.deleted_at = None
        self.update()