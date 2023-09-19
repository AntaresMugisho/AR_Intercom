# -*- This python file uses the following encoding : utf-8 -*-

from datetime import datetime


from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, QSpacerItem
from PySide6.QtGui import QFont, QCursor    
from PySide6.QtCore import QSize, Qt, QRect

from message import Message
import utils


class Bubble(QWidget):

    STRING_FORMAT_TIME = "%H:%M"

    def __init__(self, message: Message, position: str):
        QWidget.__init__(self)
        # self.setObjectName(u"bubble_container_widget")

        self.message = message
        self.position = position

        self.message_kind = self.message.get_kind()
        self.message_body = self.message.get_body()
        self.message_time = datetime.strftime(self.message.get_created_at(), self.STRING_FORMAT_TIME)
        self.message_received = self.message.get_status()

        if self.position == "left":
            self.show_left_bubble()
        else:
            # show_right_bubble()
            pass

    def show_left_bubble(self):
        if self.message_kind == "text":
            self.text()
        elif self.message_kind == "voice":
            pass
        elif self.message_kind == "video":
            pass

        elif self.message_kind == "audio":
            pass

        elif self.message_kind == "image":
            pass

        elif self.message_kind == "document":
            pass

    def text(self):
        print("Text Label")
        font4 = QFont()
        font4.setPointSize(12)

        font5 = QFont()
        font5.setPointSize(8)

        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        # sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())

        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        # sizePolicy2.setHeightForWidth(self.left_bubble_3.sizePolicy().hasHeightForWidth())
        self.bubble_container_widget = QWidget(self)
        self.bubble_container_widget.setObjectName(u"bubble_container_widget")
        self.bubble_container_widget.setStyleSheet(u"")

        self.horizontalLayout_11 = QHBoxLayout(self.bubble_container_widget)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)


        # Labels container
        self.left_msg_frame = QFrame(self)
        self.left_msg_frame.setObjectName(u"left_msg_frame")
        self.left_msg_frame.setMinimumSize(QSize(120, 71))
        self.left_msg_frame.setStyleSheet(u"")
        self.left_msg_frame.setFrameShape(QFrame.StyledPanel)
        self.left_msg_frame.setFrameShadow(QFrame.Raised)

        # Small decorators
        self.frame = QFrame(self.left_msg_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 14, 14))
        self.frame.setStyleSheet(u"\n"
                                 "background-color: rgba(40, 40, 43, 0.7);\n"
                                 "border-radius:7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.frame_2 = QFrame(self.left_msg_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(5, 4, 8, 8))
        self.frame_2.setStyleSheet(u"background-color: rgb(40, 40, 43);\n"
                                   "border-radius:4px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        # Background
        self.bubble = QFrame(self.left_msg_frame)
        self.bubble.setObjectName(u"bubble")
        self.bubble.setGeometry(QRect(17, 17, 92, 51))
        sizePolicy1.setHeightForWidth(self.bubble.sizePolicy().hasHeightForWidth())
        self.bubble.setSizePolicy(sizePolicy1)
        self.bubble.setStyleSheet(u"	border-radius:20px;\n"
                                  "	border-top-left-radius:8px;\n"
                                  "	background-color: rgb(255, 170, 0);\n"
                                  "	background-color: rgb(40, 40, 43);\n"
                                  "")
        self.bubble.setFrameShape(QFrame.StyledPanel)
        self.bubble.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22 = QVBoxLayout(self.bubble)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(12, 6, 12, 0)

        # Message Label
        self.message_label = QLabel(self.bubble)
        self.message_label.setObjectName(u"message_label")
        sizePolicy2.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy2)
        self.message_label.setMaximumSize(QSize(304, 16777215))
        self.message_label.setFont(font4)
        self.message_label.setStyleSheet(u"QLabel{\n"
                                         "	color: #ddd;\n"
                                         "background-color:transparent;\n"
                                         "}")
        self.message_label.setScaledContents(False)
        self.message_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.message_label.setWordWrap(True)
        self.message_label.setTextInteractionFlags(
            Qt.LinksAccessibleByKeyboard | Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
        self.message_label.setText(self.message_body)
        self.verticalLayout_22.addWidget(self.message_label)

        # Time label
        self.time_label_layout = QHBoxLayout()
        self.time_label_layout.setSpacing(0)
        self.time_label_layout.setObjectName(u"time_label_layout")
        self.time_label_spacer = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.time_label_layout.addItem(self.time_label_spacer)

        self.time_label = QLabel(self.bubble)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(31, 14))
        self.time_label.setMaximumSize(QSize(31, 14))
        self.time_label.setFont(font5)
        self.time_label.setStyleSheet(u"QLabel{\n"
                                      "color:#555;\n"
                                      "border-radius:7px;\n"
                                      "}")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setText(self.message_time)

        self.time_label_layout.addWidget(self.time_label)

        self.verticalLayout_22.addLayout(self.time_label_layout)


        self.horizontalLayout_11.addWidget(self.left_msg_frame)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.spacer)
