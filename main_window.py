# -*- This python file uses the following encoding : utf-8 -*-
import sys
import hashlib

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
from PySide6.QtCore import Qt, Slot

from ui.main_window import Ui_MainWindow
from styles import LineEdit
from user import User



class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # HIDE WARNINGS
        self.ui.name_warning.hide()
        self.ui.psw_warning.hide()

        # CHANGE ECHO MODE TO PREVIEW PASSWORD
        self.ui.toogle_button.enterEvent = lambda event: self.ui.log_password.setEchoMode(QLineEdit.EchoMode.Normal)
        self.ui.toogle_button.leaveEvent = lambda event: self.ui.log_password.setEchoMode(QLineEdit.EchoMode.Password)

        # GET USER INFORMATION FROM DATABASE
        user = User.find(1)
        self.user_name = user.get_user_name()
        self.password = user.get_password()

        # The inputted password
        self.ui_password = None

        # CONNECT UI BUTTONS TO SLOTS
        self.ui.connect_log.clicked.connect(self.auth)
        self.ui.connect_log.keyPressEvent = self.auth

        self.show()

    def check_username(self):
        """
        Check if the username is authentic
        """
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
        """
        CHeck if the password is authentic
        """
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
        """
        Verifies user credentials and allow access to the chat window if the user is authenticated
        """

        if event is not True or event.key() == Qt.Key.Key_Return:
            self.check_username()
            self.check_password()

        if (self.ui.log_username.text(), self.ui_password) != (self.user_name, self.password):
            # show chat window
            # self.ui.stackedWidget.setCurrentWidget()
            print("Authenticated")
            # Close login window
            # self.close()
            # run = ChatWindow()


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())