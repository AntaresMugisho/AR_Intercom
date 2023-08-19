# -*- This python file uses the following encoding : utf-8 -*-

import random
import sys
import sqlite3

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

from ui.splash import Ui_SplashScreen
from register_window import RegisterWindow
from login_window import LoginWindow
from chat_window import ChatWindow
from user import User
import utils

try:
    from ctypes import windll # Exists on windows only
    app_id = "com.artrevolutionlabel.software.arintercom.v2"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
except ImportError:
    pass

# GLOBALS
counter = 0


class SplashScreen(QWidget):
    """
    Shows splashscreen before launching app.
    """
    def __init__(self):
        QWidget.__init__(self)
        self.splash_screen = Ui_SplashScreen()
        self.splash_screen.setupUi(self)

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
        self.splash_screen.line.setGraphicsEffect(shadow)

        # PROGRESS START AT ZERO
        self.progress_value(0)

        # TIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)  # Run timer every 10 milliseconds

        # CHANGE LOADING LABEL TEXT
        QtCore.QTimer.singleShot(1400, lambda: self.splash_screen.loading.setText("Checking Network"))
        QtCore.QTimer.singleShot(2500, lambda: self.splash_screen.loading.setText("Starting Databases"))
        QtCore.QTimer.singleShot(3500, lambda: self.splash_screen.loading.setText("Starting Server"))
        QtCore.QTimer.singleShot(4050, lambda: self.splash_screen.loading.setText("Loading User Interface"))
        QtCore.QTimer.singleShot(4500, lambda: self.splash_screen.loading.setText("Launching..."))

        # CREATE MEDIA FOLDERS IF NOT EXISTS
        utils.create_media_folders()

        # SHOW SPLASH SCREEN
        self.show()

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
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET NEW STYLESHEET
        stylesheet = stylesheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET ON PROGRESS BAR
        self.splash_screen.circular_progress.setStyleSheet(stylesheet)

    def progress(self):
        """
        Controls the progress value and initialize main window after loading is done
        """
        global counter
        value = counter

        # SET VALUE TO PROGRESS BAR

        # Fix value error if > 1.000
        if value >= 100 : value = 1.000
        self.progress_value(value)

        # CLOSE SPLASHSCREEN AND OPEN APP
        if counter > 100:
            # Stop timer
            self.timer.stop()

            # CLOSE SPLASH SCREEN
            self.close()

            # SHOW REGISTER IN WINDOW OR LOGIN WINDOW
            if not User.find(1):
                RegisterWindow()
            else:
                # LoginWindow()
                win = ChatWindow()

        # INCREASE COUNTER
        counter += 0.8


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    run = SplashScreen()
    sys.exit(app.exec())
