# -*- This python file uses the following encoding : utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_chat_window import Ui_ChatWindow


class ChatWindow(QMainWindow):
    """
    Initialize chat window as the main window
    """
    def __init__(self):
        QMainWindow.__init__(self)

        self.chat_window = Ui_ChatWindow()
        self.chat_window.setupUi(self)

        # SHOW WINDOW
        self.show()
        self.chat_window.online_toast_2.hide()


# RUN JUST FOR TEST
if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = ChatWindow()
    sys.exit(app.exec_())
