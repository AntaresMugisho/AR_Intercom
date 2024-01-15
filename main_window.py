# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os
import threading
from datetime import datetime, timedelta
from functools import partial

import EmojiStore
from PySide6.QtMultimedia import QMediaRecorder, QMediaPlayer
from PySide6.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMainWindow, QWidget, QPushButton, QLabel, QScrollArea, QGridLayout, QHBoxLayout, QVBoxLayout, QTabWidget, QFileDialog, QSlider
from PySide6.QtGui import QColor
from PySide6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, Slot, QTimer, Qt
from sqlalchemy import or_

import utils
from model.base import db
from styles import Clients, SendButton, Player as PlayerStyle
from server import Server
from client import Client
from model import User, Message
from recorder import Recorder
from player import Player
from netscanner import NetScanner
from notification import NotificationWidget
from gui import Ui_MainWindow
from widgets import Bubble, ClientWidget, DateLabel, EmojiButton, ScanResult

# Global variables for recorder time counter
seconds = minutes = 0


class MainWindow(QMainWindow):
    """
    Main window
    """

    WINDOW_MAXIMIZED = False
    # DATE = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # REMOVE DEFAULT WINDOW FRAME
        self.ui.app_margins.setContentsMargins(0, 0, 0, 0)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # SET MOVE EVENT ON THE WINDOW
        self.dragPos = None
        self.ui.app_brand.mouseMoveEvent = self.move_window
        self.ui.auth_user_box.mouseMoveEvent = self.move_window
        self.ui.title_bar.mouseMoveEvent = self.move_window
        self.ui.app_title.mouseMoveEvent = self.move_window

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        # self.ui.app_bg.setGraphicsEffect(self.shadow)

        # HIDE SOME WIDGETS ON START UP
        self.ui.system_menu.hide()
        self.ui.last_seen.hide()
        self.ui.right_stacked_widget.setFixedWidth(0)
        self.ui.emoji_widget.setFixedHeight(0)
        self.ui.media_bg.setFixedHeight(0)
        self.ui.record_widget.hide()
        self.ui.chat_page_layout.removeWidget(self.ui.media_bg)

        # CONNECT BUTTONSf
        self.ui.menu_btn.clicked.connect(self.toggle_menu)
        self.ui.settings_btn.clicked.connect(self.toggle_settings)
        self.ui.emoji_btn.clicked.connect(self.toggle_emojis)
        self.ui.close_emoji_btn.clicked.connect(self.toggle_emojis)
        self.ui.media_btn.clicked.connect(self.toggle_media)
        self.ui.start_scan_btn.clicked.connect(self.scan_network)

        # Choose media buttons
        self.ui.media_doc.clicked.connect(self.choose_media)
        self.ui.media_audio.clicked.connect(self.choose_media)
        self.ui.media_image.clicked.connect(self.choose_media)
        self.ui.media_video.clicked.connect(self.choose_media)

        # System buttons
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        self.ui.maximize_restore_btn.clicked.connect(self.maximize_restore)
        self.ui.close_btn.clicked.connect(self.close)

        # Menus
        self.ui.home_btn.clicked.connect(self.menu_click)
        self.ui.scan_btn.clicked.connect(self.menu_click)
        self.ui.chat_btn.clicked.connect(self.menu_click)
        self.ui.about_btn.clicked.connect(self.menu_click)

        # self.ui.chat_scroll_layout.itemAt(1).spacerItem()

        # Start on home page
        self.ui.home_btn.clicked.emit()
        # self.ui.chat_btn.clicked.emit()

        # Chat buttons connection
        self.ui.input.textChanged.connect(self.change_send_style)
        self.ui.send_btn.clicked.connect(self.send_text_or_record)

        # Load / show components
        QTimer().singleShot(1000, self.load_auth_user_details)
        QTimer().singleShot(1500, self.load_user_list)
        QTimer().singleShot(2000, self.load_emojis)

        # Initialize chat functions
        self.initialize_chat()

        # SHOW MAIN WINDOW
        self.show()

    # MAIN UI FUNCTIONS ################################################################################################

    def closeEvent(self, event) -> None:
        try:
            self.server.stop()
            self.player.stop()
            self.recorder.stop()
        except Exception as e:
            print(f"Error while closing : ", e)
        finally:
            self.close()

    def maximize_restore(self):
        """
        Minimize and restore the window size
        """
        if not self.WINDOW_MAXIMIZED:
            self.showMaximized()
            self.WINDOW_MAXIMIZED = True
            self.ui.maximize_restore_btn.setStatusTip("Restore")
            self.ui.maximize_restore_btn.setStyleSheet("background-image:url(:/cils/cils/icon_restore.png);")

        else:
            self.showNormal()
            self.WINDOW_MAXIMIZED = False
            self.ui.maximize_restore_btn.setStatusTip("Maximize")
            self.ui.maximize_restore_btn.setStyleSheet("background-image:url(:/cils/cils/icon_maximize.png);")

    def move_window(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos.toPoint())
            self.dragPos = event.globalPosition()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition()

    @Slot()
    def menu_click(self):
        """
        Change view when the user clicks on a menu.
        """
        menu_btn: QPushButton = self.sender()
        menu = menu_btn.objectName()
        self.set_as_active(menu)

        if menu == "home_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.about_page)
            self.ui.chat_stacked_widget.setCurrentWidget(self.ui.home_page)

        elif menu == "scan_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.contact_page)
            self.ui.contacts_stack.setCurrentWidget(self.ui.scan_page)

        elif menu == "chat_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.contact_page)
            self.ui.contacts_stack.setCurrentWidget(self.ui.chat_list_page)

        elif menu == "about_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.about_page)

    def set_as_active(self, menu):
        """
        Change the active menu style.
        """
        selected_menu_style = """
            text-align:left;
            padding-left:42px;
            border-left:16px solid transparent;
            border-radius: 0px;
            background-repeat:none;
            background-position:center left;		
            border-left: 16px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.699 
                rgba(255, 200, 200, 255), stop:0.7 rgba(0, 0, 0, 0));
            background-color: rgb(40, 42, 43);
        """

        for btn in self.ui.left_menu.findChildren(QPushButton):
            if btn.objectName() == menu:
                btn.setStyleSheet(btn.styleSheet() + selected_menu_style)
            else:
                reset_style = btn.styleSheet().replace(selected_menu_style, "")
                btn.setStyleSheet(reset_style)

    def start_animation(self, widget, min, max):
        """
        Animate widget
        """
        if widget.width() <= min:
            start_value = min
            end_value = max
        else:
            start_value = max
            end_value = min

        # ANIMATION SETTINGS BOX
        self.animation = QPropertyAnimation(widget, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation.start()

    @Slot()
    def toggle_settings(self):
        """
        Show/Hide settings widget
        """
        self.start_animation(self.ui.right_stacked_widget, 0, 251)

    @Slot()
    def toggle_menu(self):
        """
        Show/Hide menu text
        """
        self.start_animation(self.ui.left_menu, 60, 163)

    # CONVERSATION SCREEN FUNCTIONS ####################################################################################

    @Slot()
    def toggle_emojis(self):
        """
        Show/Hide emoji list widget on chat screen
        """
        if self.ui.emoji_widget.height() == 0:
            self.ui.emoji_widget.setFixedHeight(196)
        else:
            self.ui.emoji_widget.setFixedHeight(0)

    @Slot()
    def toggle_media(self):
        """
        Show/Hide buttons to send media messages on chat screen
        """
        if self.ui.media_bg.height() == 0:
            self.ui.media_bg.move(QPoint(12, self.ui.chat_page.height() - 260))
            self.ui.media_bg.setFixedHeight(190)

        else:
            self.ui.media_bg.setFixedHeight(0)
            # self.ui.chat_page_layout.addWidget(self.ui.media_bg)

    def load_emojis(self):
        categories = ['smileys_and_people',
                      'animals_and_nature',
                      'food_and_drink',
                      'travel_and_places',
                      'activities',
                      'objects',
                      'symbols',
                      'flags'
        ]

        for i, category in enumerate(categories):
            tab: QTabWidget = self.ui.emoji_tab_widget.widget(i)
            scroll_area: QScrollArea = tab.findChild(QScrollArea)
            layout: QGridLayout = scroll_area.widget().layout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(2)

            # Delete default emoji button from the layout
            layout.itemAtPosition(0, 0).widget().deleteLater()

            row = 0
            column = -1
            for emoji in EmojiStore.get_by_category(category):
                column += 1
                if column % 24 == 0:
                    row += 1
                    column = 0
                btn = EmojiButton(emoji.emoji)
                btn.emojiClicked.connect(self.ui.input.textCursor().insertText)
                layout.addWidget(btn, row, column)

    def load_auth_user_details(self):
        user = User.query.first()
        self.ui.me_username.setText(user.user_name)
        self.ui.me_status.setText(user.user_status)
        profile_path = user.image_path

        if profile_path is not None:
            profile_picture = utils.create_rounded_image(profile_path, self.ui.me_picture.width())
            self.ui.me_picture.setPixmap(profile_picture)
        else:
            self.ui.me_picture.setText(user.user_name[0])

    def load_user_list(self):
        """
        Load users conversation list from users who are registered in database
        """
        # Clear layout
        utils.clear_layout(self.ui.chat_list_layout)

        # Add new user's list
        users = User.query.filter(User.id > 1).order_by(User.updated_at.desc()).all()
        for user in users:
            widget = ClientWidget(user)
            last_index = self.ui.chat_list_layout.count() - 1
            self.ui.chat_list_layout.insertWidget(last_index, widget, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignTop)
            widget.clicked.connect(self.show_conversations)

    @staticmethod
    def send_id(host_address: str):
        # SEND MY IDs
        client = Client(host_address)
        message = Message()
        message.kind = "ID_RESPONSE"
        client.send_message(message)

    def initialize_chat(self):
        # START SERVER
        self.server = Server()
        QTimer().singleShot(1000, self.server.start)

        # LISTEN FOR MESSAGE SIGNALS
        self.server.messageReceived.connect(self.show_incoming_message)
        self.server.idRequested.connect(self.send_id)
        self.server.userAdded.connect(self.load_user_list)

        # SCAN NETWORK TO FIND CONNECTED DEVICES
        self.server_hosts = {}

        # CREATE RECORDER INSTANCE AND ASSOCIATED TIME COUNTER
        self.recorder = Recorder()
        self.record_timer = QTimer()
        self.record_timer.timeout.connect(self.time_counter)

        self.recorder.recorderStateChanged.connect(self.recorder_state_changed)
        self.recorder.recordConfirmed.connect(self.send_media)

        # Create a Player instance
        self.player = Player()

    # MESSAGES AND CONVERSATIONS -------------------------------------------------------

    @Slot(str)
    def show_conversations(self, button_object_name: str):
        """
        Shows conversation bubbles with a specified user
        """
        # TRY TO STOP MEDIA PLAYER
        try:
            self.player.stop()
        except AttributeError:
            pass

        # GET USER UUID
        user_uuid = button_object_name
        user = User.query.filter(User.uuid == user_uuid).first()

        # SET NAME AND STATUS TO THE ACTIVE CLIENT LABEL
        self.ui.chat_stacked_widget.setCurrentWidget(self.ui.chat_page)
        self.ui.active_client_name.setText(user.user_name)
        self.ui.active_client_name.setObjectName(user.uuid)
        self.ui.active_client_status.setText(user.user_status)

        # DISPLAY PROFILE PICTURE
        profile_path = user.image_path
        if profile_path is not None:
            profile_picture = utils.create_rounded_image(profile_path, self.ui.active_client_picture.width())
            self.ui.active_client_picture.setPixmap(profile_picture)
        else:
            self.ui.active_client_picture.setText(user.user_name[0])

        # REMOVE ACTUAL VISIBLE CHAT BUBBLES
        utils.clear_layout(self.ui.chat_scroll_layout, start=2, end=0)

        # CLEAR MESSAGE COUNTER AND SHOW ONLINE TOAST IF SELECTED USER IS ONLINE
        message_counter = self.ui.chat_list_scroll.findChild(QLabel, f"{user.uuid}_counter")
        message_counter.setText("0")
        message_counter.hide()

        # RESET DATE
        self.DATE = None

        # SHOW OLDER MESSAGES WITH THE ACTIVE USER IN NEW BUBBLES
        messages = Message.query.filter(or_(Message.sender_id == user.id, Message.receiver_id == user.id)).order_by(Message.updated_at).all()
        for message in messages:
            self.show_bubble(message)
            if not message.read:
                message.read = True

        db.commit()
        # Reset to normal style sheet (important in case of unread messages)
        # message_counter.parent().setStyleSheet(Clients.frame_normal)

        # Connect delete messages button
        self.ui.delete_btn.clicked.connect(self.delete_messages)

        # SEND MY IDs
        client = Client(user.host_address)
        message = Message()
        message.kind = "ID_RESPONSE"
        client.send_message(message)

    def show_bubble(self, message: Message):

        # FORMAT DATE LABEL
        date = message.created_at
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
        if message.sender_id == 1:
            bubble = Bubble(message, "right")
            self.ui.chat_scroll_layout.addWidget(bubble, 0, Qt.AlignmentFlag.AlignRight)
        else:
            bubble = Bubble(message, "left")
            self.ui.chat_scroll_layout.addWidget(bubble, 0, Qt.AlignmentFlag.AlignLeft)

        # Connect play button if the bubble is of playable media type:
        if message.kind in ["voice", "audio", "video"]:
            bubble.playButtonClicked.connect(self.play)

        # UPDATE SCROLL POSITION
        vertical_scroll = self.ui.chat_scroll.verticalScrollBar()
        QTimer.singleShot(500, lambda: vertical_scroll.setValue(vertical_scroll.maximum()))

    @Slot(int)
    def show_incoming_message(self, id: int):
        """
        Shows incoming message bubble or increase new message counter
        """
        message = Message.query.filter(Message.id == id).first()
        user = message.sender

        if self.ui.active_client_name.isVisible() and self.ui.active_client_name.objectName() == user.uuid:
            # Show message in the bubble
            message.read = True
            self.show_bubble(message)
        else:
            # Show notification widget
            self.notification_widget = NotificationWidget(user.user_name)
            self.notification_widget.show()

            # Increase the unread message counter badge
            message_count = self.ui.chat_list_scroll.findChild(QLabel, f"{user.uuid}_counter")
            unread_msg = int(message_count.text()) + 1
            message_count.setText(f"{unread_msg}")

            message_count.show()
            # Changing client frame design may be more user friendly

        # Update user's list
        user.update()
        db.commit()
        self.load_user_list()

    @Slot()
    def change_send_style(self):
        """
        Changes send button style, and disable media button so that a user can not send media message and text message
        at a time.
        """
        if self.ui.input.toPlainText():
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
        text_message = self.ui.input.toPlainText()

        # SEND TEXT MESSAGE
        if text_message:
            receiver = User.query.filter(User.uuid == self.ui.active_client_name.objectName()).first()

            message = Message()
            message.sender = User.query.first()
            message.receiver = receiver
            message.kind = "text"
            message.body = text_message

            # Send message and get it back with the status report modified
            client = Client(receiver.host_address)
            message = client.send_message(message)

            # Save text message in database
            db.add(message)

            # Update user's list
            receiver.update()
            db.commit()
            self.load_user_list()

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
        receiver = User.query.filter(User.uuid == self.ui.active_client_name.objectName()).first()

        message = Message()
        message.sender = User.query.first()
        message.receiver = receiver
        message.kind = kind
        message.body = path

        # Send message and get it back with the status report modified
        client = Client(receiver.host_address)
        message = client.send_message(message)

        # Save media message in database
        db.add(message)

        # Update user's list
        receiver.update()
        db.commit()
        self.load_user_list()

        # Show bubble
        self.show_bubble(message)

    def choose_media(self):
        """
        Choose files to send
        """
        media: QPushButton = self.sender()

        if media.objectName() == "media_audio":
            kind = "audio"
            filters = "Audio files (*.mp3 *.m4a *.aac *.wav)"

        elif media.objectName() == "media_video":
            kind = "video"
            filters = "Video files (*.mp4 *.avi *.mpeg *.mkv)"

        elif media.objectName() == "media_image":
            kind = "image"
            filters = "Image files (*.jpeg *.jpg *.png)"

        else:
            kind = "document"
            filters = "Any file (*)"

        paths = QFileDialog.getOpenFileNames(self, "Seletionner le.s fichier.s à envoyer", "", filters)[0]

        # Close media buttons
        self.toggle_media()

        # Send selected files
        for path in paths:
            self.send_media(kind, path)

    @Slot()
    def resend_message(self):
        """
        Resend a message that failed
        """
        clicked_button = self.sender()

        # Find message and user by id from the object name of clicked button
        message_id = clicked_button.objectName().split("_")[1]
        message = Message.query.filter(Message.id == int(message_id)).first()
        receiver = Message.receiver

        # Send message
        client = Client(receiver.host_address)
        message = client.send_message(message)

        # Update in database
        message.update()
        db.commit()

        # Delete old bubble and create a new one
        # clicked_button.parent().deleteLater()
        self.show_bubble(message)

    @Slot()
    def delete_messages(self):
        user = User.query.filter(User.uuid == self.ui.active_client_name.objectName()).first()
        messages = Message.query.filter(or_(Message.sender == user, Message.receiver == user)).all()

        utils.clear_layout(self.ui.chat_scroll_layout, start=2, end=0)

        for message in messages:
            db.delete(message)

        db.commit()

        self.show_conversations(user.uuid)

    # MEDIA RECORDER -----------------------------------------------------------------

    @Slot()
    def record_voice(self):
        """
        Starts recording voice message
        """
        # SHOW RECORD WIDGET INDICATOR AND CONNECT ACTION BUTTONS
        self.ui.record_widget.show()
        self.ui.end.clicked.connect(self.recorder._stop)
        self.ui.cancel.clicked.connect(self.recorder.cancel)

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
        self.ui.time.setText(time_counter)

    def recorder_state_changed(self):
        """
        Perform some actions according to the recording state
        """
        global seconds, minutes

        if self.recorder.recorderState() == QMediaRecorder.RecorderState.StoppedState:
            self.record_timer.stop()
            self.ui.record_widget.hide()
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
            total_time.setText(MainWindow.hhmmss(self.player.duration()))

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
    def update_duration(slider: QSlider, total_time: QLabel, duration: int):
        """
        Update player duration on GUI
        """
        # Update slider maximum value
        slider.setMaximum(duration)

        # Show total time on label
        total_time.setText(MainWindow.hhmmss(duration))

    @staticmethod
    def update_position(slider: QSlider, elapsed_time: QLabel, position: int):
        """
        Update player position on GUI
        """
        # Update time on GUI label
        elapsed_time.setText(MainWindow.hhmmss(position))

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
        utils.clear_layout(self.ui.scan_list_layout)
        self.ui.start_scan_btn.setText("SCANNING...")

        my_ip = utils.get_private_ip()
        if my_ip.startswith("127."):
            self.ui.signal_text.setText("Please connect to a network.")
            self.ui.start_scan_btn.setText("SCAN")

        else:
            self.ui.signal_text.setText("You're connected !")
            my_ip_bytes = my_ip.split(".")
            net_id = ".".join(my_ip_bytes[:3])

            # Create network scanner threads
            threads = []
            for host_id in range(1, 255):
                if host_id != int(my_ip_bytes[3]):
                    address = f"{net_id}.{host_id}"
                    scanner = NetScanner(address)
                    scanner.signal.scanFinished.connect(self.check_online)

                    threads.append(scanner)

            # Start network scanner threads
            for scanner in threads:
                scanner.start()

    def check_online(self, hosts: dict):
        """
        Display discovered hosts
        """
        for item in hosts.items():
            last_index = self.ui.scan_list_layout.count() - 1
            widget = ScanResult(item[1], item[0])
            self.ui.scan_list_layout.insertWidget(last_index, widget)

            widget.clicked.connect(self.add_user)

        self.ui.start_scan_btn.setText("SCAN")

    def add_user(self, host_address):
        """
        Add new user in the database
        """
        print(f'Try to add user {host_address}')
        client = Client(host_address)

        message = Message()
        message.kind = "ID_REQUEST"
        client.send_message(message)

        if host_address in Client.CONNECTED_SERVERS:
            self.ui.signal_text.setText("Adding user...")

        QTimer().singleShot(5_000, lambda: self.ui.signal_text.setText("You're connected !"))


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
