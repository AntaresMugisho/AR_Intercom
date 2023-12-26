

from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont, QCursor, QMouseEvent, QPixmap
from PySide6.QtCore import QSize, Qt, QRect, Signal


class ScanResult(QFrame):

    addUser = Signal(str)

    def __init__(self, host_name, host_address):
        QFrame.__init__(self)
        self.host_name = host_name
        self.host_address = host_address

        self.setObjectName(u"socket_info")
        self.setMinimumSize(QSize(0, 42))
        self.setMaximumSize(QSize(16777215, 42))
        self.setStyleSheet("QFrame {background-color:rgb(16, 17, 18);border-radius:21px;}")

    def setup_ui(self):
        self.horizontalLayout_4 = QHBoxLayout(self)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 1, 0, 1)

        self.device_icon = QLabel(self)
        self.device_icon.setObjectName(u"device_icon")
        self.device_icon.setMinimumSize(QSize(40, 40))
        self.device_icon.setMaximumSize(QSize(40, 40))
        self.device_icon.setStyleSheet("{background-color:rgb(30, 32, 33);"
                                       "background-image: url(:/cils/cils/cil-screen-desktop.png);\n"
                                       "	background-repeat:no-repeat;"
                                       "	background-position:center;"
                                       "	border-top-left-radius:20px;"
                                       "	border-bottom-left-radius:20px;"
                                       "}")
        self.device_icon.setPixmap(QPixmap(u":/image/1.png"))
        self.device_icon.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.device_icon)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")


        self.host_name = QLabel(self)
        self.host_name.setObjectName(u"host_name")
        self.host_name.setStyleSheet(u"padding-left:5px;"
                                     u"background-color:rgb(30, 32, 33);")

        self.verticalLayout_3.addWidget(self.host_name)

        self.host_address = QLabel(self)
        self.host_address.setObjectName(u"host_address")
        self.host_address.setStyleSheet(u"color:gray;"
                                        u"padding-left:5px;"
                                        u"background-color:rgb(30, 32, 33);"
                                        )
        self.host_address.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.host_address)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.add_to_contact_btn = QPushButton(self)
        self.add_to_contact_btn.setObjectName(u"add_to_contact_btn")
        self.add_to_contact_btn.setMinimumSize(QSize(40, 40))
        self.add_to_contact_btn.setMaximumSize(QSize(40, 40))
        self.add_to_contact_btn.setStyleSheet("QPushButton{"
                                              "background-image: url(:/cils/cils/cil-user-follow.png);"
                                              "background-color:rgb(30, 32, 33);"
                                              "background-repeat:no-repeat;"
                                              "background-position:center;"
                                              "border-top-right-radius:20px;"
                                              "border-bottom-right-radius:20px;}"
                                       "QPushButton:hover{\n"
                                       "	background-color:rgb(56, 57, 58);}\n"
                                       "\n"
                                       "#QPushButton:pressed{\n"
                                       "	background-color:rgb(27, 28, 29);}"
                                              "")
        self.add_to_contact_btn.clicked.connect(lambda: ScanResult.addUser.emit(self.host_address))

        self.horizontalLayout_4.addWidget(self.add_to_contact_btn)


