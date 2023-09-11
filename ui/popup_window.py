# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)
from resources import img_rc

class Ui_NotificationWidget(object):
    def setupUi(self, NotificationWidget):
        if not NotificationWidget.objectName():
            NotificationWidget.setObjectName(u"NotificationWidget")
        NotificationWidget.resize(340, 105)
        self.global_frame = QFrame(NotificationWidget)
        self.global_frame.setObjectName(u"global_frame")
        self.global_frame.setGeometry(QRect(5, 11, 331, 81))
        self.global_frame.setStyleSheet(u"#global_frame{\n"
"	outline:none;\n"
"	background-color: rgb(200, 211, 211);\n"
"	background-color: rgba(255, 255, 127, 100);\n"
"	border-radius:10px;\n"
"	border:1px solid  rgba(255, 0, 0, 100);\n"
"}")
        self.global_frame.setFrameShape(QFrame.StyledPanel)
        self.global_frame.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.global_frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(80, 12, 241, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"}")
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.logo = QPushButton(self.global_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 13, 61, 51))
        self.logo.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/icons/ARsoftlogo.png);\n"
"	border:none;\n"
"}")
        self.sender_name = QLabel(self.global_frame)
        self.sender_name.setObjectName(u"sender_name")
        self.sender_name.setGeometry(QRect(80, 40, 241, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.sender_name.setFont(font1)
        self.sender_name.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"}")
        self.sender_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sender_name_2 = QLabel(self.global_frame)
        self.sender_name_2.setObjectName(u"sender_name_2")
        self.sender_name_2.setGeometry(QRect(260, 60, 71, 21))
        font2 = QFont()
        font2.setPointSize(7)
        self.sender_name_2.setFont(font2)
        self.sender_name_2.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"	color:gray;\n"
"}")
        self.sender_name_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.retranslateUi(NotificationWidget)

        QMetaObject.connectSlotsByName(NotificationWidget)
    # setupUi

    def retranslateUi(self, NotificationWidget):
        NotificationWidget.setWindowTitle(QCoreApplication.translate("NotificationWidget", u"AR Notifier", None))
        self.title.setText(QCoreApplication.translate("NotificationWidget", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nouveau message</span></p></body></html>", None))
        self.sender_name.setText(QCoreApplication.translate("NotificationWidget", u"Username sent you a massage", None))
        self.sender_name_2.setText(QCoreApplication.translate("NotificationWidget", u"AR Intercom 2.1", None))
    # retranslateUi

