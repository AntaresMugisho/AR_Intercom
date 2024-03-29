# -*- coding: utf-8 -*-
import os.path

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QSizePolicy, QLabel
from PySide6.QtCore import QObject, Qt, Signal, Slot

from message import Message
import utils
from styles import *
from resources import img_rc


class Ui_ChatWindow(QObject):

    playButtonPressed = Signal(object)
    conversationButtonPressed = Signal(object)

    def setupUi(self, ChatWindow):
        if not ChatWindow.objectName():
            ChatWindow.setObjectName(u"ChatWindow")

        ChatWindow.resize(690, 470)
        icon = QtGui.QIcon()
        icon.addFile(":/icons/icons/app_icon.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChatWindow.setWindowIcon(icon)
        ChatWindow.setWindowTitle("AR Intercom - Chat Window")

        self.chat_window_layout = QtWidgets.QHBoxLayout()
        self.chat_window_layout.setSpacing(0)
        self.chat_window_layout.setContentsMargins(0, 0, 0, 0)
        
        ChatWindow.setLayout(self.chat_window_layout)

        # Create widgets
        self.left_side()
        self.right_side()

    def left_side(self):
        """
        Create the user's (contacts) widgets
        """
        # CONTAINER
        self.left_container = QtWidgets.QWidget()
        self.left_container.setMinimumSize(QtCore.QSize(150, 250))
        self.left_container.setMaximumWidth(236)
        self.chat_window_layout.addWidget(self.left_container)

        # Layout inside container
        self.layleft = QtWidgets.QVBoxLayout(self.left_container)
        self.layleft.setSpacing(3)
        self.layleft.setContentsMargins(0, 0, 0, 0)

        # WIDGETS______________________________

        # HEADER
        self.chatlist = QtWidgets.QLabel(self.left_container)
        self.chatlist.setMinimumSize(236, 41)
        self.chatlist.setStyleSheet("QLabel{color: rgb(255, 255, 255); background-color: rgb(0, 0, 59);"
                                    "font-size:20px; font-weight:bold; padding-left:10px;}")
        self.chatlist.setText("<p align='left'>Chat list</p>")

        # SCROLL REGION
        # Layout
        self.left_scroll_layout = QtWidgets.QVBoxLayout()
        self.left_scroll_layout.setSpacing(4)
        self.left_scroll_layout.setContentsMargins(0, 0, 0, 0)

        self.spacer = QtWidgets.QSpacerItem(1, 240, vData=QSizePolicy.Policy.Preferred)
        self.left_scroll_layout.addSpacerItem(self.spacer)


        # Scroll widget
        self.left_scroll = QtWidgets.QWidget()
        self.left_scroll.setStyleSheet("QWidget{background-color:rgba(24, 53, 72, 250)}")
        self.left_scroll.setLayout(self.left_scroll_layout)

        # Scroll area
        self.clients_field = QtWidgets.QScrollArea(self.left_container)
        self.clients_field.setMinimumSize(236, 100)
        self.clients_field.setWidgetResizable(True)
        self.clients_field.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.clients_field.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.clients_field.setWidget(self.left_scroll)
        self.clients_field.setStyleSheet(ScrollBar.orange_style)

        # LAYOUT LEFT SIDE
        self.layleft.addWidget(self.chatlist)
        self.layleft.addWidget(self.clients_field)

        # --------------------------------------- Client_frame

    def show_user_widget(self, user, online: bool = False):
        """
        Load users conversation list from users who are registered in database
        """
        uuid = user.get_uuid()
        name = user.get_user_name()
        profile_picture_path = user.get_image_path()

        # FRAME FOR ONE CLIENT
        self.client_info = QtWidgets.QFrame(self.left_scroll)
        self.client_info.setGeometry(QtCore.QRect(0, 0, 236, 60))
        self.client_info.setMinimumSize(QtCore.QSize(236, 60))
        self.client_info.setMaximumSize(QtCore.QSize(236, 60))
        self.client_info.setStyleSheet(Clients.frame_normal)
        self.client_info.setLineWidth(1)

        last_index = self.left_scroll_layout.count() - 1
        self.left_scroll_layout.insertWidget(last_index, self.client_info,
                                             Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignTop)

        # PROFILE PICTURE
        self.client_picture = QtWidgets.QLabel(self.client_info)
        self.client_picture.setGeometry(QtCore.QRect(3, 0, 60, 60))
        rounded_pixmap = utils.create_rounded_image(profile_picture_path, self.client_picture.width())
        self.client_picture.setPixmap(rounded_pixmap)
        self.client_picture.setScaledContents(True)
        self.client_picture.setStyleSheet("border-radius:30px;border:none;")

        # ONLINE TOAST
        self.online_toast = QtWidgets.QLabel(self.client_info)
        self.online_toast.setGeometry(QtCore.QRect(45, 11, 16, 16))
        self.online_toast.setStyleSheet("""QLabel{
                                        border:none;
                                        border-radius:8px;
                                        background-color: #00ff00;}""")
        self.online_toast.setObjectName(f"{uuid}_toast")
        if not online:
            self.online_toast.hide()

        # NAME
        self.client_name = QtWidgets.QPushButton(self.client_info)
        self.client_name.setGeometry(QtCore.QRect(56, 0, 175, 60))
        self.client_name.setStyleSheet("QPushButton{color:#FFF;font-size:20px; text-align:left; padding-left:10px;"
                                       "border:none;background:none;}")
        self.client_name.setText(name)
        self.client_name.setObjectName(uuid)
        self.client_name.clicked.connect(self.show_conversation)

        # MESSAGE COUNTER
        self.msg_counter = QtWidgets.QLabel(self.client_info)
        self.msg_counter.setGeometry(QtCore.QRect(184, 18, 22, 22))
        self.msg_counter.setStyleSheet("QLabel{border-radius:11px; font-weight:bold; text-align:right; color:#ffAa00;"
                                        "border:none; background-color: rgb(0, 0, 59);}")
        self.msg_counter.setText("0")
        self.msg_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.msg_counter.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.msg_counter.setObjectName(f"{uuid}_counter")
        self.msg_counter.hide()

####################################################################################
# THE LEFT SIDE IS DONE,
# LET'S DESIGN THE RIGHT SIDE NOW

    def right_side(self):
        """
        Create the conversation widgets
        """
        # CONTAINER
        self.right_container = QtWidgets.QWidget()
        self.right_container.setMinimumSize(285, 200)
        self.chat_window_layout.addWidget(self.right_container)

        # Layout inside container
        self.layright = QtWidgets.QVBoxLayout(self.right_container)
        self.layright.setSpacing(0)
        self.layright.setContentsMargins(0, 0, 0, 0)

        # WIDGETS______________________________________________________________________
        # HEAD
        self.active_client_bg = QtWidgets.QFrame(self.right_container)
        self.active_client_bg.setMinimumSize(200, 51)
        self.active_client_bg.setMaximumHeight(51)
        self.active_client_bg.setStyleSheet("QFrame{background-color: rgba(0,0,0, 25);"
                                            "background-image: url(:/icons/icons/multilogo.png);"
                                            "background-repeat:repeat-x;}")
        self.layright.addWidget(self.active_client_bg)

        # MASSAGES CONTAINER
        self.create_chat_field()

        # ACTIVE CLIENT NAME
        self.active_client = QtWidgets.QLabel(self.right_container)
        self.active_client.setMinimumSize(80, 41)
        self.active_client.setMaximumHeight(41)
        self.active_client.setStyleSheet("QLabel{color: rgb(255, 255, 255);background: rgb(0, 0, 59);"
                                         "border-radius:20px; border:5px solid;border-color:rgb(0, 0, 59);"
                                         "border-bottom-color: rgb(255, 170, 0);font-size:20px; font-weight:Bold;"
                                         "image:none;}")
        self.active_client.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.active_client.hide()

        # DELETE MESSAGES BUTTON
        self.delete_button = QtWidgets.QPushButton(self.right_container)
        self.delete_button.setFixedSize(31, 31)
        self.delete_button.setStyleSheet("QPushButton{image: url(:/icons/icons/24778-200.png);background:transparent;}"
                                 "QPushButton::hover{background-color:#55FFFFFF;")
        #self.delete_button.clicked.connect(self.delete_message)
        self.delete_button.hide()

        tophlayout = QtWidgets.QHBoxLayout(self.active_client_bg)
        tophlayout.setContentsMargins(5, 10, 5, 0)

        tophlayout.addWidget(self.active_client)
        tophlayout.addStretch()
        tophlayout.addWidget(self.delete_button)

        # MESSAGE TYPING FIELD
        self.create_typing_zone()

    def create_chat_field(self):
        # WIDGET CONTAINING MESSAGES (SCROLL AREA)

        # Layout bubbles's frames
        self.layout_bubble = QtWidgets.QVBoxLayout()
        self.layout_bubble.setSpacing(10)
        self.layout_bubble.setContentsMargins(10, 15, 15, 10)

        spacer = QtWidgets.QSpacerItem(1, 260, vData=QSizePolicy.Policy.Preferred)
        self.layout_bubble.addSpacerItem(spacer)


        # Widget for the scroll area object
        self.right_scroll = QtWidgets.QWidget()
        self.right_scroll.setLayout(self.layout_bubble)

        # Scroll area
        self.chat_field = QtWidgets.QScrollArea(self.right_container)
        self.chat_field.setMinimumSize(200, 30)
        self.chat_field.setWidgetResizable(True)
        self.chat_field.setStyleSheet(ScrollBar.blue_style)
        self.chat_field.setWidget(self.right_scroll)

        self.layright.addWidget(self.chat_field)

    def create_typing_zone(self):

        # CHOOSE MEDIA BUTTON (+) #######################################################
        def change_media_style():
            # CONTROL MEDIA BUTTON STYLE
            if self.media_button.styleSheet() == MediaButton.style_more:
                self.show_media_buttons()

            else:
                self.media_button.setStyleSheet(MediaButton.style_more)
                self.media_bg.deleteLater()

        # button
        self.media_button = QtWidgets.QPushButton(self.right_container)
        self.media_button.setFixedSize(40, 40)
        self.media_button.setStyleSheet(MediaButton.style_more)
        self.media_button.setToolTip("Envoyer un fichier (PRO)")
        self.media_button.clicked.connect(change_media_style)

        ##################################################################

        # TYPE TEXT MESSAGE FIELD
        self.entry_field = QtWidgets.QLineEdit(self.right_container)
        self.entry_field.setMinimumSize(225, 40)
        self.entry_field.setMaximumHeight(40)
        self.entry_field.setStyleSheet("QLineEdit{border:1px solid;padding-left:10px; padding-right:10px;"
                                       "border-color: rgb(0, 85, 255);border-radius:20px; font-size:20px;}"
                                       "QLineEdit:hover{border:2px solid #3385CC;}")
        self.entry_field.setFrame(True)
        self.entry_field.setPlaceholderText("Saisissez votre message ici !")

        # SEND MESSAGE BUTTON
        self.send_button = QtWidgets.QPushButton(self.right_container)
        self.send_button.setFixedSize(40, 40)
        self.send_button.setStyleSheet(SendButton.style_record)

        # Layout bottom widgets
        bottomhlayout = QtWidgets.QHBoxLayout()
        bottomhlayout.setSpacing(5)
        bottomhlayout.setContentsMargins(10, 5, 10, 5)

        bottomhlayout.addWidget(self.media_button)
        bottomhlayout.addWidget(self.entry_field)
        bottomhlayout.addWidget(self.send_button)

        self.layright.addLayout(bottomhlayout)

    def show_media_buttons(self):
        # LAYOUT
        self.media_layout = QtWidgets.QHBoxLayout()
        self.media_layout.setSpacing(2)
        self.media_layout.setContentsMargins(0, 0, 0, 0)

        # BACKGROUND
        self.media_bg = QtWidgets.QWidget(self.right_container)
        self.media_bg.setMinimumSize(168, 41)
        self.media_bg.move(self.media_button.x(), self.media_button.y() - 50)
        self.media_bg.setStyleSheet("QWidget{border-radius:20px; background-color: rgba(90, 162, 255, 90);}")
        self.media_bg.setLayout(self.media_layout)
        self.media_bg.show()

        # IMAGE BUTTON
        self.media_image = QtWidgets.QPushButton(self.media_bg)
        self.media_image.setMinimumSize(QtCore.QSize(40, 40))
        self.media_image.setStyleSheet("QPushButton{image: url(:/icons/icons/photo.png);border-radius:20px;}"
                                       "QPushButton:hover{border:1px solid #3385CC;}")
        self.media_image.setToolTip("Envoyer une image (PRO)")
        self.media_layout.addWidget(self.media_image)

        # MUSIC BUTTON
        self.media_music = QtWidgets.QPushButton(self.media_bg)
        self.media_music.setMinimumSize(QtCore.QSize(40, 40))
        self.media_music.setStyleSheet("QPushButton{image: url(:/icons/icons/song.png);border-radius:20px;}"
                                       "QPushButton:hover{border:1px solid #3385CC;}")
        self.media_music.setToolTip("Envoyer une musique (PRO)")
        self.media_layout.addWidget(self.media_music)

        # VIDEO BUTTON
        self.media_video = QtWidgets.QPushButton(self.media_bg)
        self.media_video.setMinimumSize(QtCore.QSize(40, 40))
        self.media_video.setStyleSheet("QPushButton{image: url(:/icons/icons/video.png);border-radius:20px;}"
                                       "QPushButton:hover{border:1px solid #3385CC;}")
        self.media_video.setToolTip("Envoyer une vidéo (PRO)")
        self.media_layout.addWidget(self.media_video)

        # DOCUMENT BUTTON
        self.media_doc = QtWidgets.QPushButton(self.media_bg)
        self.media_doc.setMinimumSize(QtCore.QSize(40, 40))
        self.media_doc.setStyleSheet("QPushButton{image: url(:/icons/icons/document.png);border-radius:20px;}"
                                     "QPushButton:hover{border:1px solid #3385CC;}")
        self.media_doc.setToolTip("Envoyer un document (PRO)")
        self.media_layout.addWidget(self.media_doc)

        self.media_button.setStyleSheet(MediaButton.style_less)

    def create_left_bubble(self, message: Message):

        # GRID LAYOUT
        self.left_msg_layout = QtWidgets.QGridLayout()
        self.left_msg_layout.setContentsMargins(0, 0, 0, 0)
        self.left_msg_layout.setHorizontalSpacing(0)
        self.left_msg_layout.setVerticalSpacing(3)

        # LEFT MESSAGE FRAME
        self.l_bubble_container = QtWidgets.QWidget()
        self.l_bubble_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.l_bubble_container.setLayout(self.left_msg_layout)

        self.layout_bubble.addWidget(self.l_bubble_container, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)

        # Small left bubble
        self.l_bubble = QtWidgets.QFrame()
        self.l_bubble.setFixedSize(16, 16)
        self.l_bubble.setStyleSheet("background-color: rgb(255, 170, 0);border-radius:7px;")
        self.left_msg_layout.addWidget(self.l_bubble, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        if message.get_kind() == "text":
            # LAYOUT MESSAGE

            # Left text container
            self.left_bubble = QtWidgets.QLabel()
            self.left_bubble.setMaximumWidth(304)
            self.left_bubble.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            self.left_bubble.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse |
                                                     Qt.TextInteractionFlag.TextSelectableByKeyboard)
            self.left_bubble.setCursor(Qt.CursorShape.IBeamCursor)
            self.left_bubble.setText(message.get_body())
            self.left_bubble.setWordWrap(True)
            self.left_bubble.setStyleSheet("border-radius:13px; color: rgb(0, 0, 0);background-color: rgb(255, 170, 0);"
                                           "padding-left:10px;padding-right:10px;padding-top:5px;padding-bottom:5px;"
                                           "font-size:16px;")
            self.left_msg_layout.addWidget(self.left_bubble, 0, 1, 1, 1)

        else:
            # CREATE THE MEDIA PARENT WIDGET
            self.left_media_parent = QtWidgets.QWidget()
            self.left_media_parent.setFixedSize(304, 73)
            self.left_media_parent.setStyleSheet("QWidget{border-radius:15px;"
                                                 "background-color: rgb(255, 170, 0);}")
            self.left_msg_layout.addWidget(self.left_media_parent, 0, 1, 1, 1)

            # CREATE BUBBLE
            if message.get_kind() == "voice":
                self.create_voice_bubble(self.left_media_parent, message.get_body())

            elif message.get_kind() == "video":
                pass

            elif message.get_kind() == "audio":
                pass

            elif message.get_kind() == "image":
                pass

            elif message.get_kind() == "document":
                pass

        # Left time bubble
        self.left_time = QtWidgets.QLabel()
        self.left_time.setFixedSize(96, 16)
        self.left_time.setText(f"<p align='center'>{message.get_created_at()}</p>")
        self.left_time.setStyleSheet("QLabel{border-radius:8px; color:#000000; background-color:#C5C5C5;"
                                     "font-size:10px;}")
        self.left_msg_layout.addWidget(self.left_time, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        # UPDATE SCROLL BAR
        QtCore.QTimer.singleShot(10, self.scroll_to_end)
        QtCore.QTimer.singleShot(1000, self.scroll_to_end)

    def create_right_bubble(self, message: Message):

        # GRID LAYOUT
        self.right_msg_layout = QtWidgets.QGridLayout()
        self.right_msg_layout.setContentsMargins(0, 0, 0, 0)
        self.right_msg_layout.setHorizontalSpacing(0)
        self.right_msg_layout.setVerticalSpacing(3)

        # RIGHT MESSAGE WIDGET (BUBBLE AND TIME CONTAINER)
        self.r_bubble_container = QtWidgets.QWidget()
        self.r_bubble_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.r_bubble_container.setLayout(self.right_msg_layout)
        self.r_bubble_container.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.r_bubble_container.setStyleSheet("background-color:99000000")

        self.layout_bubble.addWidget(self.r_bubble_container, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignBottom)

        # Small right bubble (design)
        self.r_bubble = QtWidgets.QFrame()
        self.r_bubble.setFixedSize(QtCore.QSize(16, 16))
        self.r_bubble.setStyleSheet("background-color:#3385CC; border-radius:8px;")
        self.right_msg_layout.addWidget(self.r_bubble, 0, 0, 1, 1, Qt.AlignmentFlag.AlignBottom)

        # CREATE TEXT MESSAGE, OR MEDIA BUBBLE
        if message.get_kind() == "text":
            # Right text container
            self.right_bubble = QtWidgets.QLabel()
            self.right_bubble.setMaximumWidth(304)
            self.right_bubble.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            self.right_bubble.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse |
                                                      Qt.TextInteractionFlag.TextSelectableByKeyboard)
            self.right_bubble.setCursor(Qt.CursorShape.IBeamCursor)
            self.right_bubble.setText(message.get_body())
            self.right_bubble.setWordWrap(True)
            self.right_bubble.setStyleSheet("QLabel{border-radius:15px;color: rgb(255, 255, 255);"
                                            "background-color: #3385CC;padding:10px;font-size:16px;}")
            self.right_bubble.setObjectName(f"body_{message.get_id()}")
            self.right_msg_layout.addWidget(self.right_bubble, 0, 1, 1, 1)

        else:
            # CREATE THE MEDIA PARENT WIDGET
            # Set layout to the right bubble to prevent reversed progressbar
            ly = QtWidgets.QHBoxLayout()
            ly.setContentsMargins(0, 0, 0, 0)

            self.right_media_parent = QtWidgets.QWidget()
            self.right_media_parent.setFixedSize(304, 73)
            self.right_media_parent.setStyleSheet("QWidget{border-radius:15px;"
                                            "background-color: #3385CC;}")
            self.right_media_parent.setLayout(ly)
            self.right_media_parent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

            self.right_msg_layout.addWidget(self.right_media_parent, 0, 1, 1, 1)

            # CREATE MEDIA BUBBLE
            if message.get_kind() == "voice":
                self.create_voice_bubble(self.right_media_parent, message.get_body())

            elif message.get_kind() == "video":
                pass

            elif message.get_kind() == "audio":
                pass

            elif message.get_kind() == "image":
                pass

            elif message.get_kind() == "document":
                pass

        # Right time
        self.right_time = QtWidgets.QLabel()
        self.right_time.setFixedSize(96, 16)
        self.right_time.setText(f"<p align='center'>{message.get_created_at()}</p>")
        self.right_time.setStyleSheet("QLabel{border-radius:8px;color:#000000; background-color:#C5C5C5;"
                                      "font-size:10px;}")
        self.right_msg_layout.addWidget(self.right_time, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        # SHOW MESSAGE STATUS INDICATOR
        self.message_status = QtWidgets.QPushButton()
        self.message_status.setFixedSize(16, 16)

        if message.get_status():
            self.message_status.setStyleSheet(MessageStatus.style_sent)
            self.message_status.setObjectName(f"success_{message.get_id()}")
        else:
            self.message_status.setStyleSheet(MessageStatus.style_not_sent)
            self.message_status.setToolTip("Cliquez pour renvoyer le message")
            self.message_status.setObjectName(f"error_{message.get_id()}")

        self.right_msg_layout.addWidget(self.message_status, 1, 1, 1, 0)

        # UPDATE SCROLL BAR
        QtCore.QTimer.singleShot(10, self.scroll_to_end)
        QtCore.QTimer.singleShot(1000, self.scroll_to_end)

    def scroll_to_end(self):
        # SCROLL TO END
        self.scroll_bar = self.chat_field.verticalScrollBar()
        self.scroll_bar.setValue(self.scroll_bar.maximum())

    def show_record_widget(self):
        # Frame
        self.record_tip = QtWidgets.QFrame(self.right_container)
        self.record_tip.setFixedSize(161, 31)
        self.record_tip.move(self.send_button.x() - 160, self.send_button.y()+5)
        self.record_tip.setStyleSheet("QFrame{background-color:#FFFFFF;border-radius:15px;}")
        self.record_tip.show()

        # Confirm end or record
        self.end_record = QtWidgets.QPushButton(self.record_tip)
        self.end_record.setGeometry(QtCore.QRect(10, 5, 31, 20))
        self.end_record.setToolTip("Finir l'enregistrement (PRO)")
        self.end_record.setStyleSheet("""QPushButton{background:#00FF00; border-top-left-radius:10px;
                                                    border-bottom-left-radius:10px;
                                                    image:url(:/cils/cils/cil-media-record-bl.png);}
                                        QPushButton:hover{background:#00DD00}""")
        self.end_record.show()

        # Time indicator
        self.record_time = QtWidgets.QLabel(self.record_tip)
        self.record_time.setGeometry(QtCore.QRect(45, 5, 71, 20))
        self.record_time.setStyleSheet("QLabel{background:grey; color:white; border-radius:none;}")
        self.record_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.record_time.setText("00:00")
        self.record_time.show()

        # Cancel record
        self.cancel_record = QtWidgets.QPushButton(self.record_tip)
        self.cancel_record.setGeometry(QtCore.QRect(119, 5, 31, 20))
        self.cancel_record.setToolTip("Annuler l'enregistrement (PRO)")
        self.cancel_record.setStyleSheet("""QPushButton{background:#FF0000;border-top-right-radius:10px;
                                                        border-bottom-right-radius:10px;
                                                        image:url(:/cils/cils/cil-media-stop-bl.png);}
                                        QPushButton:hover{background:#DD0000;}""")
        self.cancel_record.show()

    def create_voice_bubble(self, parent, path: str):
        file_name = os.path.splitext(os.path.split(path)[1])[0] + ".arv"

        # Frame
        self.voice_bubble = QtWidgets.QFrame(parent)
        self.voice_bubble.setGeometry(QtCore.QRect(2, 2, 300, 69))
        self.voice_bubble.setStyleSheet("QFrame{background-color:#88FFFFFF; border-radius:10px;}")

        # Title
        self.title = QtWidgets.QLabel(self.voice_bubble)
        self.title.setGeometry(QtCore.QRect(52, 3, 241, 20))
        self.title.setStyleSheet("QLabel{background:#44FFFFFF;}")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setText(file_name)
        self.title.setObjectName(f"path|{path}")

        # Slider
        self.slider = QtWidgets.QSlider(self.voice_bubble)
        self.slider.setGeometry(QtCore.QRect(52, 30, 241, 12))
        self.slider.setStyleSheet(Slider.slider)
        self.slider.setMaximum(100)
        self.slider.setValue(0)
        # self.slider.setSliderPosition(0)
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        # Elapsed time
        self.elapsed_time = QtWidgets.QLabel(self.voice_bubble)
        self.elapsed_time.setGeometry(QtCore.QRect(52, 49, 51, 16))
        self.elapsed_time.setStyleSheet("QLabel{background:#22FFFFFF; border-radius:8px;}")
        self.elapsed_time.setText("00:00")
        self.elapsed_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.elapsed_time.setObjectName("elapsed_time")

        # Total time
        self.total_time = QtWidgets.QLabel(self.voice_bubble)
        self.total_time.setGeometry(QtCore.QRect(241, 49, 51, 16))
        self.total_time.setStyleSheet("QLabel{background:#22FFFFFF; border-radius:8px;}")
        self.total_time.setText("--:--")
        self.total_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.total_time.setObjectName("total_time")

        # Play button
        self.play_button = QtWidgets.QPushButton(self.voice_bubble)
        self.play_button.setGeometry(QtCore.QRect(7, 12, 41, 41))
        self.play_button.setStyleSheet(Player.play)
        # self.play_button.setObjectName("stopped")
        self.play_button.clicked.connect(self.play)

    def play(self):
        button = self.sender()
        self.playButtonPressed.emit(button)

    def show_conversation(self):
        button = self.sender()
        self.conversationButtonPressed.emit(button.objectName())