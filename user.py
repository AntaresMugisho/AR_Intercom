# -*- This python file uses the following encoding : utf-8 -*-

from database import Database

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


class UserController:

    def __init__(self):
        self.db = Database()


    def store(self, user: User):
        statement = f"""
        INSERT INTO users (
            host_address, host_name, user_name, user_status, password,
            image_path, department, role, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            # created_at
        ]



if __name__ == "__main__":
    user = User()
    user.set_user_status("We live we love we die !")

    controller = UserController()
    controller.store(user)
