# -*- This python file uses the following encoding : utf-8 -*-
import hashlib
import platform
from datetime import datetime
import os

from database import Database

import utils


class User:
    def __init__(self):
        self.uuid = None
        self.host_address = None
        self.host_name = None
        self.user_name = None
        self.user_status = None
        self.password = None
        self.image_path = "user/default.png"
        self.department = None
        self.role = None
        self.created_at = None
        self.updated_at = None
        self.deleted_at = None

    # SETTERS
    def set_uuid(self, uuid):
        self.uuid = uuid

    def set_host_address(self, host_address):
        self.host_address = host_address

    def set_host_name(self, host_name):
        self.host_name = host_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_user_status(self, user_status):
        self.user_status = user_status

    def set_password(self, password):
        self.password = password

    def set_image_path(self, path):
        self.image_path = path

    def set_department(self, department):
        self.department = department

    def set_role(self, role):
        self.role = role

    def set_created_at(self):
        self.created_at = datetime.now()

    def set_updated_at(self):
        self.updated_at = datetime.now()

    def set_deleted_at(self):
        self.deleted_at = datetime.now()

    # GETTERS
    def get_uuid(self):
        return self.uuid

    def get_host_address(self):
        return self.host_address

    def get_host_name(self):
        return self.host_name

    def get_user_name(self):
        return self.user_name

    def get_user_status(self):
        return self.user_status

    def get_password(self):
        return self.password

    def get_image_path(self):
        return self.image_path

    def get_department(self):
        return self.department

    def get_role(self):
        return self.role

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

    def get_deleted_at(self):
        return self.deleted_at


class UserController:

    def __init__(self):
        self.db = Database()

    def find(self, id):
        statement = f"SELECT * FROM users WHERE id = {id}"
        result = self.db.fetch(statement)[0]
        return result

    def store(self, user: User):
        statement = """
        INSERT INTO users (
            host_address, host_name, user_name, user_status, password,
            image_path, department, role, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        data = [
            user.get_host_address(),
            user.get_host_name(),
            user.get_user_name(),
            user.get_user_status(),
            user.get_password(),
            user.get_image_path(),
            user.get_department(),
            user.get_role(),
            user.get_created_at(),
            user.get_updated_at()
        ]

        self.db.execute(statement, data)


if __name__ == "__main__":
    # user = User()
    # user.set_host_address(utils.get_private_ip())
    # user.set_host_name(platform.node())
    # user.set_user_name(os.environ["USER"].capitalize())
    # user.set_user_status("We live we love we die !")
    # user.set_password(hashlib.sha1(b"1234").hexdigest())
    # user.set_department("AR Software")
    # user.set_role("Security Analyst")
    # user.set_created_at()
    # user.set_updated_at()

    controller = UserController()
    # controller.store(user)

    user = controller.find(2)
    # print(user)