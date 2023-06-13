# -*- This python file uses the following encoding : utf-8 -*-

import sys
import sqlite3

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from splash import Ui_SplashScreen

from functionsSL import SignIn
from functions import ChatWin


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
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # SET UP SHADOW
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 200))

        # Apply shadow on splash screen
        self.splash_screen.line.setGraphicsEffect(shadow)

        # PROGRESS START AT ZERO
        self.progressValue(0)

        # TIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)  # Run timer every 10 milliseconds

        # CHANGE LOADING LABEL TEXT
        QtCore.QTimer.singleShot(1400, lambda: self.splash_screen.loading.setText("Checking Network"))
        QtCore.QTimer.singleShot(2500, lambda: self.splash_screen.loading.setText("Locating Database"))
        QtCore.QTimer.singleShot(3500, lambda: self.splash_screen.loading.setText("Preparing Server"))
        QtCore.QTimer.singleShot(4050, lambda: self.splash_screen.loading.setText("Loading User Interface"))
        QtCore.QTimer.singleShot(4500, lambda: self.splash_screen.loading.setText("Launching"))

        self.show()

    def progressValue(self, value):
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
        global counter
        value = counter

        # SET VALUE TO PROGRESS BAR

        # Fix value error if > 1.000
        if value >= 100 : value = 1.000
        self.progressValue(value)

        # CLOSE SPLASHSCREEN AND OPEN APP
        if counter > 100:
            # Stop timer
            self.timer.stop()

            # CLOSE SPLASH SCREEN
            self.close()

            # SHOW SIGN IN WINDOW OR LOGIN WINDOW
            self.connect_database()

        # INCREASE COUNTER
        counter += 0.2

    def connect_database(self):
        """
        Check if the user exists in database (has already created an account),
        if not, show registration form, else show login form.
        """
        # CONNECT TO DATA BASE
        try:
            connection = sqlite3.connect("ui.db")
            cursor = connection.cursor()

            i = str(1)
            cursor.execute("SELECT * FROM uidb WHERE id = ?", i)

            cursor.close()
            connection.close()

        except :
            self.main = SignIn()

        else:
            self.main = ChatWin()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    run = SplashScreen()
    sys.exit(app.exec())
