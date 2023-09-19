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
        self.setObjectName(u"bubble_container_widget")

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
        font4 = QFont()
        font4.setPointSize(12)

        font5 = QFont()
        font5.setPointSize(8)

        font8 = QFont()
        font8.setPointSize(7)

        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        # sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())

        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        # sizePolicy2.setHeightForWidth(self.left_bubble_3.sizePolicy().hasHeightForWidth())


        self.horizontalLayout_11 = QHBoxLayout(self)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)


        # Labels container
        self.bubble_frame = QWidget(self)
        self.bubble_frame.setObjectName(u"bubble_frame")
        self.bubble_frame.setMinimumSize(QSize(120, 71))
        # self.bubble_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.bubble_frame.setStyleSheet(u"background-color:rgba(255,255,255,0.1);")
        # self.bubble_frame.setFrameShape(QFrame.StyledPanel)
        # self.bubble_frame.setFrameShadow(QFrame.Raised)

        # Small decoration frames
        self.frame = QFrame(self.bubble_frame)
        self.frame.setObjectName(u"frame")
        if self.on_left:
            self.frame.setGeometry(QRect(10, 10, 14, 14))
            self.frame.setStyleSheet(u"background-color: rgba(40, 40, 43, 0.7);border-radius:7px;")
        else:
            self.frame.setGeometry(QRect(96, 8, 14, 14))
            self.frame.setStyleSheet(u"background-color: rgba(14, 14, 15, 0.7);border-radius:7px;")



        self.frame_2 = QFrame(self.bubble_frame)
        self.frame_2.setObjectName(u"frame_2")
        if self.on_left:
            self.frame_2.setGeometry(QRect(5, 4, 8, 8))
            self.frame_2.setStyleSheet(u"background-color: rgb(40, 40, 43);border-radius:4px;")
        else:
            self.frame_2.setGeometry(QRect(107, 2, 8, 8))
            self.frame_2.setStyleSheet(u"background-color: rgb(14, 14, 15);border-radius:4px;")


        left_style = u"border-radius:20px;border-top-left-radius:8px;background-color: rgb(40, 40, 43);"
        right_style = u"border-radius:20px;border-top-right-radius:8px;background-color: rgb(14, 14, 15);"

        # Bubble : background
        self.bubble = QFrame(self.bubble_frame)
        self.bubble.setObjectName(u"bubble")
        # self.bubble.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.bubble.setGeometry(QRect(17, 17, 92, 51))

        if self.on_left:
            self.bubble.setStyleSheet(left_style)
        else:
            self.bubble.setStyleSheet(right_style)


        self.bubble.setFrameShape(QFrame.StyledPanel)
        self.bubble.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22 = QVBoxLayout(self.bubble)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(12, 6, 12, 0)

        # Message Label
        self.message_label = QLabel(self.bubble)
        self.message_label.setObjectName(u"message_label")
        # sizePolicy2.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        # self.message_label.setSizePolicy(sizePolicy2)
        self.message_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        self.message_label.setMaximumWidth(304)
        self.message_label.setFont(font4)
        if self.on_left:
            self.message_label.setStyleSheet(u"QLabel{color: #ccc;background-color:transparent;}")
        else:
            self.message_label.setStyleSheet(u"QLabel{color: #eee;background-color:transparent;}")

        self.message_label.setScaledContents(False)
        self.message_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.message_label.setWordWrap(True)
        self.message_label.setTextInteractionFlags(
            Qt.LinksAccessibleByKeyboard | Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
        self.message_label.setText(self.message_body)

        self.verticalLayout_22.addWidget(self.message_label)

        # Time label
        self.time_label_layout = QHBoxLayout()
        self.time_label_layout.setSpacing(3)
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
        if not self.on_left :
            self.ticks = QLabel(self.bubble)
            self.ticks.setObjectName(u"ticks")
            self.ticks.setMinimumSize(QSize(24, 14))
            self.ticks.setMaximumSize(QSize(24, 14))
            self.ticks.setFont(font8)
            self.ticks.setStyleSheet(u"\n"
                                       "image: url(:/cils/cils/cil-check-circle-green.png);\n"
                                       "background-color:rgba(255,255,255,0.1);\n"
                                       "border-radius:7px;\n"
                                       "padding:1px;")
            self.ticks.setAlignment(Qt.AlignCenter)

            self.time_label_layout.addWidget(self.ticks)


        self.verticalLayout_22.addLayout(self.time_label_layout)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        if self.on_left:
            self.horizontalLayout_11.addWidget(self.bubble_frame)
            self.horizontalLayout_11.addItem(self.spacer)
        else:
            self.horizontalLayout_11.addItem(self.spacer)
            self.horizontalLayout_11.addWidget(self.bubble_frame)
