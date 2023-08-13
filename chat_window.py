# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os
import time
import threading

import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QWidget, QSlider, QMessageBox
from PySide6.QtCore import QTimer, Slot
from PySide6.QtMultimedia import QMediaRecorder, QMediaPlayer

from ui.chat_window import Ui_ChatWindow
from styles import Clients, SendButton
from server import Server
from client import Client


from user import User
from message import Message
from netscanner import NetscanThread

from recorder import Recorder
import utils


# Global variables for recorder time counter
seconds = minutes = 0

class ChatWindow(QMainWindow):
    """
    Initialize chat window to show conversations and start chatting
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
        # self.server.start()

        # LISTEN FOR MESSAGE SIGNALS
        # self.server.message_listener.messageReceived.connect(self.show_incoming_message)

        # SCAN NETWORK TO FIND CONNECTED DEVICES
        self.server_hosts = {}

        # Scan on startup
        #t1 = threading.Thread(target=self.scan_network)
        #t1.start()

        # Scan network every 5 minutes to refresh active servers
        #self.net_scanner = QTimer()
        #self.net_scanner.timeout.connect(self.scan_network)
        # self.net_scanner.start(300_000)
        #self.net_scanner.start(10_000)

        # CREATE RECORDER INSTANCE AND ASSOCIATED TIME COUNTER
        self.recorder = Recorder()
        self.record_timer = QTimer()
        self.record_timer.timeout.connect(self.time_counter)

        self.recorder.recorderStateChanged.connect(self.recorder_state_changed)
        self.recorder.recordConfirmed.connect(self.send_media)

        # SHOW CHAT WINDOW
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

        # GET USER FROM CLICKED BUTTON'S OBJECT NAME
        user = User.where("uuid", "=", user_uuid)[0]
        user_name = user.get_user_name()

        # SET NAME TO THE ACTIVE CLIENT LABEL
        self.ui.active_client.setText(user_name)
        self.ui.active_client.setObjectName(user_uuid)
        self.ui.active_client.show()
        self.ui.delete_button.show()

        # REMOVE ACTUAL VISIBLE CHAT BUBBLES
        try:
            for index in reversed(range(1, self.ui.layout_bubble.count())):
                self.ui.layout_bubble.itemAt(index).widget().deleteLater()
                # The widget at index 0 is a layout spacer, we don't need to delete it
                # That's why we end with index 1
        except Exception as e:  # If chat field was not visible or is empty
            print(e)

        # SHOW OLDER MESSAGES WITH THE ACTIVE USER IN NEW BUBBLES
        messages = user.messages()
        for message in messages:
            sender_id = message.get_sender_id()

            #  Knowing that the user with id == 1 is the owner,
            #  messages sent from user_id 1 will be shown in the right bubble
            if sender_id == 1:
                self.ui.create_right_bubble(message)
                if self.ui.message_status.objectName().startswith("error"):
                    self.ui.message_status.clicked.connect(self.resend_message)
            else:
                self.ui.create_left_bubble(message)

        # CLEAR MESSAGE COUNTER AND SHOW ONLINE TOAST IF SELECTED USER IS ONLINE
        for frame in self.ui.left_scroll.findChildren(QFrame):
            # Reset Message counter
            if frame.objectName() == user_uuid + "_counter":
                frame.setText("0")
                frame.hide()

                # Reset to normal style sheet
                frame.parent().setStyleSheet(Clients.frame_normal)

    @Slot(int)
    def show_incoming_message(self, id: int):
        """
        Shows incoming message bubble or increase new message counter
        """
        message = Message.find(id)
        user = User.find(message.get_sender_id())

        if self.ui.active_client.objectName() and self.ui.active_client.objectName() == user.get_uuid():
            self.ui.create_left_bubble(message)
        else:
            # Increase the unread message counter badge
            for widget in self.ui.left_scroll.findChildren(QFrame):
                if widget.objectName() == f"{user.get_uuid()}_counter":
                    unread_msg = int(widget.text())
                    unread_msg += 1
                    widget.setText(f"{unread_msg}")

                    try:
                        widget.show()
                    except Exception as e:
                        print(f"Error while trying to show counter widget {e}")

                    parent = widget.parent()
                    parent.setStyleSheet(Clients.frame_unread_msg)

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
        if not self.ui.active_client.text():
            QMessageBox.warning(self, "Destinataire non défini",
                                "Veuillez spécifiez d'abord votre destinataire!",
                                QMessageBox.StandardButton.Ok)
        else:
            # SEND TEXT MESSAGE
            if self.ui.send_button.styleSheet() == SendButton.style_send:
                receiver = User.where("uuid", "=", self.ui.active_client.objectName())[0]
                receiver_id = receiver.get_id()

                text_message = self.ui.entry_field.text()

                message = Message()
                message.set_sender_id(1)
                message.set_receiver_id(receiver_id)
                message.set_kind("text")
                message.set_body(text_message)

                # Send message and get it back with the status report modified
                client = Client(receiver.get_host_address())
                message = client.send_message(message)

                # Save text message in database
                message.save()

                # Show bubble
                self.ui.create_right_bubble(message)

                # Reset some ui states
                self.ui.entry_field.setText(None)
                self.ui.send_button.setStyleSheet(SendButton.style_record)
                self.ui.media_button.setEnabled(True)

            # RECORD VOICE MESSAGE
            elif self.ui.send_button.styleSheet() == SendButton.style_record:
                self.ui.media_button.setEnabled(False)
                self.record_voice()

    @Slot(str, str)
    def send_media(self, kind: str, path: str):
        """
        Sends the media message and shows bubble
        """
        receiver = User.where("uuid", "=", self.ui.active_client.objectName())[0]
        receiver_id = receiver.get_id()

        message = Message()
        message.set_sender_id(1)
        message.set_receiver_id(receiver_id)
        message.set_kind(kind)
        message.set_body(path)

        # Send message and get it back with the status report modified
        client = Client(receiver.get_host_address())
        message = client.send_message(message)

        # Save media message in database
        message.save()

        # Show bubble
        self.ui.create_right_bubble(message)

    def resend_message(self):
        """
        Resend a message that failed
        """
        clicked_button = self.sender()

        # Find message and user by id from the object name of clicked button
        message_id = clicked_button.objectName().split("_")[1]
        message = Message.find(int(message_id))
        receiver = User.find(message.get_receiver_id())

        # Send message
        client = Client(receiver.get_host_address())
        client.send_message(message)

        # Update in database
        message.update()

        # Delete old bubble and create a new one
        clicked_button.parent().deleteLater()
        self.ui.create_right_bubble(message)

# RECORDER --------------------------------------------------------------------------

    def record_voice(self):
        """
        Starts recording voice message
        """
        # SHOW RECORD WIDGET INDICATOR AND CONNECT ACTION BUTTONS
        self.ui.show_record_widget()
        self.ui.end_record.clicked.connect(self.recorder._stop)
        self.ui.cancel_record.clicked.connect(self.recorder.cancel)

        self.recorder._record()
        self.record_timer.start(1000)

    def time_counter(self):
        """
        Show recording time
        """
        global seconds, minutes

        seconds += 1
        if seconds == 10:
            minutes += 1
            seconds = 0

        time_counter = "%02d:%02d" % (minutes, seconds)
        self.ui.record_time.setText(time_counter)
        print(time_counter)

    def recorder_state_changed(self):
        """
        Perform some actions according to the recording state
        """
        global seconds, minutes

        if self.recorder.recorderState() == QMediaRecorder.StoppedState:
            self.record_timer.stop()
            self.ui.record_tip.deleteLater()
            seconds = minutes = 0

        # May change the stylesheet of Play/Pause button on a next feature

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
                thread.join()

    def check_online(self, server_host: str):
        """
        Checks online devices and show or hide green online indicator widget.
        """
        client = Client(server_host)
        threading.Thread(target=client.connect_to_server).start()
        # client.connect_to_server()

        # Show green online toast if client is online
        user = User.where("host_address", "=", server_host)
        if user:
            user_uuid = user[0].get_uuid()
            for widget in self.ui.left_scroll.findChildren(QFrame):
                if widget.objectName() == f"{user_uuid}_toast":
                    if client.online:
                        widget.show()
                    else:
                        widget.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = ChatWindow()
    sys.exit(app.exec())
