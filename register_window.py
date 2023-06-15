# -*- This python file uses the following encoding : utf-8 -*-

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

from ui.register_window import Ui_SigninWindow


class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_SigninWindow()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # SET UP SHADOW
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 50))

        # Apply shadow on register window
        self.setGraphicsEffect(self.shadow)

        self.ui.choose_profilepicture.setToolTip("Choose profile picture (PRO)")

        # SHOW REGISTER WINDOW
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = RegisterWindow()
    sys.exit(app.exec())
