# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTextBrowser, QVBoxLayout, QWidget)
from resources import img_rc

class Ui_SigninWindow(object):
    def setupUi(self, SigninWindow):
        if not SigninWindow.objectName():
            SigninWindow.setObjectName(u"SigninWindow")
        SigninWindow.resize(275, 593)
        icon = QIcon()
        icon.addFile(u":/icons/icons/app_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        SigninWindow.setWindowIcon(icon)
        self.stackedWidget = QStackedWidget(SigninWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 45, 275, 541))
        self.stackedWidget.setStyleSheet(u"QStackedWidget{\n"
"	background-color:#FFFFFF;\n"
"	border-bottom-left-radius:12px;\n"
"	border-bottom-right-radius:12px;\n"
"}\n"
"\n"
"\n"
"/* SCROLL BAR */\n"
"            \n"
"QScrollBar:vertical{border: none;background: #CCDDFF;width: 10px; margin: 21px 0 21px 0; border-radius: 0px;}\n"
"\n"
"QScrollBar::handle:vertical{background: #3385CC; min-height: 25px; border-radius: 5px;}\n"
"\n"
"QScrollBar::add-line:vertical{border: none; background: #3385CC;height: 20px;\n"
"            border-bottom-left-radius: 5px; border-bottom-right-radius: 5px;\n"
"            subcontrol-position: bottom; subcontrol-origin: margin;}\n"
"\n"
"QScrollBar::sub-line:vertical{border: none; background: #3385CC; height: 20px;\n"
"            border-top-left-radius: 5px; border-top-right-radius: 5px;\n"
"            subcontrol-position: top;subcontrol-origin: margin;}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{background: none;}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {bac"
                        "kground: none;}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"")
        self.central_signin = QFrame(self.page)
        self.central_signin.setObjectName(u"central_signin")
        self.central_signin.setGeometry(QRect(0, 0, 275, 531))
        self.central_signin.setMinimumSize(QSize(275, 511))
        self.central_signin.setMaximumSize(QSize(275, 16777215))
        self.central_signin.setStyleSheet(u"")
        self.create_account = QLabel(self.central_signin)
        self.create_account.setObjectName(u"create_account")
        self.create_account.setGeometry(QRect(-2, 30, 280, 21))
        self.create_account.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);font-size:14px; font-family:Roboto ;\n"
"border-radius:10px;")
        self.create_account.setAlignment(Qt.AlignCenter)
        self.form = QFrame(self.central_signin)
        self.form.setObjectName(u"form")
        self.form.setGeometry(QRect(3, 312, 268, 150))
        self.form.setStyleSheet(u"QFrame{\n"
"background-color: rgba(57, 146, 240, 50);\n"
"border-radius:20px;}")
        self.form.setFrameShape(QFrame.StyledPanel)
        self.form.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.user_name = QLineEdit(self.form)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setMinimumSize(QSize(250, 40))
        self.user_name.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout.addWidget(self.user_name)

        self.passcode = QLineEdit(self.form)
        self.passcode.setObjectName(u"passcode")
        self.passcode.setMinimumSize(QSize(250, 40))
        self.passcode.setStyleSheet(u"QLineEdit{\n"
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
        self.passcode.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.passcode)

        self.passcode2 = QLineEdit(self.form)
        self.passcode2.setObjectName(u"passcode2")
        self.passcode2.setMinimumSize(QSize(250, 40))
        self.passcode2.setStyleSheet(u"QLineEdit{\n"
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
        self.passcode2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passcode2)

        self.logo = QLabel(self.central_signin)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 59, 271, 71))
        self.logo.setStyleSheet(u"background-color: rgba(57, 146, 240, 5);\n"
"background-image: url(:/icons/icons/multilogo.png);\n"
"image:url(:/icons/icons/ARsoftlogo.png)")
        self.welcome = QLabel(self.central_signin)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(0, -7, 281, 41))
        self.welcome.setStyleSheet(u"background-color: rgb(51, 153, 204);\n"
"color: rgb(255, 255, 255);font-size:16px; font-weight:bold; font-family:Roboto ;")
        self.welcome.setAlignment(Qt.AlignCenter)
        self.image_field = QFrame(self.central_signin)
        self.image_field.setObjectName(u"image_field")
        self.image_field.setGeometry(QRect(2, 210, 270, 81))
        self.image_field.setStyleSheet(u"QFrame{\n"
"background-color: rgba(57, 146, 240, 50);\n"
"border-radius:20px;\n"
"}")
        self.image_field.setFrameShape(QFrame.StyledPanel)
        self.image_field.setFrameShadow(QFrame.Raised)
        self.next = QPushButton(self.central_signin)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(3, 490, 268, 41))
        self.next.setStyleSheet(u"QPushButton{\n"
"	border:none; \n"
"	border-radius:20px; \n"
"	font-size:18px; \n"
"	font-weight:bold;\n"
"	padding-left:15px;\n"
"	padding-right:15px; \n"
"	background-color:rgba(57, 146, 240, 180);\n"
"	color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:2px solid rgba(57, 146, 240, 250); \n"
"	font-weight:0;\n"
"	background-color:#FFFFFF;\n"
"	color:rgba(57, 146, 240, 250);\n"
"}")
        self.choose_profilepicture = QLabel(self.central_signin)
        self.choose_profilepicture.setObjectName(u"choose_profilepicture")
        self.choose_profilepicture.setGeometry(QRect(71, 144, 131, 131))
        self.choose_profilepicture.setStyleSheet(u"QLabel{\n"
"	border:1px solid #FFF;\n"
"	border-radius:65px;\n"
"	background-color:#FFFFFF;\n"
"	background-image: url(:/cils/cils/cil-user.png);	\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"	border: 4px solid ;\n"
"	border-color: #c1c1c1;\n"
"\n"
"}\n"
"\n"
"QLabel:hover,  QFrame:focus{\n"
"	border-color: rgba(57, 146, 240, 180); \n"
"}")
        self.choose_profilepicture.setScaledContents(True)
        self.choose_profilepicture.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.logo.raise_()
        self.form.raise_()
        self.welcome.raise_()
        self.create_account.raise_()
        self.image_field.raise_()
        self.next.raise_()
        self.choose_profilepicture.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.central_signin_2 = QFrame(self.page_2)
        self.central_signin_2.setObjectName(u"central_signin_2")
        self.central_signin_2.setGeometry(QRect(0, 1, 275, 601))
        self.central_signin_2.setMinimumSize(QSize(275, 511))
        self.central_signin_2.setMaximumSize(QSize(275, 16777215))
        self.central_signin_2.setStyleSheet(u"outline:none;")
        self.central_signin_2.setFrameShape(QFrame.StyledPanel)
        self.central_signin_2.setFrameShadow(QFrame.Raised)
        self.read_carefuly = QLabel(self.central_signin_2)
        self.read_carefuly.setObjectName(u"read_carefuly")
        self.read_carefuly.setGeometry(QRect(0, 28, 275, 21))
        self.read_carefuly.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);font-size:14px; font-family:Roboto ;\n"
"border-radius:10px;")
        self.read_carefuly.setAlignment(Qt.AlignCenter)
        self.cgu = QLabel(self.central_signin_2)
        self.cgu.setObjectName(u"cgu")
        self.cgu.setGeometry(QRect(0, 0, 280, 41))
        self.cgu.setStyleSheet(u"background-color: rgb(51, 153, 204);\n"
"color: rgb(255, 255, 255);font-size:16px; font-weight:bold; font-family:Roboto ;")
        self.cgu.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.validate = QPushButton(self.central_signin_2)
        self.validate.setObjectName(u"validate")
        self.validate.setGeometry(QRect(3, 490, 268, 41))
        self.validate.setStyleSheet(u"QPushButton{\n"
"	border:none; \n"
"	border-radius:20px; \n"
"	font-size:18px; \n"
"	font-weight:bold;\n"
"	padding-left:15px;\n"
"	padding-right:15px; \n"
"	background-color:rgba(57, 146, 240, 180);\n"
"	color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:2px solid rgba(57, 146, 240, 250); \n"
"	font-weight:0;\n"
"	background-color:#FFFFFF;\n"
"	color:rgba(57, 146, 240, 250);\n"
"}")
        self.textBrowser = QTextBrowser(self.central_signin_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(3, 62, 270, 371))
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
"	border-top-right-radius:5px;\n"
"	border-bottom-right-radius:5px;\n"
"	font-size:16px;\n"
"}")
        self.iaggree = QCheckBox(self.central_signin_2)
        self.iaggree.setObjectName(u"iaggree")
        self.iaggree.setGeometry(QRect(10, 450, 261, 20))
        self.cgu.raise_()
        self.read_carefuly.raise_()
        self.validate.raise_()
        self.textBrowser.raise_()
        self.iaggree.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.cgu_2 = QLabel(self.page_3)
        self.cgu_2.setObjectName(u"cgu_2")
        self.cgu_2.setGeometry(QRect(0, 2, 280, 41))
        self.cgu_2.setStyleSheet(u"background-color: rgb(51, 153, 204);\n"
"color: rgb(255, 255, 255);font-size:16px; font-weight:bold; font-family:Roboto ;")
        self.cgu_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.read_carefuly_2 = QLabel(self.page_3)
        self.read_carefuly_2.setObjectName(u"read_carefuly_2")
        self.read_carefuly_2.setGeometry(QRect(0, 30, 275, 21))
        self.read_carefuly_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);font-size:14px; font-family:Roboto ;\n"
"border-radius:10px;")
        self.read_carefuly_2.setAlignment(Qt.AlignCenter)
        self.whatnews_frame = QFrame(self.page_3)
        self.whatnews_frame.setObjectName(u"whatnews_frame")
        self.whatnews_frame.setGeometry(QRect(0, 60, 275, 556))
        self.whatnews_frame.setStyleSheet(u"")
        self.whatnews_frame.setFrameShape(QFrame.StyledPanel)
        self.whatnews_frame.setFrameShadow(QFrame.Raised)
        self.what_isnew = QStackedWidget(self.whatnews_frame)
        self.what_isnew.setObjectName(u"what_isnew")
        self.what_isnew.setGeometry(QRect(2, 0, 270, 401))
        self.what_isnew.setStyleSheet(u"background-color: #FFFFFF;")
        self.w0 = QWidget()
        self.w0.setObjectName(u"w0")
        self.w0.setStyleSheet(u"image: url(:/features/Features/0.png);")
        self.what_isnew.addWidget(self.w0)
        self.w1 = QWidget()
        self.w1.setObjectName(u"w1")
        self.w1.setStyleSheet(u"image: url(:/features/Features/1.png);")
        self.what_isnew.addWidget(self.w1)
        self.w2 = QWidget()
        self.w2.setObjectName(u"w2")
        self.w2.setStyleSheet(u"image: url(:/features/Features/2.png);")
        self.what_isnew.addWidget(self.w2)
        self.w3 = QWidget()
        self.w3.setObjectName(u"w3")
        self.w3.setStyleSheet(u"image: url(:/features/Features/3.png);")
        self.what_isnew.addWidget(self.w3)
        self.w4 = QWidget()
        self.w4.setObjectName(u"w4")
        self.w4.setStyleSheet(u"image: url(:/features/Features/4.png);")
        self.what_isnew.addWidget(self.w4)
        self.w5 = QWidget()
        self.w5.setObjectName(u"w5")
        self.w5.setStyleSheet(u"image: url(:/features/Features/5.png);")
        self.what_isnew.addWidget(self.w5)
        self.next_feature = QPushButton(self.whatnews_frame)
        self.next_feature.setObjectName(u"next_feature")
        self.next_feature.setGeometry(QRect(240, 220, 30, 30))
        self.next_feature.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"	background-color:#0055FF;\n"
"	background-image: url(:/cils/cils/cil-chevron-circle-right-alt.png);\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")
        self.prev_feature = QPushButton(self.whatnews_frame)
        self.prev_feature.setObjectName(u"prev_feature")
        self.prev_feature.setGeometry(QRect(6, 220, 30, 30))
        self.prev_feature.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"	background-color:#0055FF;\n"
"	background-image: url(:/cils/cils/cil-chevron-circle-left-alt.png);\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")
        self.current_feature = QFrame(self.whatnews_frame)
        self.current_feature.setObjectName(u"current_feature")
        self.current_feature.setGeometry(QRect(62, 392, 141, 21))
        self.current_feature.setStyleSheet(u"background:none;\n"
"outline:none;")
        self.current_feature.setFrameShape(QFrame.StyledPanel)
        self.current_feature.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.current_feature)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.feature_0 = QPushButton(self.current_feature)
        self.feature_0.setObjectName(u"feature_0")
        self.feature_0.setMinimumSize(QSize(15, 15))
        self.feature_0.setMaximumSize(QSize(15, 15))
        self.feature_0.setStyleSheet(u"QPushButton{\n"
"	background-color:#EAEAEA;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#3385CC;\n"
"}")

        self.horizontalLayout.addWidget(self.feature_0)

        self.feature_1 = QPushButton(self.current_feature)
        self.feature_1.setObjectName(u"feature_1")
        self.feature_1.setMinimumSize(QSize(15, 15))
        self.feature_1.setMaximumSize(QSize(15, 15))
        self.feature_1.setStyleSheet(u"QPushButton{\n"
"	background-color:#EAEAEA;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#3385CC;\n"
"}")

        self.horizontalLayout.addWidget(self.feature_1)

        self.feature_2 = QPushButton(self.current_feature)
        self.feature_2.setObjectName(u"feature_2")
        self.feature_2.setMinimumSize(QSize(15, 15))
        self.feature_2.setMaximumSize(QSize(15, 15))
        self.feature_2.setStyleSheet(u"QPushButton{\n"
"	background-color:#EAEAEA;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#3385CC;\n"
"}")

        self.horizontalLayout.addWidget(self.feature_2)

        self.feature_3 = QPushButton(self.current_feature)
        self.feature_3.setObjectName(u"feature_3")
        self.feature_3.setMinimumSize(QSize(15, 15))
        self.feature_3.setMaximumSize(QSize(15, 15))
        self.feature_3.setStyleSheet(u"QPushButton{\n"
"	background-color:#EAEAEA;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#3385CC;\n"
"}")

        self.horizontalLayout.addWidget(self.feature_3)

        self.feature_4 = QPushButton(self.current_feature)
        self.feature_4.setObjectName(u"feature_4")
        self.feature_4.setMinimumSize(QSize(15, 15))
        self.feature_4.setMaximumSize(QSize(15, 15))
        self.feature_4.setStyleSheet(u"QPushButton{\n"
"	background-color:#EAEAEA;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#3385CC;\n"
"}")

        self.horizontalLayout.addWidget(self.feature_4)

        self.feature_5 = QPushButton(self.current_feature)
        self.feature_5.setObjectName(u"feature_5")
        self.feature_5.setMinimumSize(QSize(15, 15))
        self.feature_5.setMaximumSize(QSize(15, 15))
        self.feature_5.setStyleSheet(u"QPushButton{\n"
"	background-color:#EAEAEA;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#3385CC;\n"
"}")

        self.horizontalLayout.addWidget(self.feature_5)

        self.terminate = QPushButton(self.whatnews_frame)
        self.terminate.setObjectName(u"terminate")
        self.terminate.setGeometry(QRect(3, 431, 268, 41))
        self.terminate.setStyleSheet(u"QPushButton{\n"
"	border:none; \n"
"	border-radius:20px; \n"
"	font-size:18px; \n"
"	font-weight:bold;\n"
"	padding-left:15px;\n"
"	padding-right:15px; \n"
"	background-color:rgba(57, 146, 240, 180);\n"
"	color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:2px solid rgba(57, 146, 240, 250); \n"
"	font-weight:0;\n"
"	background-color:#FFFFFF;\n"
"	color:rgba(57, 146, 240, 250);\n"
"}")
        self.stackedWidget.addWidget(self.page_3)
        self.main_title = QLabel(SigninWindow)
        self.main_title.setObjectName(u"main_title")
        self.main_title.setGeometry(QRect(0, 4, 275, 41))
        font = QFont()
        font.setFamilies([u"Kirvy"])
        font.setBold(True)
        self.main_title.setFont(font)
        self.main_title.setStyleSheet(u"color: rgb(51, 153, 204);\n"
"background-color: rgb(255, 255, 255);\n"
"font-size:20px; \n"
"font-weight:bold; \n"
"font-family: Kirvy;\n"
"padding-right:10px;\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius:12px;\n"
"")
        self.main_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.return_button = QPushButton(SigninWindow)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setGeometry(QRect(2, 12, 26, 26))
        self.return_button.setStyleSheet(u"QPushButton{\n"
"	image: url(:/cils/cils/cil-arrow-circle-left.png);\n"
"	border-radius:13px;\n"
"	background:none;\n"
"	color:none;\n"
"	border:none;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#3399CC;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:grey;\n"
"}")

        self.retranslateUi(SigninWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.what_isnew.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(SigninWindow)
    # setupUi

    def retranslateUi(self, SigninWindow):
        SigninWindow.setWindowTitle(QCoreApplication.translate("SigninWindow", u"Signin", None))
        self.create_account.setText(QCoreApplication.translate("SigninWindow", u"Cr\u00e9ez votre compte", None))
#if QT_CONFIG(tooltip)
        self.user_name.setToolTip(QCoreApplication.translate("SigninWindow", u"Saisissez votre nom d'utilisateur.", None))
#endif // QT_CONFIG(tooltip)
        self.user_name.setPlaceholderText(QCoreApplication.translate("SigninWindow", u"Nom d'utilisateur", None))
#if QT_CONFIG(tooltip)
        self.passcode.setToolTip(QCoreApplication.translate("SigninWindow", u"Saisissez votre mot de passe.\n"
"Utilisez un mot de passe facile \u00e0 retenir.", None))
#endif // QT_CONFIG(tooltip)
        self.passcode.setPlaceholderText(QCoreApplication.translate("SigninWindow", u"Mot de passe", None))
#if QT_CONFIG(tooltip)
        self.passcode2.setToolTip(QCoreApplication.translate("SigninWindow", u"Saisissez de nouveau votre mot de passe.", None))
#endif // QT_CONFIG(tooltip)
        self.passcode2.setPlaceholderText(QCoreApplication.translate("SigninWindow", u"Confirmer mot de passe", None))
        self.logo.setText("")
        self.welcome.setText(QCoreApplication.translate("SigninWindow", u"Bienvenue dans la r\u00e9volution !", None))
        self.next.setText(QCoreApplication.translate("SigninWindow", u"Suivant", None))
#if QT_CONFIG(tooltip)
        self.choose_profilepicture.setToolTip(QCoreApplication.translate("SigninWindow", u"<html><head/><body><p>Avatar (PRO)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.read_carefuly.setText(QCoreApplication.translate("SigninWindow", u"Lisez attentivement ces termes.", None))
        self.cgu.setText(QCoreApplication.translate("SigninWindow", u"Termes du contrat de licence.", None))
        self.validate.setText(QCoreApplication.translate("SigninWindow", u"Suivant", None))
        self.textBrowser.setHtml(QCoreApplication.translate("SigninWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600;\">CONDITIONS GENERALES D'UTILISATION  DU LOGICIEL &quot;AR Intercom&quot;</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\"> </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600;\">============================</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">Nom : AR Intercom</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">Version : 2.1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">Nom de version: Kivringo</span></p>"
                        "\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">Mise \u00e0 jour\u00a0	: 25-08-2023</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">Auteur : Antares Mugisho</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">E-mail auteur	: antaresmugisho@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">Editeur : Art Revolution Label</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:1"
                        "2pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">Site web : </span><a href=\"http://www.arintercom.org\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; text-decoration: underline; color:#0000ff;\">www.artrevolutionlqbel.com</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">Licence\u00a0: MIT</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600;\">============================</span></p>\n"
"<p style=\" margin-top:0px; mar"
                        "gin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">\u00a0</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 1</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : </span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Objet</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','s"
                        "ans-serif'; font-size:12pt; color:#333333;\">Les pr\u00e9sentes CGU ou Conditions G\u00e9n\u00e9rales d\u2019Utilisation encadrent juridiquement l\u2019utilisation des services du logiciel de messagerie intann\u00e9e &quot;</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">AR Intercom</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">&quot; (ci-apr\u00e8s d\u00e9nomm\u00e9 \u00ab le logiciel \u00bb).</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Constituant le contrat entre la soci\u00e9t\u00e9 Art Revolutin Label et le dernier Utilisateur, l\u2019acc\u00e8s au logiciel doit \u00eatre pr\u00e9c\u00e9d\u00e9 de l\u2019accept"
                        "ation de ces CGU. L\u2019acc\u00e8s \u00e0 cette plateforme signifie l\u2019acceptation des pr\u00e9sentes CGU.</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial Narrow','sans-serif'; font-size:12pt; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 2</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : </span><a href=\"https://www.legalplace.fr/guides/mentions-legales/\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; text-decoration: underline; color:#c00000;\">Mention"
                        "s l\u00e9gales</span></a><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#c00000;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">L\u2019\u00e9dition du logiciel Art Revolutuion Intercom est assur\u00e9e par la soci\u00e9t\u00e9 Art Revolution Label inscrite au RCCM, dont le si\u00e8ge social est localis\u00e9 \u00e0 Goma, Quartier Katoyi, Av. Bakisi, N\u00b055 dans la Province du Nord-Kivu, en R\u00e9publique D\u00e9mocraique du Congo.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 3</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : Acc\u00e8s au logiciel</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Le logiciel AR Intercom est fait pour permettre \u00e0 l\u2019utilisateur de communiquer gratuitement avec un autre disposant du m\u00eame logiciel. Les informations \u00e9chang\u00e9es peuvent \u00eatre des textes \u00e9crits ou des fichiers multim\u00e9dia entre autres les images, les m\u00e9dias audio, des m\u00e9dias visuels et autres types de donn\u00e9e mu"
                        "ltim\u00e9dia.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Les services du logiciel sont accessibles gratuitement par tout utilisateur disposant d'abord d'un compte AR intercom puis d\u2019un acc\u00e8s au r\u00e9seau local de l'entreprise. Tous les frais \u00e9ventuels n\u00e9cessaires pour l\u2019acc\u00e8s aux services (mat\u00e9riel informatique, connexion Internet\u2026) sont \u00e0 la charge de l\u2019utilisateur.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px; font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">L\u2019acc\u00e8s aux services d\u00e9di\u00e9s aux utilisateurs s\u2019effectue \u00e0 l\u2019aide d\u2019un identifiant (Nom d'utilisateur) et d\u2019un mot de passe pr\u00e9alablement d\u00e9finis par l\u2019utilisateur lors de sa premi\u00e8re utilisation du logiciel.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Pour des raisons de maintenance ou autres, l\u2019acc\u00e8s au logiciel peut \u00eatre interrompu ou suspendu par l\u2019\u00e9diteur sans pr\u00e9avis ni justification.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 4</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : Collecte des donn\u00e9es</span><span style=\" font-family:'Arial Narrow','sans-serif'"
                        "; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Pour la cr\u00e9ation du compte de l\u2019Utilisateur, la collecte des informations au moment de l\u2019inscription sur le logiciel est n\u00e9cessaire et obligatoire. Conform\u00e9ment \u00e0 la loi n\u00b078-17 du 6 janvier relative \u00e0 l\u2019informatique, aux fichiers et aux libert\u00e9s, la collecte et le traitement d\u2019informations personnelles s\u2019effectuent dans le respect de la vie priv\u00e9e.</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial Narrow','sans-serif'; font-size:12pt; background-color:#ffffff;\"><br /></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Suivant la loi Informatique et Libert\u00e9s en date du 6 janvier 1978, articles 39 et 40, l\u2019Utilisateur dispose du droit d\u2019acc\u00e9der, de rectifier, de supprimer et d\u2019opposer ses donn\u00e9es personnelles. L\u2019exercice de ce droit s\u2019effectue par le menu &quot;Mon Compte&quot; disponible dans les menus du logiciel.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family"
                        ":'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 5</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : Propri\u00e9t\u00e9 intellectuelle</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Les marques, logos ainsi que les contenus du logiciel AR Intercom (illustrations graphiques, textes\u2026) sont prot\u00e9g\u00e9s par le Code de la propri\u00e9t\u00e9 intellectuelle et par le droit d\u2019auteur.</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span styl"
                        "e=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">La reproduction ou la copie des contenus par l\u2019Utilisateur requi\u00e8rent une autorisation pr\u00e9alable de l'\u00e9diteur. Dans ce cas, toute utilisation \u00e0 des usages commerciaux ou \u00e0 des fins publicitaires est proscrite.</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 6</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : Responsabilit\u00e9"
                        "</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Bien que les informations \u00e9chang\u00e9es entre utilisateurs soient r\u00e9put\u00e9es fiables, le logiciel se r\u00e9serve la facult\u00e9 d\u2019une non-garantie de la fiabilit\u00e9 des sources.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">"
                        "En d\u00e9pit des mises \u00e0 jour r\u00e9guli\u00e8res, la responsabilit\u00e9 du logiciel ne peut \u00eatre engag\u00e9e en cas de modification des dispositions administratives et juridiques apparaissant apr\u00e8s la publication. Il en est de m\u00eame pour l\u2019utilisation et l\u2019interpr\u00e9tation des informations communiqu\u00e9es sur la plateforme.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Le logiciel d\u00e9cline toute responsabilit\u00e9 concernant les \u00e9ventuels virus pouvant infecter le mat\u00e9riel informatique de l\u2019Utilisateur apr\u00e8s l\u2019"
                        "utilisation ou l\u2019acc\u00e8s \u00e0 ce logiciel.</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Le logiciel ne peut \u00eatre tenu pour responsable en cas de force majeure ou du fait impr\u00e9visible et insurmontable d\u2019un tiers.</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial Narrow','sans-serif'; font-size:12pt; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style="
                        "\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">La garantie totale de la s\u00e9curit\u00e9 et la confidentialit\u00e9 des donn\u00e9es n\u2019est pas assur\u00e9e par le logiciel. Cependant, le logiciel s\u2019engage \u00e0 mettre en \u0153uvre toutes les m\u00e9thodes requises pour le faire au mieux.</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 7</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : Liens hypert"
                        "extes</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Le logiciel peut \u00eatre constitu\u00e9 de liens hypertextes. En cliquant sur ces derniers, l\u2019Utilisateur sortira de la plateforme. Cette derni\u00e8re n\u2019a pas de contr\u00f4le et ne peut pas \u00eatre tenue responsable du contenu des pages web relatives \u00e0 ces liens.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><"
                        "span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 08</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : Dur\u00e9e du contrat</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Le pr\u00e9sent contrat est valable pour une dur\u00e9e ind\u00e9termin\u00e9e. L'acceptation de ces termes par l'Utilisateur marque l\u2019application du contrat \u00e0 son \u00e9gard.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margi"
                        "n-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; font-weight:600; color:#333333;\">Article 09</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\"> : Droit applicable et juridiction comp\u00e9tente</span><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">Le pr\u00e9sent contrat est soumis \u00e0 la l\u00e9gislation congolaise. L\u2019absence de r\u00e9solution \u00e0 l\u2019amiable des cas de litige entre les parties implique le recours aux tribunaux congolais comp\u00e9tents pour r\u00e9gler le contentieux.</span><span style=\" font-family:'Arial "
                        "Narrow','sans-serif'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt;\">\u00a0</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; background-color:#ffffff;\">L'\u00e9diteur</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\"> </span></p>\n"
"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial Narrow','sans-serif'; font-size:12pt; color:#333333;\">\u00a9</span><span style=\" font-family:'Arial Narrow','sans-"
                        "serif'; font-size:12pt;\"> 2023, AR Intercom</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\"> </span></p></body></html>", None))
        self.iaggree.setText(QCoreApplication.translate("SigninWindow", u"J'accepte les termes de ce contrat.", None))
        self.cgu_2.setText(QCoreApplication.translate("SigninWindow", u"Change log", None))
        self.read_carefuly_2.setText(QCoreApplication.translate("SigninWindow", u"Quoi de neuf ?", None))
        self.next_feature.setText("")
        self.prev_feature.setText("")
        self.feature_0.setText("")
        self.feature_1.setText("")
        self.feature_2.setText("")
        self.feature_3.setText("")
        self.feature_4.setText("")
        self.feature_5.setText("")
        self.terminate.setText(QCoreApplication.translate("SigninWindow", u"Terminer", None))
        self.main_title.setText(QCoreApplication.translate("SigninWindow", u"Art Revolution Intercom", None))
        self.return_button.setText("")
    # retranslateUi

