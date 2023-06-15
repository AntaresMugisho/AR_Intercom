# -*- This python file uses the following encoding : utf-8 -*-

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit

from ui.loginwindow import Ui_LoginWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # HIDE WARNINGS
        self.ui.name_warning.hide()
        self.ui.psw_warning.hide()

        # CHANGE ECHO MODE TO PREVIEW PASSWORD
        self.ui.toogle_button.enterEvent = lambda event: self.ui.log_password.setEchoMode(QLineEdit.Normal)
        self.ui.toogle_button.leaveEvent = lambda event: self.ui.log_password.setEchoMode(QLineEdit.Password)

        # SHOW LOGIN WINDOW
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = LoginWindow()
    sys.exit(app.exec())
