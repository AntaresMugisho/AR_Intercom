# -*- This python file uses the following encoding : utf-8 -*-

import sys
import hashlib

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, pyqtSlot as Slot

from login_window import LoginWindow
from users import Users
from styles import LineEdit
from client import Client
from server import Server
from chat_functions import Chat

from user import User


class Login(LoginWindow):
    def __init__(self):
        super().__init__()

        # GET USER INFORMATION FROM DATABASE
        user = User.find(1)
        self.user_name = user.get_user_name()
        self.password = user.get_password()

        # The inputted password
        self.ui_password = None

        # CONNECT UI BUTTONS TO SLOTS
        self.ui.connect_log.clicked.connect(self.auth)
        self.ui.connect_log.keyPressEvent = self.auth

    def check_username(self):
        if not self.ui.log_username.text():
            self.ui.log_username.setStyleSheet(LineEdit.style_error)
            self.ui.name_warning.show()
            self.ui.name_warning.setText("Entrez votre nom d'utilisateur")

        elif self.ui.log_username.text() != self.user_name:
            self.ui.name_warning.show()
            self.ui.name_warning.setText("Nom d'utilisateur incorrect !")

        else:
            self.ui.name_warning.hide()
            self.ui.log_username.setStyleSheet(LineEdit.style_normal)

    def check_password(self):
        ui_password = self.ui.log_password.text()
        self.ui_password = hashlib.sha1(ui_password.encode()).hexdigest()

        if not self.ui.log_password.text():
            self.ui.log_password.setStyleSheet(LineEdit.style_error)
            self.ui.psw_warning.show()
            self.ui.psw_warning.setText("Entrez votre mot de passe")

        elif self.ui_password != self.password:
            self.ui.psw_warning.show()
            self.ui.psw_warning.setText("Mot de passe incorrect !")

        else:
            self.ui.psw_warning.hide()
            self.ui.log_password.setStyleSheet(LineEdit.style_normal)

    @Slot(bool)
    def auth(self, event):
        if event is False or event.key == Qt.Key.Key_Return:
            self.check_username()
            self.check_password()

        if (self.ui.log_username.text(), self.ui_password) == (self.user_name, self.password):
            chat_window = Chat()
            self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Login()
    sys.exit(app.exec())
