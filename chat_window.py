# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QWidget, QSlider
from PyQt6.QtCore import pyqtSlot as Slot

from ui.chat_window import Ui_ChatWindow
from styles import Clients, SendButton
from server import Server
import recorder
import player
from user import UserController
import message


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

        # CONNECT SEND BUTTON
        self.ui.entry_field.textEdited.connect(self.change_send_style)
        self.ui.entry_field.returnPressed.connect(self.send_text_or_record)
        self.ui.send_button.clicked.connect(self.send_text_or_record)

        # START SERVER
        self.server = Server()
        self.server.start()

        # LISTEN FOR MESSAGE SIGNALS
        self.server.message.textMessageReceived.connect(self.show_bubble)

        # SHOW WINDOW
        self.show()

    @Slot(str, str)
    def show_bubble(self, kind, body):
        self.ui.create_left_bubble(kind, None, None, body, time.strftime("%Y-%m-%d %H:%M"))

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
        self.server.stop()
        self.close()

    @Slot()
    def show_conversations(self):
        """Try to connect to another client"""
        try:
            # GET CLICKED BUTTON
            clicked_button = self.sender()

            # GET NAME AND PORT OF CLICKED CLIENT NAME
            user_name = clicked_button.objectName()
            user_uuid = "aaab"  # clicked_button.objectName()

            # SET NAME TO THE ACTIVE CLIENT LABEL
            self.ui.active_client.setText(user_name)
            self.ui.active_client.show()
            self.ui.delete_button.show()

            # RESTORE EXISTING MESSAGES
            controller = UserController()
            user = UserController.find(1)
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

    @Slot()
    def change_send_style(self):
        """
        Changes send button style, and disable media button so that a user can not send media message and text message
        at a time.
        """
        if self.ui.entry_field.text():
            # Change send button style
            self.ui.send_button.setStyleSheet(SendButton.style_send)
            # Disable media button
            self.ui.media_button.setEnabled(False)

        else:
            self.ui.send_button.setStyleSheet(SendButton.style_record)
            self.ui.media_button.setEnabled(True)

    @Slot()
    def send_text_or_record(self):
        """
        According to the send button style, send text message or record a voice
        """
        if self.ui.send_button.styleSheet() == SendButton.style_send:
            text_message = self.ui.entry_field.text()
            # self.send_message(text_message)
            self.ui.create_right_bubble("text", None, None, text_message, time.strftime("%Y-%m-%d %H:%M"))
            self.ui.entry_field.setText(None)
            self.ui.send_button.setStyleSheet(SendButton.style_record)
            self.ui.media_button.setEnabled(True)

        elif self.ui.send_button.styleSheet() == SendButton.style_record:
            self.ui.media_button.setEnabled(False)
            # self.record_voice()
            # CONNECT RECORD BUTTONS
            self.ui.record_widget()
            self.ui.end_record.clicked.connect(recorder.start_recorder)
            self.ui.cancel_record.clicked.connect(recorder.stop_recorder)

    @Slot()
    def send_media(self, kind, path_to_media):
        #self.client.send_message(kind, path_to_media)

        # COLLECT MEDIA INFORMATIONS
        client_table = f"sa{self.ui.active_client.text()[:2].lower()}ch"
        send_time = time.strftime("%d-%m-%Y %H:%M")

        with open(path_to_media, "rb") as file:
            content = file.read()

        file_output_name, ext = path_to_media.split("/")[-1][:-4], path_to_media.split("/")[-1][-4:]

        try:
            self.create_right_bubble(kind, file_output_name, ext, content, send_time, sent)
            self.save_message(client_table, "S", kind, file_output_name, ext, content, send_time, sent)
        except Exception as e:
            print("552", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = ChatWindow()
    sys.exit(app.exec())
