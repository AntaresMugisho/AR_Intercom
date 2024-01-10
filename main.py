# -*- This python file uses the following encoding : utf-8 -*-

import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, Slot

from gui import Ui_SplashScreen
from register_window import RegisterWindow
from login_window import LoginWindow
import utils

from model import User

# GLOBALS
counter = 0


class SplashScreen(QWidget):
    """
    Shows splashscreen before launching app
    """
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowTitle("AR Intercom")

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # SET UP SHADOW
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 200))

        # Apply shadow on splash screen
        self.ui.line.setGraphicsEffect(shadow)

        # PROGRESS START AT ZERO
        self.progress_value(0)

        # FIND THE FIRST USER
        self.user = User.query.first()

        # CREATE MEDIA FOLDERS IF NOT EXISTS
        utils.create_media_folders()

        # TIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)  # Run timer every 10 milliseconds

        # CHANGE LOADING LABEL TEXT
        QtCore.QTimer.singleShot(1000, lambda: self.ui.loading.setText("Checking Network"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.loading.setText("Analysing Databases"))
        QtCore.QTimer.singleShot(2500, lambda: self.ui.loading.setText("Starting Server"))
        QtCore.QTimer.singleShot(2800, lambda: self.ui.loading.setText("Loading User Interface"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.loading.setText("Launching..."))

        # SHOW SPLASH SCREEN
        self.show()

    @Slot()
    def progress(self):
        """
        Controls the progress value and initialize main window after loading is done
        """
        global counter
        value = counter

        # SET VALUE TO PROGRESS BAR

        # Fix value error if > 100
        if value >= 99: value = 100
        self.progress_value(value)

        # CLOSE SPLASHSCREEN AND OPEN APP
        if counter > 150:
            # Stop timer
            self.timer.stop()

            # CLOSE SPLASH SCREEN
            self.close()

            # SHOW REGISTER WINDOW OR LOGIN WINDOW

            if not self.user:
                print("No user")
                self.register_window = RegisterWindow()
            else:
                print(self.user)
                self.login_window = LoginWindow()
        # INCREASE COUNTER
        counter += 0.4

    def progress_value(self, value):
        """
        Update the stylesheet according to the progress value
        """
        stylesheet = """
          QFrame{
              border-radius:132px;
              background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1}
              rgba(250, 249, 251, 255), stop:{STOP_2} rgba(255, 0, 0, 255));}
          """

        # GET PROGRESS BAR VALUE AND CONVERT TO FLOAT
        progress = (100 - value) / 100.0

        # SET NEW VALUES
        stop_1 = str(progress - 0.0001)
        stop_2 = str(progress)

        # SET NEW STYLESHEET
        stylesheet = stylesheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET ON PROGRESS BAR
        self.ui.circular_progress.setStyleSheet(stylesheet)


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    run = SplashScreen()
    sys.exit(app.exec())
