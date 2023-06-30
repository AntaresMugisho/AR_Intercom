# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os
import time
import threading

from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QWidget, QSlider
from PyQt6.QtCore import QTimer, pyqtSlot as Slot

from ui.chat_window import Ui_ChatWindow
from styles import Clients, SendButton
from server import Server
from client import Client

import recorder
import player
from user import User
from message import Message
import utils
from netscanner import NetscanThread


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

        # SHOW USER'S LIST
        users = User.where("id", ">=", 1)
        self.ui.load_client(users)

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
        self.server.message_listener.messageReceived.connect(self.show_bubble)

        # SCAN NETWORK TO FIND CONNECTED DEVICES
        self.server_hosts = {}

        # Scan on startup
        t1 = threading.Thread(target=self.scan_network)
        t1.start()

        # Scan network every 5 minutes to refresh active servers
        self.net_scanner = QTimer()
        self.net_scanner.timeout.connect(self.scan_network)
        # self.net_scanner.start(25_000)

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
        """
        Close all connections, timers and exit the application
        """
        try:
            self.net_scanner.stop()
            # self.online_checker.stop()
            # Stop all clients instances
            self.server.stop()
        except Exception as e:
            print(f"Error while trying to close app: {e}")
        finally:
            self.close()

    @Slot()
    def show_conversations(self):
        """
        Shows conversation bubbles with a specified user
        """

        # GET CLICKED BUTTON
        clicked_button = self.sender()
        user_uuid = clicked_button.objectName()

        # GET USER FROM CLICKED BUTTON OBJECT NAME
        user = User.where("uuid", "=", user_uuid)[0]
        user_name = user.get_user_name()

        # SET NAME TO THE ACTIVE CLIENT LABEL
        self.ui.active_client.setText(user_name)
        self.ui.active_client.setObjectName(user_uuid)
        self.ui.active_client.show()
        self.ui.delete_button.show()

        # REMOVE ACTUAL VISIBLE CHAT BUBBLES
        try:
            for index in reversed(range(self.ui.layout_bubble.count())):
                if index == 0:  # The widget at index 0 is a layout spacer, we don't have to delete it
                    break
                self.ui.layout_bubble.itemAt(index).widget().deleteLater()
        except Exception as e:  # If chat field was not visible or is empty
            print(e)

        # SHOW OLDER MESSAGES WITH THE ACTIVE USER
        messages = user.messages()
        for message in messages:
            sender_id = message.get_sender_id()
            kind = message.get_kind()
            body = message.get_body()
            created_at = message.get_created_at()
            status = message.get_status()

            #  Knowing that the user with id == 1 is the owner,
            #  messages sent from user_id 1 will be shown in the right bubble
            if sender_id == 1:
                self.ui.create_right_bubble(kind, body, created_at, status)
            else:
                self.ui.create_left_bubble(kind, body, created_at)

        # CLEAR MESSAGE COUNTER AND SHOW ONLINE TOAST IF SELECTED USER IS ONLINE
        for frame in self.ui.left_scroll.findChildren(QFrame):
            # Reset Message counter
            if frame.objectName() == user_uuid + "_counter":
                frame.setText("0")
                frame.hide()

                # Reset to normal style sheet
                frame.parent().setStyleSheet(Clients.frame_normal)

    def check_online(self, server_host: str):
        """
        Checks online devices and show or hide green online indicator widget.
        """
        client = Client(server_host)
        client.connect_to_server()

        user = User.where("host_address", "=", server_host)
        if user:
            user_uuid = user[0].get_uuid()

            # Show green online toast if client is online
            for widget in self.ui.left_scroll.findChildren(QFrame):
                if widget.objectName() == f"{user_uuid}_toast":
                    if client.online:
                        widget.show()
                    else:
                        widget.hide()


    @Slot(int)
    def show_bubble(self, id: int):
        """
        Shows incoming message bubble and
        """
        message = Message.find(id)
        kind = message.get_kind()
        body = message.get_body()
        created_at = message.get_created_at()

        if self.ui.active_client.objectName():
            user = User.where("uuid", "=", self.ui.active_client.objectName())[0]
            if user.get_id() == message.get_sender_id():
                self.ui.create_left_bubble(kind, body, created_at)

            else:
                user = User.find(message.get_sender_id())
                self.update_unread_message_counter(user.get_uuid())
        else:
            user = User.find(message.get_sender_id())
            self.update_unread_message_counter(user.get_uuid())

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

            # Send message
            receiver = User.where("uuid", "=", self.ui.active_client.objectName())[0]
            client = Client(receiver.get_host_address())
            client.connect_to_server()
            client.send_message("text", text_message)

            # Show bubble
            self.ui.create_right_bubble("text", text_message, time.strftime("%Y-%m-%d %H:%M"), client.message_delivered)

            # Reset some ui states
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
    def send_media(self, kind: str, path_to_media: str):
        """
        Sends the media message and shows bubble
        """
        # self.client.send_message(kind, path_to_media)
        self.ui.create_right_bubble(kind, path_to_media)

    def update_unread_message_counter(self, uuid: str):
        """
        Increase the unread message counter badge on new message.
        """
        for widget in self.ui.left_scroll.findChildren(QFrame):
            if widget.objectName() == uuid + "_counter":
                unread_msg = int(widget.text())
                unread_msg += 1
                widget.setText(f"{unread_msg}")

                try:
                    widget.show()
                except Exception as e:
                    print(f"Error while trying to show counter widget {e}")

                parent = widget.parent()
                parent.setStyleSheet(Clients.frame_unread_msg)

    def scan_network(self):
        """
        Scan network to find connected devices and put them in server_host dictionary.
        """
        addresses = []
        threads = []

        my_ip = utils.get_private_ip()
        if my_ip.startswith("127.0"):
            print("Veuillez vous connecter à un réseau Wi-Fi !")
        else:
            my_ip_bytes = my_ip.split(".")
            net_id = ".".join(my_ip_bytes[:3])

            for host_id in range(0, 256):  # 0 is supposed to be Net address, 1 the Gateway and 255 the Broadcast address
                # if host_id != int(my_ip_bytes[3]):
                addresses.append(f"{net_id}.{str(host_id)}")

            scan_threads = [NetscanThread(address) for address in addresses]
            for thread in scan_threads:
                thread.start()
                threads.append(thread)

            for i, thread in enumerate(threads):
                thread.join()

            self.server_hosts = NetscanThread.hosts

            # Check online hosts after network scan
            online_checkers = []
            for server_host in self.server_hosts.keys():
                thread = threading.Thread(target=self.check_online, args=(server_host,))
                online_checkers.append(thread)

            for thread in online_checkers:
                thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = ChatWindow()
    sys.exit(app.exec())
