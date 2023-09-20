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

        self.message = message
        self.position = position
        self.on_left = self.position == "left"

        self.message_kind = self.message.get_kind()
        self.message_body = self.message.get_body()
        self.message_time = datetime.strftime(self.message.get_created_at(), self.STRING_FORMAT_TIME)
        self.message_received = self.message.get_status()

        self.show_bubble()


    def show_bubble(self):
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
        """
        Create text message bubble
        """

        font12 = QFont()
        font12.setPointSize(12)

        font8 = QFont()
        font8.setPointSize(8)

        font7 = QFont()
        font7.setPointSize(7)

        self.horizontalLayout_11 = QHBoxLayout(self)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)

        # Labels container
        self.bubble_frame = QFrame(self)
        self.bubble_frame.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.bubble_frame.setMinimumSize(QSize(300, 71))
        self.bubble_frame.setMaximumWidth(300)
        self.bubble_frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)


        # Small decoration frames
        self.frame = QFrame(self.bubble_frame)
        if self.on_left:
            self.frame.setGeometry(QRect(10, 10, 14, 14))
            self.frame.setStyleSheet(u"background-color: rgba(40, 40, 43, 0.7);border-radius:7px;")
        else:
            self.frame.setGeometry(QRect(134, 8, 14, 14))
            self.frame.setStyleSheet(u"background-color: rgba(14, 14, 15, 0.7);border-radius:7px;")

        self.frame_2 = QFrame(self.bubble_frame)
        if self.on_left:
            self.frame_2.setGeometry(QRect(5, 4, 8, 8))
            self.frame_2.setStyleSheet(u"background-color: rgb(40, 40, 43);border-radius:4px;")
        else:
            self.frame_2.setGeometry(QRect(145, 2, 8, 8))
            self.frame_2.setStyleSheet(u"background-color: rgb(14, 14, 15);border-radius:4px;")


        # Bubble : background
        self.bubble = QFrame(self.bubble_frame)
        self.bubble.move(17, 17)

        left_style = u"border-radius:20px;border-top-left-radius:8px;background-color: rgb(40, 40, 43);"
        right_style = u"border-radius:20px;border-top-right-radius:8px;background-color: rgb(14, 14, 15);"

        if self.on_left:
            self.bubble.setStyleSheet(left_style)
        else:
            # self.bubble.move(self.bubble_frame.width() + self.bubble.width(), 17)
            self.bubble.setStyleSheet(right_style)

        self.verticalLayout_22 = QVBoxLayout(self.bubble)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(12, 6, 12, 0)

        # Message Label
        self.message_label = QLabel(self.bubble)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setMaximumWidth(300)
        self.message_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.message_label.setFont(font12)
        if self.on_left:
            self.message_label.setStyleSheet(u"QLabel{color: #ccc;background-color:transparent;}")
        else:
            self.message_label.setStyleSheet(u"QLabel{color: #eee;background-color:transparent;}")

        # self.message_label.setScaledContents(False)
        self.message_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.message_label.setWordWrap(True)
        self.message_label.setTextInteractionFlags(
            Qt.LinksAccessibleByKeyboard | Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
        self.message_label.setText(self.message_body)

        self.verticalLayout_22.addWidget(self.message_label)

        # Time label
        self.time_label_layout = QHBoxLayout()
        self.time_label_layout.setSpacing(3)

        self.time_label_spacer = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.time_label_layout.addItem(self.time_label_spacer)

        self.time_label = QLabel(self.bubble)
        self.time_label.setFixedSize(QSize(31, 14))
        self.time_label.setFont(font8)
        self.time_label.setStyleSheet(u"QLabel{color:#555;border-radius:7px;}")
        self.time_label.setText(self.message_time)

        self.time_label_layout.addWidget(self.time_label)

        if not self.on_left:
            self.ticks = QLabel(self.bubble)
            self.ticks.setFixedSize(QSize(24, 14))
            self.ticks.setFont(font7)
            self.ticks.setStyleSheet(u"image: url(:/cils/cils/cil-check-circle-green.png);\n"
                                     "background-color:rgba(255,255,255,0.1);border-radius:7px;padding:1px;")
            self.time_label_layout.addWidget(self.ticks)

        self.verticalLayout_22.addLayout(self.time_label_layout)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        if self.on_left:
            self.horizontalLayout_11.addWidget(self.bubble_frame)
            self.horizontalLayout_11.addItem(self.spacer)
        else:
            self.horizontalLayout_11.addItem(self.spacer)
            self.horizontalLayout_11.addWidget(self.bubble_frame, Qt.AlignmentFlag.AlignRight, Qt.AlignmentFlag.AlignVCenter)
