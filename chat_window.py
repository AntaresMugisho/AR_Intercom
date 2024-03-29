# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os
import time
import threading
from functools import partial

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QWidget, QSlider, QMessageBox, QSpacerItem, QSizePolicy
from PySide6.QtCore import QObject, QTimer, Slot, Qt, Signal, QThreadPool
from PySide6.QtMultimedia import QMediaRecorder, QMediaPlayer

from ui.chat_window import Ui_ChatWindow
from styles import Clients, SendButton, Player as PlayerStyle
from server import Server
from client import Client

from user import User
from message import Message
from recorder import Recorder
from player import Player
from netscanner import NetScanner
from notification import NotificationWidget
import utils

# Global variables for recorder time counter
seconds = minutes = 0


class ChatWindow(QWidget):
    """
    Initialize chat window to show conversations and start chatting
    """
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self)

        # SHOW USERS / CONVERSATION LIST
        users = User.where("id", ">", 1)
        for user in users:
            self.ui.show_user_widget(user)

        # CONNECT USER'S CONVERSATION BUTTONS
        self.ui.conversationButtonPressed.connect(self.show_conversations)

        # CONNECT SEND BUTTON
        self.ui.entry_field.textEdited.connect(self.change_send_style)
        self.ui.entry_field.returnPressed.connect(self.send_text_or_record)
        self.ui.send_button.clicked.connect(self.send_text_or_record)

        # START SERVER
        self.server = Server()
        self.server.start()

        # LISTEN FOR MESSAGE SIGNALS
        self.server.messageReceived.connect(self.show_incoming_message)

        # SCAN NETWORK TO FIND CONNECTED DEVICES
        self.server_hosts = {}

        # Scan on startup
        QTimer().singleShot(60_000, self.scan_network)

        # Scan network to refresh active servers
        self.net_scanner = QTimer()
        self.net_scanner.timeout.connect(self.scan_network)
        self.net_scanner.start(300_000)

        # CREATE RECORDER INSTANCE AND ASSOCIATED TIME COUNTER
        self.recorder = Recorder()
        self.record_timer = QTimer()
        self.record_timer.timeout.connect(self.time_counter)

        self.recorder.recorderStateChanged.connect(self.recorder_state_changed)
        self.recorder.recordConfirmed.connect(self.send_media)

        # PLAYER SETUP
        self.player = Player()
        self.player.errorOccurred.connect(lambda error: print(error))

        self.ui.playButtonPressed.connect(self.play)

    # MESSAGES AND CONVERSATIONS -------------------------------------------------------

    @Slot(str)
    def show_conversations(self, button_object_name: str):
        """
        Shows conversation bubbles with a specified user
        """
        # TRY TO STOP MEDIA PLAYER
        self.player.stop()

        # GET USER UUID
        user_uuid = button_object_name

        user = User.first_where("uuid", "=", user_uuid)
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
        message_counter = self.ui.left_scroll.findChild(QLabel, f"{user_uuid}_counter")
        message_counter.setText("0")
        message_counter.hide()

        # Reset to normal style sheet (important in case of unread messages)
        message_counter.parent().setStyleSheet(Clients.frame_normal)

        # Connect delete messages button
        self.ui.delete_button.clicked.connect(self.delete_messages)

    @Slot(int)
    def show_incoming_message(self, id: int):
        """
        Shows incoming message bubble or increase new message counter
        """
        message = Message.find(id)
        user = User.find(message.get_sender_id())

        if self.ui.active_client.objectName() and self.ui.active_client.objectName() == user.get_uuid():
            # Show message in the bubble
            self.ui.create_left_bubble(message)
        else:
            # Show notification widget
            self.notification_widget = NotificationWidget(user.get_user_name())
            self.notification_widget.show()

            # Increase the unread message counter badge
            message_counter = self.ui.left_scroll.findChild(QLabel, f"{user.get_uuid()}_counter")
            unread_msg = int(message_counter.text())
            unread_msg += 1
            message_counter.setText(f"{unread_msg}")

            try:
                message_counter.show()
            except Exception as e:
                print(f"Error while trying to show counter widget {e}")

            message_counter.parent().setStyleSheet(Clients.frame_unread_msg)

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
                                "Veuillez sélectionner d'abord votre destinataire !",
                                QMessageBox.StandardButton.Ok)

        # SEND TEXT MESSAGE
        elif self.ui.entry_field.text():
            receiver = User.first_where("uuid", "=", self.ui.active_client.objectName())
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
        elif not self.ui.entry_field.text():
            self.ui.media_button.setEnabled(False)
            self.ui.send_button.setEnabled(False)
            self.record_voice()

    @Slot(str, str)
    def send_media(self, kind: str, path: str):
        """
        Sends the media message and shows bubble
        """
        receiver = User.first_where("uuid", "=", self.ui.active_client.objectName())
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

    @Slot()
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
        message = client.send_message(message)

        # Update in database
        message.update()

        # Delete old bubble and create a new one
        clicked_button.parent().deleteLater()
        self.ui.create_right_bubble(message)

    @Slot()
    def delete_messages(self):
        user = User.first_where("uuid", "=", self.ui.active_client.objectName())
        messages = user.messages()

        print("Deleting conversation of you with", user.get_user_name())
        for index in reversed(range(1, self.ui.layout_bubble.count())):
            self.ui.layout_bubble.itemAt(index).widget().deleteLater()

        for message in messages:
            if message.get_kind() != "text":
                try:
                    os.remove(message.get_body())
                except Exception as e:
                    print("Error while trying to delete file: ", e)

            message.delete()

    # MEDIA RECORDER -----------------------------------------------------------------

    @Slot()
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
        if seconds == 60:
            minutes += 1
            seconds = 0

        time_counter = "%02d:%02d" % (minutes, seconds)
        self.ui.record_time.setText(time_counter)

    def recorder_state_changed(self):
        """
        Perform some actions according to the recording state
        """
        global seconds, minutes

        if self.recorder.recorderState() == QMediaRecorder.StoppedState:
            self.record_timer.stop()
            self.ui.record_tip.deleteLater()
            seconds = minutes = 0
            self.ui.media_button.setEnabled(True)
            self.ui.send_button.setEnabled(True)

    # MEDIA PLAYER ----------------------------------------------------------------------

    @Slot(QPushButton)
    def play(self, play_button: QPushButton):
        """
        Play/Pause Media
        """
        # IF PLAYER IS IN PLAYING STATE, THE PAUSE
        if play_button.objectName() == "playing":
            self.player._pause()

        else:
            # Try to stop an eventual playing player
            self.player.stop()

            # GET PATH, ELAPSED AND TOTAL TIME LABELS
            parent = play_button.parent()
            title_label, elapsed_time, total_time = parent.findChildren(QLabel)
            slider = parent.findChild(QSlider)

            path = title_label.objectName().split("|")[1]
            self.player = Player()
            self.player._play(path)

            # Show GUI indications of playing state
            play_button.setStyleSheet(PlayerStyle.pause)
            play_button.setObjectName("playing")
            slider.setMaximum(self.player.duration())
            total_time.setText(ChatWindow.hhmmss(self.player.duration()))

            # Connect signals
            slider.valueChanged.connect(self.player.setPosition)
            self.player.durationChanged.connect(partial(self.update_duration, slider, total_time))
            self.player.positionChanged.connect(partial(self.update_position, slider, elapsed_time))
            self.player.playbackStateChanged.connect(partial(self.player_state_changed, play_button))

    @staticmethod
    def hhmmss(milliseconds: int):
        """
        Converts millisecond time in hour, minute and seconds
        """
        h, r = divmod(milliseconds, 3_600_000)
        m, r = divmod(r, 60_000)
        s, _ = divmod(r, 1000)
        return ("%02d:%02d:%02d" % (h, m, s)) if h else ("%02d:%02d" % (m, s))

    @staticmethod
    def update_duration(slider: object, total_time: object, duration: int):
        """
        Update player duration on GUI
        """
        # Update slider maximum value
        slider.setMaximum(duration)

        # Show total time on label
        total_time.setText(ChatWindow.hhmmss(duration))

    @staticmethod
    def update_position(slider: object, elapsed_time: object, position: int):
        """
        Update player position on GUI
        """
        # Update time on GUI label
        elapsed_time.setText(ChatWindow.hhmmss(position))

        # Disable slider signals to prevent updating triggering a
        # setPosition signal (can cause stuttering).
        slider.blockSignals(True)
        slider.setValue(position)
        slider.blockSignals(False)

    def player_state_changed(self, play_button: QPushButton, state: object):
        """
        Perform some actions according to the playing state
        """
        if state == QMediaPlayer.PlaybackState.PlayingState:
            play_button.setStyleSheet(PlayerStyle.pause)

        if state == QMediaPlayer.PlaybackState.PausedState:
            play_button.setStyleSheet(PlayerStyle.play)

        elif state == QMediaPlayer.PlaybackState.StoppedState:
            self.player.setPosition(0)
            play_button.setStyleSheet(PlayerStyle.play)
            play_button.setObjectName(None)

    def player_error(self, error):
        if error == QMediaPlayer.Error.ResourceError:
            print("Player resource error")
            self.player.stop()

    # NETWORKING  ----------------------------------------------------------------------
    def scan_network(self):
        """
        Scan network to find connected devices and put them in server_host dictionary.
        """
        my_ip = utils.get_private_ip()
        if my_ip.startswith("127.0"):
            print("Aucune connexion détectée.\nVeuillez vous connecter à un réseau !")

        else:
            my_ip_bytes = my_ip.split(".")
            net_id = ".".join(my_ip_bytes[:3])

            # Create threads
            threads = []
            for host_id in range(1, 255):
                if host_id != int(my_ip_bytes[3]):
                    address = f"{net_id}.{host_id}"
                    scanner = NetScanner(address)
                    scanner.signal.scanFinished.connect(self.check_online)

                    threads.append(scanner)

            # Start threads
            for scanner in threads:
                scanner.start()

    def check_online(self, hosts: dict):
        """
        Checks online devices and show or hide green online indicator widget.
        """
        clients = []
        threads = []

        for host_address in hosts.keys():
            client = Client(host_address)
            clients.append(client)

            th = threading.Thread(target=client.connect_to_server)
            threads.append(th)

        for thread in threads:
            thread.start()

        for client in clients:
            user = User.first_where("host_name", "=", hosts.get(client.server_host))

            # Show green online toast cause the client is online
            if user:
                user_uuid = user.get_uuid()
                online_toast = self.ui.left_scroll.findChild(QLabel, f"{user_uuid}_toast")

                if client.online:
                    print(f"[+] {client.server_host} online")
                    online_toast.show()

                    # Send my ID to the connected client
                    message = Message()
                    message.set_kind("ID")
                    client.send_message(message)

                else:
                    print(f"[-] {client.server_host} offline")
                    online_toast.hide()
            else:
                if client.online:
                    self.add_user(client.server_host, hosts.get(client.server_host))

    def add_user(self, host_address, host_name):
        """
        Add new user in the database
        """
        # Save user database
        if host_name is not None:
            host_name = host_name.capitalize()
            print(f"Adding new user {host_name}")
            user = User()
            user.set_user_name(host_name)
            user.set_host_address(host_address)
            user.set_host_name(host_name)
            user.set_image_path()
            user.save()

            self.ui.show_user_widget(user, online=True)


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    chat_window = ChatWindow()
    chat_window.show()
    sys.exit(app.exec())
