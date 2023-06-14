# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os

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

        # CONNECT MENU BAR SLOTS
        self.ui.actionAide.triggered.connect(lambda: self.help())
        self.ui.actionQuitter.triggered.connect(lambda: self._close())

        # SHOW WINDOW
        self.show()

    def help(self):
        """
        Open the user manual pdf file
        """
        if sys.platform == "win32":
            os.startfile(f"{os.getcwd()}/resources/Help.pdf")
        else:
            os.system(f"open {os.getcwd()}/resources/Help.pdf")

    def _close(self):
        try:
            self.client.disconnect()
            self.server.close_server()
            self.player.stop()

        except Exception as e:
            print("Error while closing", e)

        finally:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = ChatWindow()
    sys.exit(app.exec())
