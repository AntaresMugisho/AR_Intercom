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
        self.global_frame.setStyleSheet(u"QFrame{\n"
"	outline:none;\n"
"	background-color:grey;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	background:none;\n"
"	font-family:Kirvy;\n"
"}")
        self.global_frame.setFrameShape(QFrame.StyledPanel)
        self.global_frame.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.global_frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(80, 2, 221, 31))
        self.title.setStyleSheet(u"QLabel{\n"
"	background:none;\n"
"	font:bold 18px;\n"
"}")
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.logo = QPushButton(self.global_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(2, -1, 85, 85))
        self.logo.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/icons/AR_logo.png);\n"
"	background:none;\n"
"	border:none;\n"
"}")
        self.sender_name = QLabel(self.global_frame)
        self.sender_name.setObjectName(u"sender_name")
        self.sender_name.setGeometry(QRect(80, 32, 221, 31))
        self.sender_name.setStyleSheet(u"QLabel{\n"
"	background:none;\n"
"	font: bold 16px;\n"
"}")
        self.sender_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.app_name = QLabel(self.global_frame)
        self.app_name.setObjectName(u"app_name")
        self.app_name.setGeometry(QRect(215, 60, 101, 20))
        self.app_name.setStyleSheet(u"QLabel{\n"
"	background:none;\n"
"	color:#EcEcEc;\n"
"}")
        self.app_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(NotificationWidget)

        QMetaObject.connectSlotsByName(NotificationWidget)
    # setupUi

    def retranslateUi(self, NotificationWidget):
        NotificationWidget.setWindowTitle(QCoreApplication.translate("NotificationWidget", u"AR Notifier", None))
        self.title.setText(QCoreApplication.translate("NotificationWidget", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nouveau message</span></p></body></html>", None))
        self.sender_name.setText(QCoreApplication.translate("NotificationWidget", u"<html><head/><body><p>Un message de Antares</p></body></html>", None))
        self.app_name.setText(QCoreApplication.translate("NotificationWidget", u"<html><head/><body><p><span style=\" font-size:7pt;\">AR Intercom 2</span></p></body></html>", None))
    # retranslateUi

