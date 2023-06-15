# -*- This python file uses the following encoding : utf-8 -*-

import sys
import threading
import sqlite3

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

from login_window import LoginWindow
from users import Users
from styles import LineEdit
from client import Client
from server import Server


class Login(LoginWindow):
    def __init__(self):
        super().__init__()

        self.server = None
        self.user_name = None
        self.user_code = None
        self.password = None

        # CHECK LOGIN CREDENTIALS ON LOGIN BUTTON CLICKED
        self.ui.connect_log.clicked.connect(self.check_data)
        self.ui.connect_log.keyPressEvent = self.check_data

        self.get_user_data()

    def get_user_data(self):
        try:
            connection = sqlite3.connect("ui.db")
            cursor = connection.cursor()

            i = str(1)
            cursor.execute("SELECT * FROM uidb WHERE id = ?", i)
            request = cursor.fetchone()

            cursor.close()
            connection.close()

            # CATCH INFORMATIONS
            self.user_name = request[1]
            self.user_code = request[2]
            self.password = request[3]

        except Exception as e:
            print(f"Error while connecting to DB: {e}")

        else:
            self.ui.welcome_log.setText(f"Salut {self.user_code} !")
            Users.ulist.remove(self.user_code)

    def check_username(self, *event):

        if not self.ui.log_username.text():
            self.ui.log_username.setStyleSheet(LineEdit.style_error)
            self.ui.name_warning.show()
            self.ui.name_warning.setText("Saisir votre nom d'utilisateur")

        elif self.ui.log_username.text() != self.user_name:
            self.ui.name_warning.show()
            self.ui.name_warning.setText("Nom d'utilisateur incorrect !")

        else:
            self.ui.name_warning.hide()
            self.ui.log_username.setStyleSheet(LineEdit.style_normal)

    def check_password(self, *event):
        if not self.ui.log_password.text():
            self.ui.log_password.setStyleSheet(LineEdit.style_error)
            self.ui.psw_warning.show()
            self.ui.psw_warning.setText("Saisir votre mot de passe")

        elif self.ui.log_password.text() != self.password:
            self.ui.psw_warning.show()
            self.ui.psw_warning.setText("Mot de passe incorrect !")

        else:
            self.ui.psw_warning.hide()
            self.ui.log_password.setStyleSheet(LineEdit.style_normal)

    def check_data(self, *event):
        if event is True:
            if event.key == Qt.Key_Return:
                self.check_username()
                self.check_password()
        else:
            self.check_username()
            self.check_password()

        if (self.ui.log_username.text(), self.ui.log_password.text()) == (self.user_name, self.password):
            self.login()

    def login(self):
        """
        Authenticated user, show chat window
        """
        # CREATE AND CONNECT SERVER

        # Set client prefix
        Client.prefix = self.user_code[0].upper()

        self.server = Server()

        self.server.set_usercode(self.user_code)
        self.server.set_port()
        self.server.create_socket_server()

        thread = threading.Thread(target=self.server.launch_server)
        thread.start()

        # CONNECT SERVER SIGNAL WHEN RECEIVING MESSAGE TO CREATE WIDGET
        # self.server.new_message.connect(lambda: self.receive("string"))
        # self.server.new_file.connect(lambda: self.receive("blob"))

        # SHOW CHAT WINDOW
        # self.show_chat_window()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Login()
    sys.exit(app.exec())
