# -*- This python file uses the following encoding : utf-8 -*-

import hashlib

from model import Model
from message import Message


class User(Model):
    """
    User model class representing a user as stored in database
    """
    def __init__(self):
        self.id = None
        self.uuid = None
        self.host_address = None
        self.host_name = None
        self.user_name = None
        self.email = None
        self.phone = None
        self.user_status = None
        self.password = None
        self.image_path = None
        self.department = None
        self.role = None
        self.created_at = None
        self.updated_at = None
        self.deleted_at = None

    # SETTERS
    def set_uuid(self, uuid=None):
        if uuid is None:
            uuid = hashlib.sha1(str(self.phone).encode()).hexdigest()
        self.uuid = uuid

    def set_host_address(self, host_address: str):
        self.host_address = host_address

    def set_host_name(self, host_name: str):
        self.host_name = host_name

    def set_user_name(self, user_name: str):
        self.user_name = user_name

    def set_email(self, email):
        self.email = email

    def set_phone(self, number):
        self.phone = number

    def set_user_status(self, user_status: str):
        self.user_status = user_status

    def set_password(self, password: str):
        self.password = hashlib.sha1(password.encode()).hexdigest()

    def set_image_path(self, path: str):
        self.image_path = path

    def set_department(self, department: str):
        self.department = department

    def set_role(self, role: str):
        self.role = role

    # GETTERS
    def get_id(self):
        return self.id

    def get_uuid(self):
        return self.uuid

    def get_host_address(self):
        return self.host_address

    def get_host_name(self):
        return self.host_name

    def get_user_name(self):
        return self.user_name

    def get_user_status(self):
        if self.user_status:
            return self.user_status
        return "Hello, i'm using AR Intercom !"

    def get_password(self):
        return self.password

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_image_path(self):
        return self.image_path

    def get_department(self):
        return self.department

    def get_role(self):
        return self.role

    # Relationships
    def messages(self):
        """
        Return all messages belonging to a distant user(client) with the actual user(server)
        """

        Message.setup_db()
        statement = f"""
            SELECT * FROM {Message.table_name} 
            WHERE (sender_id = {self.get_id()} OR receiver_id = {self.get_id()}) AND deleted_at ISNULL
        """
        return Message.db._fetchall(statement)


if __name__ == "__main__":
    user = User()
    user.set_user_name("Antares")

    user.save()