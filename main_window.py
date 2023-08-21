# -*- This python file uses the following encoding : utf-8 -*-
import sys
import os
import hashlib

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
from PySide6.QtCore import Qt, Slot

from ui.main_window import Ui_MainWindow
from login_window import LoginWindow
from chat_window import ChatWindow
from styles import LineEdit
from user import User


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect menu bar signals to their slots
        self.ui.actionAide.triggered.connect(self.help)
        self.ui.actionQuitter.triggered.connect(self.close_)

        # On startup, show login window
        self.login_window = LoginWindow()
        self.ui.stackedWidget.addWidget(self.login_window)
        self.ui.stackedWidget.setCurrentWidget(self.login_window)
        self.setWindowTitle(self.login_window.windowTitle())

        # Prepare chat window
        self.chat_window = ChatWindow()

        # Listen for authenticated signal emitted from login window on a success login
        self.login_window.authenticated.connect(self.show_chat_window)

        # Show Main window
        self.show()

    @Slot()
    def help(self):
        """
        Open the user manual pdf file
        """
        if sys.platform == "win32":
            os.startfile(f"{os.getcwd()}/resources/Help.pdf")
        else:
            os.system(f"open {os.getcwd()}/resources/Help.pdf")

    @Slot()
    def close_(self):
        """
        Close all connections, timers and exit the application
        """
        print("Exiting app")
        # try:
        #     self.net_scanner.stop()
        #     # Stop all clients instances
        #     self.server.stop()
        # except Exception as e:
        #     print(f"Error while trying to close app: {e}")
        # finally:
        #     pass
        #     # self.close()

    @Slot()
    def show_chat_window(self):
        self.ui.stackedWidget.addWidget(self.chat_window)
        self.ui.stackedWidget.setCurrentWidget(self.chat_window)
        self.setWindowTitle(self.chat_window.windowTitle())


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())