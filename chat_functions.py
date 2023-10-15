# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os
import threading
from datetime import datetime, timedelta
from functools import partial

import emojis

from PySide6.QtMultimedia import QMediaRecorder
from PySide6.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMainWindow, QWidget, QPushButton, QLabel
from PySide6.QtGui import QColor
from PySide6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, Slot, QTimer, Qt

import utils
from widgets import Bubble, ClientWidget, DateLabel, EmojiButton
from styles import Clients, SendButton, Player as PlayerStyle
from gui import Ui_MainWindow
from server import Server
from client import Client
from user import User
from message import Message
from recorder import Recorder
from player import Player
from netscanner import NetScanner
from notification import NotificationWidget

# Global variables for recorder time counter
seconds = minutes = 0


class ChatFunctions: #(QMainWindow):
    """
    Initialize chat window to show conversations and start chatting
    """

    DATE = None

    # def __init__(self):
    #     QMainWindow.__init__(self)
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self)
    #
    #     self.initialize()

    def initialize(self):
        # SHOW USERS / CONVERSATION LIST
        self.show_user_widget()

        # CONNECT SEND BUTTON
        self.ui.input.textChanged.connect(self.change_send_style)
        self.ui.send_btn.clicked.connect(self.send_text_or_record)

        # START SERVER
        # self.server = Server()
        # self.server.start()

        # LISTEN FOR MESSAGE SIGNALS
        # self.server.messageReceived.connect(self.show_incoming_message)

        # SCAN NETWORK TO FIND CONNECTED DEVICES
        self.server_hosts = {}

        # Scan on startup
        # QTimer().singleShot(60_000, self.scan_network)

        # Scan network to refresh active servers
        self.net_scanner = QTimer()
        self.net_scanner.timeout.connect(self.scan_network)
        # self.net_scanner.start(300_000)

        # CREATE RECORDER INSTANCE AND ASSOCIATED TIME COUNTER
        self.recorder = Recorder()
        self.record_timer = QTimer()
        self.record_timer.timeout.connect(self.time_counter)

        self.recorder.recorderStateChanged.connect(self.recorder_state_changed)
        self.recorder.recordConfirmed.connect(self.send_media)

        # PLAYER SETUP
        self.player = Player()
        self.player.errorOccurred.connect(lambda error: print(error))

        # self.ui.playButtonPressed.connect(self.play)

        # Just for testing
        #self.show_emojis()

        user = User.find(1)
        self.ui.me_username.setText(user.get_user_name())
        self.ui.me_status.setText(user.get_user_status())
        profile_path = user.get_image_path()
        if profile_path != "user/default.png":
            profile_picture = utils.create_rounded_image(profile_path,  self.ui.me_picture.width())
            self.ui.me_picture.setPixmap(profile_picture)
        else:
            self.ui.me_picture.setText(user.get_user_name()[0])
        # ///////////////////////



    # MESSAGES AND CONVERSATIONS -------------------------------------------------------

    def show_emojis(self):
        categories = ["Smileys & Emotion", "Animals & Nature", "Food & Drink", "Travel & Places", "Activities", "Objects", "Symbols", "Flags"]
        for i, category in enumerate(categories):
            tab = self.ui.emoji_tab_widget.widget(i)
            for widget in tab.findChildren(QWidget):
                if widget.objectName().startswith("scrollAreaWidgetContents"):
                    layout = widget.layout()

            row = 0
            column = -1
            for emoji in emojis.db.get_emojis_by_category(category):
                column += 1
                if column % 15 == 0:
                    row += 1
                    column = 0
                btn = EmojiButton(emoji.emoji)
                # layout.addWidget(btn, row, column)

    def show_user_widget(self):
        """
        Load users conversation list from users who are registered in database
        """
        # Save spacer item
        chat_list_layout_count = self.ui.chat_list_layout.count()
        spacer = self.ui.chat_list_layout.itemAt(chat_list_layout_count - 1)

        # Remove old list
        for i in reversed(range(chat_list_layout_count - 1)):
            widget = self.ui.chat_list_layout.itemAt(i).widget()
            widget.deleteLater()
            self.ui.chat_list_layout.removeWidget(widget)

        # Add new user's list
        users = User.where("id", ">=", 1)
        for user in users:
            widget = ClientWidget(user)
            last_index = self.ui.chat_list_layout.count() - 1
            self.ui.chat_list_layout.insertWidget(last_index, widget, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignTop)
            widget.clicked.connect(self.show_conversations)

        # Add spacer
        self.ui.chat_list_layout.addItem(spacer)

    @Slot(str)
    def show_conversations(self, button_object_name: str = "356a192b7913b04c54574d18c28d46e6395428ac"):
        """
        Shows conversation bubbles with a specified user
        """
        # TRY TO STOP MEDIA PLAYER
        self.player.stop()

        # GET USER UUID
        user_uuid = button_object_name

        user = User.first_where("uuid", "=", user_uuid)
        user_name = user.get_user_name()
        user_status = user.get_user_status()
        if user_status == "":
            user_status = "Hello, i'm using AR Intercom !"

        # SET NAME AND STATUS TO THE ACTIVE CLIENT LABEL
        self.ui.chat_stacked_widget.setCurrentWidget(self.ui.chat_page)
        self.ui.active_client_name.setText(user_name)
        self.ui.active_client_name.setObjectName(user_uuid)
        self.ui.active_client_status.setText(user_status)
        # picture = utils.create_rounded_image(user.get_image_path(), self.ui.active_client_picture.width())
        # self.ui.active_client_picture.setPixmap(picture)

        profile_path = user.get_image_path()
        if profile_path != "user/default.png":
            profile_picture = utils.create_rounded_image(profile_path, self.ui.active_client_picture.width())
            self.ui.active_client_picture.setPixmap(profile_picture)
        else:
            self.ui.active_client_picture.setText(user.get_user_name()[0])


        # REMOVE ACTUAL VISIBLE CHAT BUBBLES
        try:
            for index in reversed(range(1, self.ui.chat_scroll_layout.count())):
                self.ui.chat_scroll_layout.itemAt(index).widget().deleteLater()
                # The widget at index 0 is a layout spacer, we don't need to delete it
                # That's why we end with index 1
        except Exception as e:  # If chat field was not visible or is empty
            print(e)

        # CLEAR MESSAGE COUNTER AND SHOW ONLINE TOAST IF SELECTED USER IS ONLINE
        message_counter = self.ui.chat_list_scroll.findChild(QLabel, f"{user_uuid}_counter")
        message_counter.setText("0")
        message_counter.hide()

        # RESET DATE
        self.DATE = None

        # SHOW OLDER MESSAGES WITH THE ACTIVE USER IN NEW BUBBLES
        messages = user.messages()
        for message in messages:
            self.show_bubble(message)

        # Reset to normal style sheet (important in case of unread messages)
        # message_counter.parent().setStyleSheet(Clients.frame_normal)

        # Connect delete messages button
        # self.ui.delete_btn.clicked.connect(self.delete_messages)

    def show_bubble(self, message: Message):

        # SHOW DATE LABEL
        date = message.get_created_at()
        today = datetime.today()
        yesterday = datetime.now() - timedelta(days=1)

        if datetime.strftime(date, "%x") == datetime.strftime(today, "%x"):
            text = "Today"
        elif datetime.strftime(date, "%x") == datetime.strftime(yesterday, "%x"):
            text = "Yesterday"
        else:
            text = datetime.strftime(date, "%d - %m - %Y")

        if text != self.DATE:
            self.DATE = text
            date_label = DateLabel(self.DATE.upper())
            self.ui.chat_scroll_layout.addWidget(date_label, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)

        # SHOW BUBBLE
        if message.get_sender_id() == 1:
            bubble = Bubble(message, "right")
            self.ui.chat_scroll_layout.addWidget(bubble, 0, Qt.AlignmentFlag.AlignRight)
        else:
            bubble = Bubble(message, "left")
            self.ui.chat_scroll_layout.addWidget(bubble)


        # Connect play button if the bubble is of type voice:
        if message.get_kind() in ["voice", "audio", "video"]:
            bubble.playButtonClicked.connect(lambda x: print(x))

        # UPDATE SCROLL POSITION
        vertical_scroll = self.ui.chat_scroll.verticalScrollBar()
        QTimer.singleShot(500, lambda: vertical_scroll.setValue(vertical_scroll.maximum()))


    @Slot(int)
    def show_incoming_message(self, id: int):
        """
        Shows incoming message bubble or increase new message counter
        """
        message = Message.find(id)
        user = User.find(message.get_sender_id())

        if self.ui.active_client_name.isVisible() and self.ui.active_client_name.objectName() == user.get_uuid():
            # Show message in the bubble
            self.show_bubble(message)
        else:
            # Show notification widget
            self.notification_widget = NotificationWidget(user.get_user_name())
            self.notification_widget.show()

            # Increase the unread message counter badge
            message_count = self.ui.left_scroll.findChild(QLabel, f"{user.get_uuid()}_counter")
            unread_msg = int(message_count.text())
            unread_msg += 1
            message_count.setText(f"{unread_msg}")

            message_count.show()
            # message_count.parent().setStyleSheet(Clients.frame_unread_msg)

    @Slot()
    def change_send_style(self):
        """
        Changes send button style, and disable media button so that a user can not send media message and text message
        at a time.
        """
        if self.ui.input.toPlainText():
            print(self.ui.input.toPlainText())
            # Change send button style
            self.ui.send_btn.setStyleSheet(SendButton.style_send)
            # Disable media button
            self.ui.media_btn.setEnabled(False)

        else:
            self.ui.send_btn.setStyleSheet(SendButton.style_record)
            self.ui.media_btn.setEnabled(True)

    @Slot()
    def send_text_or_record(self):
        """
        According to the send button style, send text message or record a voice
        """
        # if not self.ui.active_client_name.show_text_bubble():
        #     QMessageBox.warning(self, "Destinataire non défini",
        #                         "Veuillez sélectionner d'abord votre destinataire !",
        #                         QMessageBox.StandardButton.Ok)

        text_message = self.ui.input.toPlainText()

        # SEND TEXT MESSAGE
        if text_message:
            receiver = User.first_where("uuid", "=", self.ui.active_client_name.objectName())
            receiver_id = receiver.get_id()

            message = Message()
            message.set_sender_id(1)
            message.set_receiver_id(receiver_id)
            message.set_kind("text")
            message.set_body(text_message)

            # Send message and get it back with the status report modified
            client = Client(receiver.get_host_address())
            message = client.send_message(message)
            message.set_created_at()  # Now
            message.set_updated_at()  # Now

            # Save text message in database
            message.save()

            # Show bubble
            self.show_bubble(message)

            # Reset some ui states
            self.ui.input.setText(None)
            self.ui.send_btn.setStyleSheet(SendButton.style_record)
            self.ui.media_btn.setEnabled(True)

        # RECORD VOICE MESSAGE
        else:
            self.ui.media_btn.setEnabled(False)
            self.ui.send_btn.setEnabled(False)
            self.record_voice()

    @Slot(str, str)
    def send_media(self, kind: str, path: str):
        """
        Sends the media message and shows bubble
        """
        receiver = User.first_where("uuid", "=", self.ui.active_client_name.objectName())
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
        self.show_bubble(message)

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
        # clicked_button.parent().deleteLater()
        self.show_bubble(message)

    @Slot()
    def delete_messages(self):
        user = User.first_where("uuid", "=", self.ui.active_client_name.objectName())
        messages = user.messages()

        print("Deleting conversation of you with", user.get_user_name())
        for index in reversed(range(1, self.ui.chat_scroll_layout.count())):
            self.ui.chat_scroll_layout.itemAt(index).widget().deleteLater()

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
        # self.show_record_widget()
        # self.ui.end_record.clicked.connect(self.recorder._stop)
        # self.ui.cancel_record.clicked.connect(self.recorder.cancel)

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
        print(time_counter)
        # self.ui.record_time.setText(time_counter)

    def recorder_state_changed(self):
        """
        Perform some actions according to the recording state
        """
        global seconds, minutes

        if self.recorder.recorderState() == QMediaRecorder.StoppedState:
            self.record_timer.stop()
            # self.ui.record_tip.deleteLater()
            seconds = minutes = 0
            self.ui.media_btn.setEnabled(True)
            self.ui.send_btn.setEnabled(True)

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

            self.show_user_widget(user, online=True)

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    chat_window = ChatFunctions()
    chat_window.show()
    sys.exit(app.exec())
