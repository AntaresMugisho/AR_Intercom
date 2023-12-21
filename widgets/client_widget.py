# -*- This python file uses the following encoding : utf-8 -*-
import os.path

from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton
from PySide6.QtGui import QFont, QCursor, QMouseEvent
from PySide6.QtCore import QSize, Qt, QRect, Signal

from message import Message
from user import User
import utils


class ClientWidget(QFrame):

    clicked = Signal(str)
    released = Signal(str)

    def __init__(self, user: User, online: bool = False):
        QFrame.__init__(self)

        self.user = user
        self.online = online

        # GET USER INFORMATION
        self.user_uuid = self.user.get_uuid()
        self.username = self.user.get_user_name()
        self.user_profile_picture_path = user.get_image_path()

        if self.user_profile_picture_path == "user/default.png":
            self.user_profile_picture_path = ":/icons/icons/avatar.png"

        self.messages = self.user.messages()

        # DRAW USER WIDGET
        self.setObjectName(f"{self.user_uuid}")
        self.setMinimumSize(QSize(271, 61))
        self.setMaximumSize(QSize(271, 61))
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(u"QFrame{\n"
            "	border-radius:8px;\n"
            "	background-color: rgba(50, 50, 50, 50);\n"
            "}\n"
            "\n"
            "QFrame:hover{\n"
            "	background-color: rgba(50, 50, 50, 255);\n"
            "}\n"
            "")

        self.setup_ui()

    def setup_ui(self):
        font = QFont()
        font.setPointSize(10)

        # PROFILE PICTURE
        self.client_picture = QLabel(self)
        self.client_picture.setObjectName(u"client_picture")
        self.client_picture.setGeometry(QRect(3, 3, 56, 56))
        self.client_picture.setStyleSheet("border-radius:28px;border:none;")

        # Create rounded pixmap
        rounded_pixmap = utils.create_rounded_image(self.user_profile_picture_path, self.client_picture.width())
        self.client_picture.setPixmap(rounded_pixmap)
        self.client_picture.setScaledContents(True)


        # UNREAD MESSAGE COUNTER
        self.msg_countrer = QLabel(self)
        self.msg_countrer.setObjectName(f"{self.user_uuid}_counter")
        self.msg_countrer.setGeometry(QRect(243, 7, 16, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(False)
        self.msg_countrer.setFont(font3)
        self.msg_countrer.setStyleSheet(u"QLabel{border-radius:8px;color: white;background-color: red;}")
        self.msg_countrer.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.msg_countrer.hide()

        # ONLINE TOAST
        self.online_toast = QLabel(self)
        self.online_toast.setObjectName(f"{self.user_uuid}_toast")
        self.online_toast.setGeometry(QRect(47, 41, 12, 12))
        self.online_toast.setStyleSheet(u"QLabel{\n"
                                        "	border-radius:6px;\n"
                                        "	border:2px solid rgb(20,20,20);\n"
                                        "	background-color: #00FF00;	\n"
                                        "}")
        # if not
        if self.online:
            self.online_toast.hide()

        # LAST SEEN
        self.last_seen_0 = QLabel(self)
        self.last_seen_0.setObjectName(u"last_seen_0")
        self.last_seen_0.setGeometry(QRect(198, 39, 61, 20))
        color = "#009900" if self.online else "#555"
        self.last_seen_0.setStyleSheet(u"QLabel{\n"
                                       "	background-color:transparent;\n"
                                       f"	color:{color};\n"
                                       "}")
        self.last_seen_0.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        if self.online:
            self.last_seen_0.setText("online")
        else:
            self.last_seen_0.setText("offline")

        # NAME
        self.client_name = QLabel(self)
        self.client_name.setGeometry(QRect(70, 6, 131, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.client_name.setFont(font4)
        self.client_name.setStyleSheet(u"QLabel{\n"
                                       "	background-color:none;\n"
                                       "	color: white;\n"
                                       "}")
        self.client_name.setText(self.username)

        # LAST MESSAGE
        self.last_message = QLabel(self)
        self.last_message.setObjectName(u"last_message")
        self.last_message.setGeometry(QRect(70, 36, 131, 20))
        self.last_message.setFont(font)
        self.last_message.setStyleSheet(u"QLabel{\n"
                                        "	background-color:transparent;\n"
                                        "	color:rgba(255, 255, 255, 0.5);\n"
                                        "}")
        last_message: Message = self.messages[-1]
        if last_message.get_kind() == "text":
            last_message_text = last_message.get_body()
        else:
            last_message_text = os.path.basename(last_message.get_body())

        self.last_message.setText(last_message_text if len(last_message_text) <= 23 else f"{last_message_text[:20]}...")

        # MESSAGE COUNTER
        self.messege_number = QLabel(self)
        self.messege_number.setGeometry(QRect(213, 23, 30, 20))
        self.messege_number.setText(str(len(self.messages)))
        font5 = QFont()
        font5.setPointSize(8)
        self.messege_number.setFont(font5)
        self.messege_number.setStyleSheet(u"QLabel{\n"
                                          "	background-color:transparent;\n"
                                          "	color:rgba(255, 255, 255, 0.6);\n"
                                          "\n"
                                          "}")
        self.messege_number.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        # ENVELOP ICON
        self.envelop_msg = QFrame(self)
        self.envelop_msg.setObjectName(u"envelop_msg")
        self.envelop_msg.setGeometry(QRect(247, 27, 12, 12))
        self.envelop_msg.setStyleSheet(u"QFrame{\n"
                                       "	background-color:transparent;\n"
                                       "	image: url(:/cils/cils/cil-envelope-closed.png);\n"
                                       "	border:none;}")

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.objectName())

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.released.emit(self.objectName())
