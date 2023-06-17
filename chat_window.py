# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QWidget, QSlider
from PyQt6.QtCore import pyqtSlot as Slot
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
        self.ui.actionAide.triggered.connect(self.help)
        self.ui.actionQuitter.triggered.connect(self._close)

        # CONNECT USER'S CONVERSATION BUTTONS
        for frame in self.ui.left_scroll.findChildren(QFrame):
            user_conversation_button = frame.findChild(QPushButton)
            if user_conversation_button:
                user_conversation_button.clicked.connect(self.show_conversations)

        # SHOW WINDOW
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
    def _close(self):
        self.close()

    @Slot()
    def show_conversations(self):
        """Try to connect to another client"""
        try:
            # GET CLICKED BUTTON
            clicked_button = self.sender()

            # GET NAME AND PORT OF CLICKED CLIENT NAME
            user_name = clicked_button.text()

            # SET NAME TO THE ACTIVE CLIENT LABEL
            self.ui.active_client.setText(user_name)
            self.ui.active_client.show()
            self.ui.delete_button.show()

            # RESTORE EXISTING MESSAGES
            #self.restore_chat()

            # TRY TO CONNECT
            #self.client = Client(port)
            #self.client.connect_to_server()

            # CLEAR MESSAGE COUNTER AND SHOW ONLINE TOAST IF CLIENT ONLINE
            for frame in self.ui.left_scroll.findChildren(QFrame):
                # Reset Message counter
                if frame.objectName() == user_name + "_counter":
                    frame.setText("0")
                    frame.hide()

                    # Reset to normal style sheet
                    frame.parent().setStyleSheet(Clients.frame_normal)

            # Show online toast if client is online
            #self.check_online(name)

        except Exception as e:
            print("Error while asking connection : ", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = ChatWindow()
    sys.exit(app.exec())
