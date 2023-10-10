# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)
from resources import img_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(353, 336)
        icon = QIcon()
        icon.addFile(u":/icons/icons/app_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        SplashScreen.setStyleSheet(u"border:none;")
        self.base = QFrame(SplashScreen)
        self.base.setObjectName(u"base")
        self.base.setGeometry(QRect(3, 3, 331, 301))
        self.base.setFrameShape(QFrame.StyledPanel)
        self.base.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.base)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.base)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(265, 265))
        self.line.setMaximumSize(QSize(265, 265))
        self.line.setStyleSheet(u"QFrame{\n"
"	border-radius:132px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.line.setFrameShape(QFrame.StyledPanel)
        self.line.setFrameShadow(QFrame.Raised)
        self.circular_progress = QFrame(self.line)
        self.circular_progress.setObjectName(u"circular_progress")
        self.circular_progress.setGeometry(QRect(0, 0, 265, 265))
        self.circular_progress.setMinimumSize(QSize(160, 160))
        self.circular_progress.setMaximumSize(QSize(265, 265))
        self.circular_progress.setStyleSheet(u"QFrame{\n"
"border-radius:132px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(250, 249, 251, 255), stop:\n"
"0.750 rgba(255, 0, 0, 255));\n"
"}")
        self.circular_progress.setFrameShape(QFrame.StyledPanel)
        self.circular_progress.setFrameShadow(QFrame.Raised)
        self.background = QFrame(self.circular_progress)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(7, 8, 251, 251))
        self.background.setMinimumSize(QSize(251, 251))
        self.background.setMaximumSize(QSize(251, 251))
        self.background.setStyleSheet(u"border-radius:125px;\n"
"border:46px solid rgb(0, 59, 89);\n"
"background; white;\n"
"border-color: rgb(79, 0, 0);")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.loading = QLabel(self.circular_progress)
        self.loading.setObjectName(u"loading")
        self.loading.setGeometry(QRect(64, 220, 141, 21))
        self.loading.setMinimumSize(QSize(141, 21))
        self.loading.setMaximumSize(QSize(141, 21))
        self.loading.setStyleSheet(u"QLabel{	\n"
"	border-radius:5;\n"
"	color: rgba(255, 255, 255, 60);\n"
"	background:none;\n"
"	font-weight:0;\n"
"	font-family:Kirvy-Bold;\n"
"	font-size:12px;\n"
"}")
        self.loading.setAlignment(Qt.AlignCenter)
        self.app_name = QLabel(self.circular_progress)
        self.app_name.setObjectName(u"app_name")
        self.app_name.setGeometry(QRect(83, 26, 101, 21))
        self.app_name.setMinimumSize(QSize(101, 21))
        self.app_name.setMaximumSize(QSize(101, 21))
        self.app_name.setStyleSheet(u"QLabel{	\n"
"	border-radius:5;\n"
"	\n"
"	color:#bbFFFFFF;\n"
"	background-color: rgba(255, 255, 255, 20);\n"
"	font-family:Kirvy-Regular;\n"
"	font-weight:bold;\n"
"	font-size:12px;\n"
"}")
        self.app_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)

        self.circular_foreground = QFrame(SplashScreen)
        self.circular_foreground.setObjectName(u"circular_foreground")
        self.circular_foreground.setGeometry(QRect(87, 72, 170, 170))
        self.circular_foreground.setMinimumSize(QSize(170, 170))
        self.circular_foreground.setMaximumSize(QSize(170, 170))
        self.circular_foreground.setStyleSheet(u"image: url(:/icons/icons/AR_logo.png);\n"
"border:none;")
        self.circular_foreground.setFrameShape(QFrame.StyledPanel)
        self.circular_foreground.setFrameShadow(QFrame.Raised)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"AR Intercom", None))
        self.loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:400;\">Edited by Antares</span></p></body></html>", None))
        self.app_name.setText(QCoreApplication.translate("SplashScreen", u"AR Intercom 2", None))
    # retranslateUi

