# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(690, 470)
        LoginWindow.setStyleSheet("")
        self.central_log = QtWidgets.QWidget(LoginWindow)
        self.central_log.setObjectName("central_log")
        self.log_username = QtWidgets.QLineEdit(self.central_log)
        self.log_username.setGeometry(QtCore.QRect(371, 160, 250, 40))
        self.log_username.setStyleSheet("QLineEdit{\n"
"    border:2px solid; \n"
"    border-radius:20px;\n"
"    font-size:18px;\n"
"    padding-left:15px;\n"
"    padding-right:15px; \n"
"    border-color:#FFF; \n"
"    background-color:#FFFFFF;}\n"
"\n"
"QLineEdit:hover,  QLineEdit:focus{\n"
"    border-color: rgba(57, 146, 240, 180); \n"
"}")
        self.log_username.setObjectName("log_username")
        self.log_password = QtWidgets.QLineEdit(self.central_log)
        self.log_password.setGeometry(QtCore.QRect(371, 239, 250, 40))
        self.log_password.setStyleSheet("QLineEdit{\n"
"    border:2px solid; \n"
"    border-radius:20px;\n"
"    font-size:18px;\n"
"    padding-left:15px;\n"
"    padding-right:15px; \n"
"    border-color:#FFF; \n"
"    background-color:#FFFFFF;}\n"
"\n"
"QLineEdit:hover,  QLineEdit:focus{\n"
"    border-color: rgba(57, 146, 240, 180); \n"
"}")
        self.log_password.setText("")
        self.log_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_password.setObjectName("log_password")
        self.toogle_button = QtWidgets.QPushButton(self.central_log)
        self.toogle_button.setGeometry(QtCore.QRect(578, 248, 24, 24))
        self.toogle_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toogle_button.setStyleSheet("QPushButton{\n"
"            image: url(:/cils/cils/cil_vision.png);\n"
"            background:none;\n"
"            border:none;}\n"
"\n"
"QPushButton:hover{\n"
"            image: url(:/cils/cils/cil_low_vision.png);\n"
"            background:none;\n"
"            border:none;}")
        self.toogle_button.setText("")
        self.toogle_button.setObjectName("toogle_button")
        self.connect_log = QtWidgets.QPushButton(self.central_log)
        self.connect_log.setGeometry(QtCore.QRect(407, 337, 171, 41))
        self.connect_log.setStyleSheet("QPushButton{\n"
"    border:2px solid rgba(57, 146, 240, 250);\n"
"    border-radius:20px; \n"
"    font-size:18px; \n"
"    padding-left:15px;\n"
"    padding-right:15px; \n"
"    background-color:#FFFFFF;\n"
"    color:rgba(57, 146, 240, 250);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    font-weight:bold;\n"
"    background-color: rgba(57, 146, 240, 250);\n"
"    color:#FFFFFF;\n"
"}")
        self.connect_log.setObjectName("connect_log")
        self.welcome_log = QtWidgets.QLabel(self.central_log)
        self.welcome_log.setGeometry(QtCore.QRect(291, 42, 401, 41))
        self.welcome_log.setStyleSheet("background-color: rgb(11, 11, 106);\n"
"color: rgb(255, 255, 255);font-size:16px; font-weight:bold; font-family:Roboto ;")
        self.welcome_log.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.welcome_log.setObjectName("welcome_log")
        self.connect_now = QtWidgets.QLabel(self.central_log)
        self.connect_now.setGeometry(QtCore.QRect(337, 70, 301, 21))
        self.connect_now.setStyleSheet("color: rgb(0, 0, 0);\n"
";font-size:14px; font-family:Roboto ;\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius:10px;")
        self.connect_now.setAlignment(QtCore.Qt.AlignCenter)
        self.connect_now.setObjectName("connect_now")
        self.logo_log = QtWidgets.QLabel(self.central_log)
        self.logo_log.setGeometry(QtCore.QRect(0, 0, 291, 83))
        self.logo_log.setStyleSheet("border-left:4px solid;\n"
"border-left-color: rgb(255, 170, 0);\n"
"background-color: rgb(11, 11, 106);\n"
"image: url(:/icons/icons/ARsoftlogo.png);\n"
"")
        self.logo_log.setText("")
        self.logo_log.setObjectName("logo_log")
        self.main_title_log = QtWidgets.QLabel(self.central_log)
        self.main_title_log.setGeometry(QtCore.QRect(292, 0, 401, 41))
        self.main_title_log.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font-size:20px; font-weight:bold; font-family: Kirvy ,Roboto ;")
        self.main_title_log.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title_log.setObjectName("main_title_log")
        self.multi_logo_background = QtWidgets.QLabel(self.central_log)
        self.multi_logo_background.setGeometry(QtCore.QRect(290, 79, 401, 341))
        self.multi_logo_background.setStyleSheet("background-color: rgba(57, 146, 240, 5);\n"
"background-image: url(:/icons/icons/multilogo.png);")
        self.multi_logo_background.setText("")
        self.multi_logo_background.setObjectName("multi_logo_background")
        self.multicolor = QtWidgets.QFrame(self.central_log)
        self.multicolor.setGeometry(QtCore.QRect(0, 85, 291, 351))
        self.multicolor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.multicolor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.multicolor.setObjectName("multicolor")
        self.logo_20 = QtWidgets.QLabel(self.multicolor)
        self.logo_20.setGeometry(QtCore.QRect(31, 245, 81, 81))
        self.logo_20.setStyleSheet("background-color: rgba(246, 168, 202, 200);")
        self.logo_20.setText("")
        self.logo_20.setObjectName("logo_20")
        self.logo_10 = QtWidgets.QLabel(self.multicolor)
        self.logo_10.setGeometry(QtCore.QRect(106, 124, 81, 81))
        self.logo_10.setStyleSheet("background-color: rgba(137, 184, 227, 254);")
        self.logo_10.setText("")
        self.logo_10.setObjectName("logo_10")
        self.logo_4 = QtWidgets.QLabel(self.multicolor)
        self.logo_4.setGeometry(QtCore.QRect(-1, 45, 81, 81))
        self.logo_4.setStyleSheet("background-color: rgb(0, 114, 188);\n"
"")
        self.logo_4.setText("")
        self.logo_4.setObjectName("logo_4")
        self.logo_12 = QtWidgets.QLabel(self.multicolor)
        self.logo_12.setGeometry(QtCore.QRect(-1, 170, 81, 81))
        self.logo_12.setStyleSheet("\n"
"background-color: rgba(179, 34, 111, 200);\n"
"")
        self.logo_12.setText("")
        self.logo_12.setObjectName("logo_12")
        self.logo_19 = QtWidgets.QLabel(self.multicolor)
        self.logo_19.setGeometry(QtCore.QRect(209, 280, 81, 81))
        self.logo_19.setStyleSheet("\n"
"background-color: rgba(249, 161, 97, 180);")
        self.logo_19.setText("")
        self.logo_19.setObjectName("logo_19")
        self.logo_13 = QtWidgets.QLabel(self.multicolor)
        self.logo_13.setGeometry(QtCore.QRect(69, 180, 81, 81))
        self.logo_13.setStyleSheet("background-color: rgba(238, 44, 135, 150);")
        self.logo_13.setText("")
        self.logo_13.setObjectName("logo_13")
        self.logo_6 = QtWidgets.QLabel(self.multicolor)
        self.logo_6.setGeometry(QtCore.QRect(29, 110, 81, 81))
        self.logo_6.setStyleSheet("background-color: rgba(78, 59, 151, 150);")
        self.logo_6.setText("")
        self.logo_6.setObjectName("logo_6")
        self.logo_8 = QtWidgets.QLabel(self.multicolor)
        self.logo_8.setGeometry(QtCore.QRect(80, 35, 101, 91))
        self.logo_8.setStyleSheet("background-color: rgba(0, 114, 188, 200);\n"
"")
        self.logo_8.setText("")
        self.logo_8.setObjectName("logo_8")
        self.logo_27 = QtWidgets.QLabel(self.multicolor)
        self.logo_27.setGeometry(QtCore.QRect(181, -1, 71, 71))
        self.logo_27.setStyleSheet("background-color: rgba(176, 227, 250, 200);")
        self.logo_27.setText("")
        self.logo_27.setObjectName("logo_27")
        self.logo_25 = QtWidgets.QLabel(self.multicolor)
        self.logo_25.setGeometry(QtCore.QRect(11, -1, 81, 31))
        self.logo_25.setStyleSheet("background-color: rgba(0, 0, 100, 200);")
        self.logo_25.setText("")
        self.logo_25.setObjectName("logo_25")
        self.logo_28 = QtWidgets.QLabel(self.multicolor)
        self.logo_28.setGeometry(QtCore.QRect(229, -1, 61, 71))
        self.logo_28.setStyleSheet("background-color: rgba(176, 227, 250, 200);")
        self.logo_28.setText("")
        self.logo_28.setObjectName("logo_28")
        self.logo_24 = QtWidgets.QLabel(self.multicolor)
        self.logo_24.setGeometry(QtCore.QRect(249, 110, 41, 81))
        self.logo_24.setStyleSheet("background-color: rgba(25, 187, 238, 100);\n"
"")
        self.logo_24.setText("")
        self.logo_24.setObjectName("logo_24")
        self.logo_16 = QtWidgets.QLabel(self.multicolor)
        self.logo_16.setGeometry(QtCore.QRect(209, 150, 81, 81))
        self.logo_16.setStyleSheet("background-color: rgba(0, 176, 76, 150);")
        self.logo_16.setText("")
        self.logo_16.setObjectName("logo_16")
        self.logo_7 = QtWidgets.QLabel(self.multicolor)
        self.logo_7.setGeometry(QtCore.QRect(187, 90, 81, 81))
        self.logo_7.setStyleSheet("background-color: rgba(25, 187, 238, 50);\n"
"")
        self.logo_7.setText("")
        self.logo_7.setObjectName("logo_7")
        self.logo_14 = QtWidgets.QLabel(self.multicolor)
        self.logo_14.setGeometry(QtCore.QRect(10, 240, 41, 41))
        self.logo_14.setStyleSheet("\n"
"background-color: rgba(179, 34, 111, 100);\n"
"")
        self.logo_14.setText("")
        self.logo_14.setObjectName("logo_14")
        self.logo_23 = QtWidgets.QLabel(self.multicolor)
        self.logo_23.setGeometry(QtCore.QRect(-1, 0, 101, 61))
        self.logo_23.setStyleSheet("background-color: rgba(0, 0, 100, 200);")
        self.logo_23.setText("")
        self.logo_23.setObjectName("logo_23")
        self.logo_22 = QtWidgets.QLabel(self.multicolor)
        self.logo_22.setGeometry(QtCore.QRect(100, 300, 121, 41))
        self.logo_22.setStyleSheet("background-color: rgba(247, 162, 135, 200);\n"
"background-color: rgba(239, 88, 63, 200);")
        self.logo_22.setText("")
        self.logo_22.setObjectName("logo_22")
        self.logo_17 = QtWidgets.QLabel(self.multicolor)
        self.logo_17.setGeometry(QtCore.QRect(239, 200, 51, 81))
        self.logo_17.setStyleSheet("background-color: rgba(170, 207, 55, 200);")
        self.logo_17.setText("")
        self.logo_17.setObjectName("logo_17")
        self.logo_9 = QtWidgets.QLabel(self.multicolor)
        self.logo_9.setGeometry(QtCore.QRect(162, 60, 81, 81))
        self.logo_9.setStyleSheet("background-color: rgba(25, 187, 238, 180);\n"
"")
        self.logo_9.setText("")
        self.logo_9.setObjectName("logo_9")
        self.logo_18 = QtWidgets.QLabel(self.multicolor)
        self.logo_18.setGeometry(QtCore.QRect(169, 220, 81, 81))
        self.logo_18.setStyleSheet("background-color: rgba(255, 240, 0, 160);")
        self.logo_18.setText("")
        self.logo_18.setObjectName("logo_18")
        self.logo_26 = QtWidgets.QLabel(self.multicolor)
        self.logo_26.setGeometry(QtCore.QRect(91, -1, 91, 51))
        self.logo_26.setStyleSheet("background-color: rgba(107, 167, 218, 200);")
        self.logo_26.setText("")
        self.logo_26.setObjectName("logo_26")
        self.logo_21 = QtWidgets.QLabel(self.multicolor)
        self.logo_21.setGeometry(QtCore.QRect(99, 240, 81, 71))
        self.logo_21.setStyleSheet("background-color: rgba(255, 247, 142, 200);")
        self.logo_21.setText("")
        self.logo_21.setObjectName("logo_21")
        self.logo_15 = QtWidgets.QLabel(self.multicolor)
        self.logo_15.setGeometry(QtCore.QRect(139, 160, 81, 81))
        self.logo_15.setStyleSheet("background-color: rgba(105, 201, 198, 200);")
        self.logo_15.setText("")
        self.logo_15.setObjectName("logo_15")
        self.logo_11 = QtWidgets.QLabel(self.multicolor)
        self.logo_11.setGeometry(QtCore.QRect(-1, 90, 91, 81))
        self.logo_11.setStyleSheet("background-color: rgba(124, 56, 149, 200);\n"
"")
        self.logo_11.setText("")
        self.logo_11.setObjectName("logo_11")
        self.logo_5 = QtWidgets.QLabel(self.multicolor)
        self.logo_5.setGeometry(QtCore.QRect(243, 34, 47, 81))
        self.logo_5.setStyleSheet("background-color: rgba(25, 187, 238, 100);\n"
"")
        self.logo_5.setText("")
        self.logo_5.setObjectName("logo_5")
        self.logo_29 = QtWidgets.QLabel(self.multicolor)
        self.logo_29.setGeometry(QtCore.QRect(200, 10, 31, 31))
        self.logo_29.setStyleSheet("background-color: rgba(176, 227, 250, 255);")
        self.logo_29.setText("")
        self.logo_29.setObjectName("logo_29")
        self.logo_30 = QtWidgets.QLabel(self.multicolor)
        self.logo_30.setGeometry(QtCore.QRect(50, 320, 201, 31))
        self.logo_30.setStyleSheet("\n"
"background-color: rgba(239, 88, 63, 170);")
        self.logo_30.setText("")
        self.logo_30.setObjectName("logo_30")
        self.label = QtWidgets.QLabel(self.central_log)
        self.label.setGeometry(QtCore.QRect(630, 420, 51, 16))
        self.label.setStyleSheet("QLabel{\n"
"    color:#C5C5C5;    \n"
"}")
        self.label.setObjectName("label")
        self.name_warning = QtWidgets.QLabel(self.central_log)
        self.name_warning.setGeometry(QtCore.QRect(391, 201, 151, 16))
        self.name_warning.setStyleSheet("color:red;\n"
"font-size:12px;")
        self.name_warning.setObjectName("name_warning")
        self.psw_warning = QtWidgets.QLabel(self.central_log)
        self.psw_warning.setGeometry(QtCore.QRect(391, 283, 151, 16))
        self.psw_warning.setStyleSheet("color:red;\n"
"font-size:12px;")
        self.psw_warning.setObjectName("psw_warning")
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
        LoginWindow.setCentralWidget(self.central_log)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        self.log_password.returnPressed.connect(self.connect_log.click)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Connexion - AR Intercom"))
        self.log_username.setPlaceholderText(_translate("LoginWindow", "Nom d\'utilisateur"))
        self.log_password.setPlaceholderText(_translate("LoginWindow", "Mot de passe"))
        self.connect_log.setText(_translate("LoginWindow", "Connexion"))
        self.welcome_log.setText(_translate("LoginWindow", "Bienvenue  !"))
        self.connect_now.setText(_translate("LoginWindow", "Connectez-vous maintenant."))
        self.main_title_log.setText(_translate("LoginWindow", "Art Revolution Intercom"))
        self.label.setText(_translate("LoginWindow", "Kivringo"))
        self.name_warning.setText(_translate("LoginWindow", "Empty username"))
        self.psw_warning.setText(_translate("LoginWindow", "Wrong username"))
from resources import img_rc
