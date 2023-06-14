# -*- This python file uses the following encoding : utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.chat_window import Ui_ChatWindow


class ChatWindow(QMainWindow):
    """
    Initialize chat window as the main window
    """
    def __init__(self):
        super().__init__()

        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self)

        self.ui.online_toast_2.hide()

        # SHOW WINDOW
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = ChatWindow()
    sys.exit(app.exec_())
