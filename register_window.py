
import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from ui_register_window import Ui_SigninWindow
from styles import *

class RegisterWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.register_window = Ui_SigninWindow()
        self.register_window.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # SET UP SHADOW
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 50))

        # Apply shadow on register window
        self.setGraphicsEffect(self.shadow)

        # SET MOVE EVENT ON THE WINDOW
        # self.register_window.main_title.mouseMoveEvent = self.move_window

        # CONNECT CHOOSE PROFILE
        self.register_window.choose_profilepicture.setToolTip("Définir une photo de profil (PRO)")
        # self.register_window.choose_profilepicture.mousePressEvent = self.chooseProfile

        # CONNECT "NEXT" ADN "VALIDATE" BUTTON
        self.register_window.next.clicked.connect(self.check_data)
        self.register_window.validate.clicked.connect(self.confirm_subscription)

        # HIDE "BACK" BUTTON ON START
        self.register_window.return_button.clicked.connect(self.go_back)
        self.register_window.return_button.hide()

        # INDICATE CURRENT FEATURE INDEX (0)
        self.register_window.prev_feature.hide()
        self.register_window.feature_0.setStyleSheet(Features.style_active)

        # CONNECT FEATURE BUTTONS AND HIDE THEM
        self.register_window.next_feature.clicked.connect(partial(self.features, "Next"))
        self.register_window.prev_feature.clicked.connect(partial(self.features, "Previous"))

        # Connect small indicators
        self.register_window.feature_0.clicked.connect(partial(self.features, 0))
        self.register_window.feature_1.clicked.connect(partial(self.features, 1))
        self.register_window.feature_2.clicked.connect(partial(self.features, 2))
        self.register_window.feature_3.clicked.connect(partial(self.features, 3))
        self.register_window.feature_4.clicked.connect(partial(self.features, 4))
        self.register_window.feature_5.clicked.connect(partial(self.features, 5))

        # CONNECT "TERMINATE" BUTTON
        self.register_window.terminate.clicked.connect(self.terminate)

        # SHOW SIGNIN WINDOW
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = RegisterWindow()
    sys.exit(app.exec())
