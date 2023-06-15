# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
from resources import img_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(690, 470)
        LoginWindow.setStyleSheet(u"")
        self.central_log = QWidget(LoginWindow)
        self.central_log.setObjectName(u"central_log")
        self.log_username = QLineEdit(self.central_log)
        self.log_username.setObjectName(u"log_username")
        self.log_username.setGeometry(QRect(371, 160, 250, 40))
        self.log_username.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid; \n"
"	border-radius:20px;\n"
"	font-size:18px;\n"
"	padding-left:15px;\n"
"	padding-right:15px; \n"
"	border-color:#FFF; \n"
"	background-color:#FFFFFF;}\n"
"\n"
"QLineEdit:hover,  QLineEdit:focus{\n"
"	border-color: rgba(57, 146, 240, 180); \n"
"}")
        self.log_password = QLineEdit(self.central_log)
        self.log_password.setObjectName(u"log_password")
        self.log_password.setGeometry(QRect(371, 239, 250, 40))
        self.log_password.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid; \n"
"	border-radius:20px;\n"
"	font-size:18px;\n"
"	padding-left:15px;\n"
"	padding-right:15px; \n"
"	border-color:#FFF; \n"
"	background-color:#FFFFFF;}\n"
"\n"
"QLineEdit:hover,  QLineEdit:focus{\n"
"	border-color: rgba(57, 146, 240, 180); \n"
"}")
        self.log_password.setEchoMode(QLineEdit.Password)
        self.toogle_button = QPushButton(self.central_log)
        self.toogle_button.setObjectName(u"toogle_button")
        self.toogle_button.setGeometry(QRect(578, 248, 24, 24))
        self.toogle_button.setFocusPolicy(Qt.NoFocus)
        self.toogle_button.setStyleSheet(u"QPushButton{\n"
"	        image: url(:/cils/cils/cil_vision.png);\n"
"            background:none;\n"
"            border:none;}\n"
"\n"
"QPushButton:hover{\n"
"            image: url(:/cils/cils/cil_low_vision.png);\n"
"            background:none;\n"
"            border:none;}")
        self.connect_log = QPushButton(self.central_log)
        self.connect_log.setObjectName(u"connect_log")
        self.connect_log.setGeometry(QRect(407, 337, 171, 41))
        self.connect_log.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgba(57, 146, 240, 250);\n"
"	border-radius:20px; \n"
"	font-size:18px; \n"
"	padding-left:15px;\n"
"	padding-right:15px; \n"
"	background-color:#FFFFFF;\n"
"	color:rgba(57, 146, 240, 250);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font-weight:bold;\n"
"	background-color: rgba(57, 146, 240, 250);\n"
"	color:#FFFFFF;\n"
"}")
        self.welcome_log = QLabel(self.central_log)
        self.welcome_log.setObjectName(u"welcome_log")
        self.welcome_log.setGeometry(QRect(291, 42, 401, 41))
        self.welcome_log.setStyleSheet(u"background-color: rgb(11, 11, 106);\n"
"color: rgb(255, 255, 255);font-size:16px; font-weight:bold; font-family:Roboto ;")
        self.welcome_log.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.connect_now = QLabel(self.central_log)
        self.connect_now.setObjectName(u"connect_now")
        self.connect_now.setGeometry(QRect(337, 70, 301, 21))
        self.connect_now.setStyleSheet(u"color: rgb(0, 0, 0);\n"
";font-size:14px; font-family:Roboto ;\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius:10px;")
        self.connect_now.setAlignment(Qt.AlignCenter)
        self.logo_log = QLabel(self.central_log)
        self.logo_log.setObjectName(u"logo_log")
        self.logo_log.setGeometry(QRect(0, 0, 291, 83))
        self.logo_log.setStyleSheet(u"border-left:4px solid;\n"
"border-left-color: rgb(255, 170, 0);\n"
"background-color: rgb(11, 11, 106);\n"
"image: url(:/icons/icons/ARsoftlogo.png);\n"
"")
        self.main_title_log = QLabel(self.central_log)
        self.main_title_log.setObjectName(u"main_title_log")
        self.main_title_log.setGeometry(QRect(292, 0, 401, 41))
        self.main_title_log.setStyleSheet(u"color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font-size:20px; font-weight:bold; font-family: Kirvy ,Roboto ;")
        self.main_title_log.setAlignment(Qt.AlignCenter)
        self.multi_logo_background = QLabel(self.central_log)
        self.multi_logo_background.setObjectName(u"multi_logo_background")
        self.multi_logo_background.setGeometry(QRect(290, 79, 401, 341))
        self.multi_logo_background.setStyleSheet(u"background-color: rgba(57, 146, 240, 5);\n"
"background-image: url(:/icons/icons/multilogo.png);")
        self.multicolor = QFrame(self.central_log)
        self.multicolor.setObjectName(u"multicolor")
        self.multicolor.setGeometry(QRect(0, 85, 291, 351))
        self.multicolor.setFrameShape(QFrame.StyledPanel)
        self.multicolor.setFrameShadow(QFrame.Raised)
        self.logo_20 = QLabel(self.multicolor)
        self.logo_20.setObjectName(u"logo_20")
        self.logo_20.setGeometry(QRect(31, 245, 81, 81))
        self.logo_20.setStyleSheet(u"background-color: rgba(246, 168, 202, 200);")
        self.logo_10 = QLabel(self.multicolor)
        self.logo_10.setObjectName(u"logo_10")
        self.logo_10.setGeometry(QRect(106, 124, 81, 81))
        self.logo_10.setStyleSheet(u"background-color: rgba(137, 184, 227, 254);")
        self.logo_4 = QLabel(self.multicolor)
        self.logo_4.setObjectName(u"logo_4")
        self.logo_4.setGeometry(QRect(-1, 45, 81, 81))
        self.logo_4.setStyleSheet(u"background-color: rgb(0, 114, 188);\n"
"")
        self.logo_12 = QLabel(self.multicolor)
        self.logo_12.setObjectName(u"logo_12")
        self.logo_12.setGeometry(QRect(-1, 170, 81, 81))
        self.logo_12.setStyleSheet(u"\n"
"background-color: rgba(179, 34, 111, 200);\n"
"")
        self.logo_19 = QLabel(self.multicolor)
        self.logo_19.setObjectName(u"logo_19")
        self.logo_19.setGeometry(QRect(209, 280, 81, 81))
        self.logo_19.setStyleSheet(u"\n"
"background-color: rgba(249, 161, 97, 180);")
        self.logo_13 = QLabel(self.multicolor)
        self.logo_13.setObjectName(u"logo_13")
        self.logo_13.setGeometry(QRect(69, 180, 81, 81))
        self.logo_13.setStyleSheet(u"background-color: rgba(238, 44, 135, 150);")
        self.logo_6 = QLabel(self.multicolor)
        self.logo_6.setObjectName(u"logo_6")
        self.logo_6.setGeometry(QRect(29, 110, 81, 81))
        self.logo_6.setStyleSheet(u"background-color: rgba(78, 59, 151, 150);")
        self.logo_8 = QLabel(self.multicolor)
        self.logo_8.setObjectName(u"logo_8")
        self.logo_8.setGeometry(QRect(80, 35, 101, 91))
        self.logo_8.setStyleSheet(u"background-color: rgba(0, 114, 188, 200);\n"
"")
        self.logo_27 = QLabel(self.multicolor)
        self.logo_27.setObjectName(u"logo_27")
        self.logo_27.setGeometry(QRect(181, -1, 71, 71))
        self.logo_27.setStyleSheet(u"background-color: rgba(176, 227, 250, 200);")
        self.logo_25 = QLabel(self.multicolor)
        self.logo_25.setObjectName(u"logo_25")
        self.logo_25.setGeometry(QRect(11, -1, 81, 31))
        self.logo_25.setStyleSheet(u"background-color: rgba(0, 0, 100, 200);")
        self.logo_28 = QLabel(self.multicolor)
        self.logo_28.setObjectName(u"logo_28")
        self.logo_28.setGeometry(QRect(229, -1, 61, 71))
        self.logo_28.setStyleSheet(u"background-color: rgba(176, 227, 250, 200);")
        self.logo_24 = QLabel(self.multicolor)
        self.logo_24.setObjectName(u"logo_24")
        self.logo_24.setGeometry(QRect(249, 110, 41, 81))
        self.logo_24.setStyleSheet(u"background-color: rgba(25, 187, 238, 100);\n"
"")
        self.logo_16 = QLabel(self.multicolor)
        self.logo_16.setObjectName(u"logo_16")
        self.logo_16.setGeometry(QRect(209, 150, 81, 81))
        self.logo_16.setStyleSheet(u"background-color: rgba(0, 176, 76, 150);")
        self.logo_7 = QLabel(self.multicolor)
        self.logo_7.setObjectName(u"logo_7")
        self.logo_7.setGeometry(QRect(187, 90, 81, 81))
        self.logo_7.setStyleSheet(u"background-color: rgba(25, 187, 238, 50);\n"
"")
        self.logo_14 = QLabel(self.multicolor)
        self.logo_14.setObjectName(u"logo_14")
        self.logo_14.setGeometry(QRect(10, 240, 41, 41))
        self.logo_14.setStyleSheet(u"\n"
"background-color: rgba(179, 34, 111, 100);\n"
"")
        self.logo_23 = QLabel(self.multicolor)
        self.logo_23.setObjectName(u"logo_23")
        self.logo_23.setGeometry(QRect(-1, 0, 101, 61))
        self.logo_23.setStyleSheet(u"background-color: rgba(0, 0, 100, 200);")
        self.logo_22 = QLabel(self.multicolor)
        self.logo_22.setObjectName(u"logo_22")
        self.logo_22.setGeometry(QRect(100, 300, 121, 41))
        self.logo_22.setStyleSheet(u"background-color: rgba(247, 162, 135, 200);\n"
"background-color: rgba(239, 88, 63, 200);")
        self.logo_17 = QLabel(self.multicolor)
        self.logo_17.setObjectName(u"logo_17")
        self.logo_17.setGeometry(QRect(239, 200, 51, 81))
        self.logo_17.setStyleSheet(u"background-color: rgba(170, 207, 55, 200);")
        self.logo_9 = QLabel(self.multicolor)
        self.logo_9.setObjectName(u"logo_9")
        self.logo_9.setGeometry(QRect(162, 60, 81, 81))
        self.logo_9.setStyleSheet(u"background-color: rgba(25, 187, 238, 180);\n"
"")
        self.logo_18 = QLabel(self.multicolor)
        self.logo_18.setObjectName(u"logo_18")
        self.logo_18.setGeometry(QRect(169, 220, 81, 81))
        self.logo_18.setStyleSheet(u"background-color: rgba(255, 240, 0, 160);")
        self.logo_26 = QLabel(self.multicolor)
        self.logo_26.setObjectName(u"logo_26")
        self.logo_26.setGeometry(QRect(91, -1, 91, 51))
        self.logo_26.setStyleSheet(u"background-color: rgba(107, 167, 218, 200);")
        self.logo_21 = QLabel(self.multicolor)
        self.logo_21.setObjectName(u"logo_21")
        self.logo_21.setGeometry(QRect(99, 240, 81, 71))
        self.logo_21.setStyleSheet(u"background-color: rgba(255, 247, 142, 200);")
        self.logo_15 = QLabel(self.multicolor)
        self.logo_15.setObjectName(u"logo_15")
        self.logo_15.setGeometry(QRect(139, 160, 81, 81))
        self.logo_15.setStyleSheet(u"background-color: rgba(105, 201, 198, 200);")
        self.logo_11 = QLabel(self.multicolor)
        self.logo_11.setObjectName(u"logo_11")
        self.logo_11.setGeometry(QRect(-1, 90, 91, 81))
        self.logo_11.setStyleSheet(u"background-color: rgba(124, 56, 149, 200);\n"
"")
        self.logo_5 = QLabel(self.multicolor)
        self.logo_5.setObjectName(u"logo_5")
        self.logo_5.setGeometry(QRect(243, 34, 47, 81))
        self.logo_5.setStyleSheet(u"background-color: rgba(25, 187, 238, 100);\n"
"")
        self.logo_29 = QLabel(self.multicolor)
        self.logo_29.setObjectName(u"logo_29")
        self.logo_29.setGeometry(QRect(200, 10, 31, 31))
        self.logo_29.setStyleSheet(u"background-color: rgba(176, 227, 250, 255);")
        self.logo_30 = QLabel(self.multicolor)
        self.logo_30.setObjectName(u"logo_30")
        self.logo_30.setGeometry(QRect(50, 320, 201, 31))
        self.logo_30.setStyleSheet(u"\n"
"background-color: rgba(239, 88, 63, 170);")
        self.label = QLabel(self.central_log)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(630, 420, 51, 16))
        self.label.setStyleSheet(u"QLabel{\n"
"	color:#C5C5C5;	\n"
"}")
        self.name_warning = QLabel(self.central_log)
        self.name_warning.setObjectName(u"name_warning")
        self.name_warning.setGeometry(QRect(391, 201, 151, 16))
        self.name_warning.setStyleSheet(u"color:red;\n"
"font-size:12px;")
        self.psw_warning = QLabel(self.central_log)
        self.psw_warning.setObjectName(u"psw_warning")
        self.psw_warning.setGeometry(QRect(391, 283, 151, 16))
        self.psw_warning.setStyleSheet(u"color:red;\n"
"font-size:12px;")
        LoginWindow.setCentralWidget(self.central_log)
        self.multi_logo_background.raise_()
        self.log_username.raise_()
        self.log_password.raise_()
        self.toogle_button.raise_()
        self.connect_log.raise_()
        self.welcome_log.raise_()
        self.connect_now.raise_()
        self.logo_log.raise_()
        self.main_title_log.raise_()
        self.multicolor.raise_()
        self.label.raise_()
        self.name_warning.raise_()
        self.psw_warning.raise_()
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 690, 19))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        self.log_password.returnPressed.connect(self.connect_log.click)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Connexion - AR Intercom", None))
        self.log_username.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Nom d'utilisateur", None))
        self.log_password.setText("")
        self.log_password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Mot de passe", None))
        self.toogle_button.setText("")
        self.connect_log.setText(QCoreApplication.translate("LoginWindow", u"Connexion", None))
        self.welcome_log.setText(QCoreApplication.translate("LoginWindow", u"Bienvenue  !", None))
        self.connect_now.setText(QCoreApplication.translate("LoginWindow", u"Connectez-vous maintenant.", None))
        self.logo_log.setText("")
        self.main_title_log.setText(QCoreApplication.translate("LoginWindow", u"Art Revolution Intercom", None))
        self.multi_logo_background.setText("")
        self.logo_20.setText("")
        self.logo_10.setText("")
        self.logo_4.setText("")
        self.logo_12.setText("")
        self.logo_19.setText("")
        self.logo_13.setText("")
        self.logo_6.setText("")
        self.logo_8.setText("")
        self.logo_27.setText("")
        self.logo_25.setText("")
        self.logo_28.setText("")
        self.logo_24.setText("")
        self.logo_16.setText("")
        self.logo_7.setText("")
        self.logo_14.setText("")
        self.logo_23.setText("")
        self.logo_22.setText("")
        self.logo_17.setText("")
        self.logo_9.setText("")
        self.logo_18.setText("")
        self.logo_26.setText("")
        self.logo_21.setText("")
        self.logo_15.setText("")
        self.logo_11.setText("")
        self.logo_5.setText("")
        self.logo_29.setText("")
        self.logo_30.setText("")
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Kivringo", None))
        self.name_warning.setText(QCoreApplication.translate("LoginWindow", u"Empty username", None))
        self.psw_warning.setText(QCoreApplication.translate("LoginWindow", u"Wrong username", None))
    # retranslateUi

