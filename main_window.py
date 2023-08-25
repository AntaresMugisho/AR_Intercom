# -*- This python file uses the following encoding : utf-8 -*-
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
from PySide6.QtCore import Qt, Slot

from ui.main_window import Ui_MainWindow
from login_window import LoginWindow
from chat_window import ChatWindow


class MainWindow(QMainWindow):
    """
    Main window, multiscreen
    """
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect menu bar signals to their slots
        self.ui.actionAide.triggered.connect(self.help)
        self.ui.actionQuitter.triggered.connect(self.close_)

        # ADD WIDGETS
        # Login window
        self.login_window = LoginWindow()
        self.ui.stackedWidget.addWidget(self.login_window)

        # Chat window
        self.chat_window = ChatWindow()
        self.ui.stackedWidget.addWidget(self.chat_window)

        # On startup, show login window
        self.show_login_window()

        # After authentication, show chat window
        self.login_window.authenticated.connect(self.show_chat_window)

        # Show Main window
        # self.show()

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
        self.close()
        app = QApplication.instance()
        app.quit()


    @Slot()
    def show_login_window(self):
        self.ui.stackedWidget.setCurrentWidget(self.login_window)
        self.setWindowTitle(self.login_window.windowTitle())

    @Slot()
    def show_chat_window(self):
        self.ui.stackedWidget.setCurrentWidget(self.chat_window)
        self.setWindowTitle(self.chat_window.windowTitle())


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
