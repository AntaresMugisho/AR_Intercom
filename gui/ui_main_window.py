# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)
from resources import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 796)
        MainWindow.setMinimumSize(QSize(1182, 796))
        icon = QIcon()
        icon.addFile(u":/icons/icons/ARsoftlogo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color:black;}")
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.actionAide = QAction(MainWindow)
        self.actionAide.setObjectName(u"actionAide")
        self.actionQuitter = QAction(MainWindow)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"/*  DEFAULT */\n"
"QWidget {\n"
"	color: rgb(250, 250, 250);\n"
"	selection-background-color: rgba(0, 150, 200, 50);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-repeat:no-repeat;\n"
"	background-position:center;\n"
"	border: none;\n"
"	outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 32, 33);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(51, 52, 53);\n"
"}\n"
"\n"
"#app_bg {\n"
"	background-color: #111;\n"
"	border: 2px solid #000;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"/* TITLE BAR */\n"
"#app_brand{\n"
"	border-bottom:1px dashed rgb(55, 56, 57);\n"
"}\n"
"\n"
"#title_bar{\n"
"	border-bottom: 2px dotted rgb(30, 32, 33);\n"
"}\n"
"\n"
"#settings_btn{\n"
"	background-image:url(:/cils/cils/icon_settings.png);\n"
"	border-radius: 8px\n"
"}\n"
"\n"
"#settings_btn:hover { \n"
"	background-color: rgb(31, 32, 33); \n"
"}\n"
"\n"
"#settings_btn:pressed { \n"
"	background-color: rgb(51, 52, 53); \n"
"}\n"
"\n"
"/*SYSTEM MENU*/\n"
"#system_menu{\n"
"    background-color"
                        ":rgb(31, 32, 33);\n"
"    border-bottom-left-radius:10px;\n"
"	border-top-right-radius:6px;\n"
"}\n"
"\n"
"#system_menu .QPushButton {\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"#system_menu .QPushButton:hover { \n"
"	background-color: rgb(11, 12, 13); \n"
"}\n"
"\n"
"#system_menu #minimize_btn{\n"
"	background-image: url(:/cils/cils/icon_minimize.png);\n"
"}\n"
"\n"
"#system_menu #minimize_btn:pressed{\n"
"	background-color:#fff000\n"
"}\n"
"\n"
"#system_menu #maximize_restore_btn{\n"
"	background-image: url(:/cils/cils/icon_maximize.png);\n"
"}\n"
"\n"
"#system_menu #maximize_restore_btn:pressed{\n"
"	background-color: #00dd00;\n"
"}\n"
"\n"
"#system_menu #close_btn{\n"
"	background-image: url(:/cils/cils/icon_close.png);\n"
"}\n"
"\n"
"#system_menu #close_btn:hover { \n"
"	background-color: #ff0000;\n"
"}\n"
"\n"
"\n"
"/*ASIDE MENU BAR */\n"
"\n"
"#left_menu {\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-right:2px solid rgb(30,32,33);\n"
"}\n"
"\n"
"#left_menu QPushButt"
                        "on{\n"
"	text-align:left;\n"
"	padding-left:42px;\n"
"	border-left:16px solid transparent;\n"
"	border-radius: 0px;\n"
"	background-position:center left;\n"
"}\n"
"#menu_btn{\n"
"	background-image: url(:/cils/cils/cil-list.png);\n"
"}\n"
"\n"
"#home_btn{\n"
"	background-image: url(:/cils/cils/cil-home.png);\n"
"}\n"
"\n"
"#scan_btn{\n"
"	background-image: url(:/svg/svg/icon_signal.svg);\n"
"}\n"
"\n"
"#chat_btn{\n"
"	background-image: url(:/cils/cils/cil-chat-bubble.png);\n"
"}\n"
"\n"
"#settings_btn_2{\n"
"    background-image:url(:/cils/cils/cil-settings.png);\n"
"}\n"
"\n"
"#about_btn{\n"
"	background-image: url(:/cils/cils/cil-at.png);\n"
"}\n"
"\n"
"/* LEFT SIDE - CHAT LIST */\n"
"\n"
"#left_side_container QWidget{\n"
"	background-color:rgb(21, 22, 23);\n"
"}\n"
"\n"
"/* Authenticated user info*/\n"
"#auth_user_container {\n"
"	background-color: rgb(21, 22, 23);\n"
"	border: none;\n"
"	border-bottom: 1px dashed rgb(47, 48, 50);\n"
"}\n"
"\n"
"#me_picture{\n"
"	border-radius:30px;\n"
"}\n"
"\n"
"#me_userna"
                        "me{\n"
"	color:rgba(255, 255, 255, 0.8);\n"
"}\n"
"\n"
"#me_status{\n"
"	color:rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"/* Search bar */\n"
"#search_bar {\n"
"	border: 2px solid rgb(47, 48, 50);\n"
"	border-radius: 15px;\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 30px;\n"
"	padding-right: 10px;\n"
"	background-image: url(:/svg/svg/icon_search.svg);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"\n"
"#search_bar:hover {\n"
"	color: rgb(230, 230, 230);\n"
"	border-color: rgb(62, 63, 66);\n"
"}\n"
"\n"
"#search_bar:focus {\n"
"	border-color: rgb(53, 54, 56);\n"
"	background-color: rgb(14, 14, 15);}\n"
"\n"
"/* Network signal indicator*/\n"
"#signal_status_container{\n"
"	border-top: 2px dotted rgb(30, 32, 33);\n"
"}\n"
"\n"
"#signal_icon {\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"}\n"
"\n"
"#signal_text{\n"
"	color: rgb(255, 255, 127);\n"
"}\n"
"\n"
"\n"
"/* CHAT */\n"
"\n"
"#chat_stacked_widget > QWidget{\n"
"	background-color:#111;\n"
""
                        "}\n"
"\n"
"/* Header */\n"
"#active_chat_header{\n"
"	background-color:rgb(30, 32, 33);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#active_chat_header QPushButton {\n"
"	background-color: rgb(47, 48, 50);\n"
"	border-radius: 18px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"\n"
"#active_chat_header QPushButton:hover {\n"
"	background-color: rgb(61, 62, 65);\n"
"}\n"
"\n"
"#active_chat_header QPushButton:pressed {\n"
"	background-color: rgb(16, 17, 18);\n"
"}\n"
"\n"
"#active_client_picture{\n"
"	border-radius:25px;\n"
"	background-color:rgb(20,21,22);\n"
"}\n"
"\n"
"#active_client_status{\n"
"	color: rgb(170, 170, 170);\n"
"}\n"
"\n"
"#last_seen{\n"
"	color: rgb(170, 170, 170);\n"
"}\n"
"\n"
"/*Chat scroll*/\n"
"#chat_scroll, #chat_scroll_widget{\n"
"	background:transparent;\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"/* Footer - Typing zone*/\n"
"#footer{\n"
"	background-color:rgb(30, 32, 33);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#footer QPushButton {\n"
"	background-color: rgb("
                        "47, 48, 50);\n"
"	border-radius: 20px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"\n"
"#footer QPushButton:hover {\n"
"	background-color: rgb(61, 62, 65);\n"
"}\n"
"\n"
"#footer QPushButton:pressed {\n"
"	background-color: rgb(16, 17, 18);\n"
"}\n"
"\n"
"#input_container, #record_widget{\n"
"	border-radius:25px;\n"
"	background-color:rgb(47, 48, 50);\n"
"}\n"
"\n"
"#input{\n"
"	border:none;\n"
"	background:transparent;\n"
"	color:white;\n"
"}\n"
"\n"
"/*Media buttons */\n"
"#media_bg{\n"
"	border-radius:23px;\n"
"	background:transparent;\n"
"}\n"
"#media_bg QPushButton{\n"
"	border-radius:20px;\n"
"	background-color:rgb(31, 32, 33);\n"
"	background-repeat:no-repeat;\n"
"	background-position:center;\n"
"}\n"
"\n"
"#media_bg QPushButton:hover{\n"
"	background-color:rgb(61, 62, 65);\n"
"}\n"
"\n"
"#media_bg QPushButton:pressed{\n"
"	background-color:rgb(16, 17, 18);\n"
"}\n"
"\n"
"/*Emoji widget*/\n"
"#emoji_widget{\n"
"		background-color: rgb(30,32,33);\n"
"		border-radius:8px"
                        ";\n"
"}\n"
"\n"
"#emoji_widget QTabWidget::pane {\n"
"	background-color:#000;\n"
"}\n"
"\n"
"#emoji_tab_widget QTabBar::tab{\n"
"    background-color:#222;\n"
"	width:35px;\n"
"	height:35px;\n"
"}\n"
"\n"
"#emoji_tab_widget QTabBar::tab:hover{\n"
"    background-color:#666;\n"
"}\n"
"\n"
"#emoji_tab_widget QTabBar::tab:selected{\n"
"	border-bottom:4px solid #111;\n"
"}\n"
"\n"
"#emoji_tab_widget QTabBar::tab:!selected{\n"
"	border-bottom:4px solid #222;\n"
"}\n"
"\n"
"#emoji_tab_widget QWidget{\n"
"	background-color:#111;\n"
"	border:none;\n"
"}\n"
"\n"
"/*RIGHT SIDE - SETTINGS */\n"
"\n"
"#right_stacked_widget > QWidget {\n"
"	border-left:3px solid rgb(30,32,33);\n"
"	background-color:rgb(21,22,23);\n"
"}\n"
"\n"
"#settings_stacked_widget > QWidget{\n"
"	background-color:rgb(21,22,23);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*SCROLL BARS*/\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
""
                        "QScrollBar::handle:horizontal {\n"
"    background: rgb(47, 48, 50);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border:none;\n"
"    background:rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 18"
                        "px 0 18px 0;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {\n"
"	background: rgb(47, 48, 50);\n"
"    min-height: 25px;\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"     background: rgb(47, 48, 50);\n"
"     height: 16px;\n"
"     border-bottom-left-radius:4px;\n"
"     border-bottom-right-radius:4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(47, 48, 50);\n"
"    height: 16px;\n"
"    border-top-left-radius:4px;\n"
"    border-top-right-radius:4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.main_window_layout = QVBoxLayout(self.stylesheet)
        self.main_window_layout.setSpacing(0)
        self.main_window_layout.setObjectName(u"main_window_layout")
        self.main_window_layout.setContentsMargins(0, 0, 0, 0)
        self.app_bg = QWidget(self.stylesheet)
        self.app_bg.setObjectName(u"app_bg")
        self.app_bg.setStyleSheet(u"")
        self.app_margins = QHBoxLayout(self.app_bg)
        self.app_margins.setSpacing(0)
        self.app_margins.setObjectName(u"app_margins")
        self.app_margins.setContentsMargins(3, 3, 3, 3)
        self.left_menu = QFrame(self.app_bg)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy)
        self.left_menu.setMinimumSize(QSize(60, 0))
        self.left_menu.setMaximumSize(QSize(172, 16777215))
        self.left_menu.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.app_brand = QWidget(self.left_menu)
        self.app_brand.setObjectName(u"app_brand")
        self.app_brand.setMinimumSize(QSize(161, 60))
        self.app_brand.setMaximumSize(QSize(16777215, 61))
        self.app_name = QLabel(self.app_brand)
        self.app_name.setObjectName(u"app_name")
        self.app_name.setGeometry(QRect(60, 1, 101, 51))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet(u"")
        self.app_logo = QLabel(self.app_brand)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setGeometry(QRect(9, 4, 41, 41))
        self.app_logo.setStyleSheet(u"image: url(:/icons/icons/ARsoftlogo.png);\n"
"")

        self.verticalLayout_2.addWidget(self.app_brand)

        self.menu_btn = QPushButton(self.left_menu)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMinimumSize(QSize(0, 50))
        self.menu_btn.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(10)
        self.menu_btn.setFont(font1)
        self.menu_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.menu_btn)

        self.home_btn = QPushButton(self.left_menu)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 50))
        self.home_btn.setMaximumSize(QSize(16777215, 50))
        self.home_btn.setFont(font1)
        self.home_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.home_btn)

        self.scan_btn = QPushButton(self.left_menu)
        self.scan_btn.setObjectName(u"scan_btn")
        self.scan_btn.setMinimumSize(QSize(0, 50))
        self.scan_btn.setMaximumSize(QSize(16777215, 50))
        self.scan_btn.setFont(font1)
        self.scan_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.scan_btn)

        self.chat_btn = QPushButton(self.left_menu)
        self.chat_btn.setObjectName(u"chat_btn")
        self.chat_btn.setMinimumSize(QSize(0, 50))
        self.chat_btn.setMaximumSize(QSize(16777215, 50))
        self.chat_btn.setFont(font1)
        self.chat_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.chat_btn)

        self.verticalSpacer = QSpacerItem(20, 296, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.about_btn = QPushButton(self.left_menu)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(0, 40))
        self.about_btn.setMaximumSize(QSize(16777215, 40))
        self.about_btn.setFont(font1)
        self.about_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.about_btn)


        self.app_margins.addWidget(self.left_menu)

        self.left_side_container = QStackedWidget(self.app_bg)
        self.left_side_container.setObjectName(u"left_side_container")
        self.left_side_container.setMaximumSize(QSize(290, 16777215))
        self.left_side_container.setStyleSheet(u"")
        self.contact_page = QWidget()
        self.contact_page.setObjectName(u"contact_page")
        self.verticalLayout_5 = QVBoxLayout(self.contact_page)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.auth_user_container = QWidget(self.contact_page)
        self.auth_user_container.setObjectName(u"auth_user_container")
        self.auth_user_container.setMinimumSize(QSize(291, 132))
        self.auth_user_container.setMaximumSize(QSize(291, 140))
        self.auth_user_container.setStyleSheet(u"")
        self.auth_user_box = QWidget(self.auth_user_container)
        self.auth_user_box.setObjectName(u"auth_user_box")
        self.auth_user_box.setGeometry(QRect(3, 4, 281, 71))
        self.auth_user_box.setStyleSheet(u"")
        self.me_picture = QLabel(self.auth_user_box)
        self.me_picture.setObjectName(u"me_picture")
        self.me_picture.setGeometry(QRect(3, 4, 61, 61))
        self.me_picture.setStyleSheet(u"border-image:url(:/icons/icons/avatar.png);\n"
"")
        self.me_picture.setScaledContents(True)
        self.me_online_toast = QLabel(self.auth_user_box)
        self.me_online_toast.setObjectName(u"me_online_toast")
        self.me_online_toast.setGeometry(QRect(50, 47, 16, 16))
        self.me_online_toast.setStyleSheet(u"QLabel{\n"
"	border-radius:8px;\n"
"	background-color: #00ff00;\n"
"}")
        self.me_online_toast.setFrameShadow(QFrame.Raised)
        self.me_status = QLabel(self.auth_user_box)
        self.me_status.setObjectName(u"me_status")
        self.me_status.setGeometry(QRect(79, 46, 191, 21))
        font2 = QFont()
        font2.setItalic(True)
        self.me_status.setFont(font2)
        self.me_status.setStyleSheet(u"")
        self.me_username = QLabel(self.auth_user_box)
        self.me_username.setObjectName(u"me_username")
        self.me_username.setGeometry(QRect(80, 27, 191, 21))
        self.me_username.setFont(font)
        self.me_username.setStyleSheet(u"")
        self.search_bar = QLineEdit(self.auth_user_container)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setGeometry(QRect(9, 89, 271, 31))
        self.search_bar.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.auth_user_container)

        self.contacts_stack = QStackedWidget(self.contact_page)
        self.contacts_stack.setObjectName(u"contacts_stack")
        self.contacts_stack.setMinimumSize(QSize(291, 491))
        self.contacts_stack.setMaximumSize(QSize(291, 16777215))
        self.contacts_stack.setStyleSheet(u"")
        self.chat_list_page = QWidget()
        self.chat_list_page.setObjectName(u"chat_list_page")
        self.chat_list_page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.chat_list_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.chat_list_scroll = QScrollArea(self.chat_list_page)
        self.chat_list_scroll.setObjectName(u"chat_list_scroll")
        self.chat_list_scroll.setMinimumSize(QSize(291, 491))
        self.chat_list_scroll.setMaximumSize(QSize(291, 16777215))
        self.chat_list_scroll.setStyleSheet(u"border:none;")
        self.chat_list_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chat_list_scroll.setWidgetResizable(True)
        self.chat_list_widget = QWidget()
        self.chat_list_widget.setObjectName(u"chat_list_widget")
        self.chat_list_widget.setGeometry(QRect(0, 0, 291, 491))
        self.chat_list_widget.setStyleSheet(u"")
        self.chat_list_layout = QVBoxLayout(self.chat_list_widget)
        self.chat_list_layout.setObjectName(u"chat_list_layout")
        self.client_info = QWidget(self.chat_list_widget)
        self.client_info.setObjectName(u"client_info")
        self.client_info.setMinimumSize(QSize(271, 61))
        self.client_info.setMaximumSize(QSize(271, 61))
        self.client_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_info.setStyleSheet(u"QWidget{\n"
"	border-radius:8px;\n"
"	background-color: rgba(50, 50, 50, 50);\n"
"}\n"
"\n"
"QWidget:hover{\n"
"	background-color: rgba(50, 50, 50, 255);\n"
"}\n"
"")
        self.msg_countrer = QLabel(self.client_info)
        self.msg_countrer.setObjectName(u"msg_countrer")
        self.msg_countrer.setGeometry(QRect(243, 7, 16, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(False)
        self.msg_countrer.setFont(font3)
        self.msg_countrer.setStyleSheet(u"QLabel{\n"
"	border-radius:8px;\n"
"	color: white;\n"
"	background-color: red;\n"
"}")
        self.msg_countrer.setFrameShadow(QFrame.Raised)
        self.client_picture = QLabel(self.client_info)
        self.client_picture.setObjectName(u"client_picture")
        self.client_picture.setGeometry(QRect(3, 3, 56, 56))
        self.client_picture.setStyleSheet(u"border-image: url(:/icons/icons/test.jpg);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"border-radius:28px;")
        self.client_picture.setPixmap(QPixmap(u":/image/1.png"))
        self.client_picture.setScaledContents(True)
        self.online_toast = QLabel(self.client_info)
        self.online_toast.setObjectName(u"online_toast")
        self.online_toast.setGeometry(QRect(47, 41, 12, 12))
        self.online_toast.setStyleSheet(u"QLabel{\n"
"	border-radius:6px;\n"
"	border:2px solid rgb(20,20,20);\n"
"	background-color: #00ff00;	\n"
"}")
        self.online_toast.setFrameShadow(QFrame.Raised)
        self.last_message = QLabel(self.client_info)
        self.last_message.setObjectName(u"last_message")
        self.last_message.setGeometry(QRect(70, 36, 131, 20))
        self.last_message.setFont(font1)
        self.last_message.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	color:rgba(255, 255, 255, 0.5);\n"
"}")
        self.client_name = QLabel(self.client_info)
        self.client_name.setObjectName(u"client_name")
        self.client_name.setGeometry(QRect(70, 6, 131, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.client_name.setFont(font4)
        self.client_name.setStyleSheet(u"QLabel{\n"
"	background-color:none;\n"
"	color: white;\n"
"}")
        self.messege_number = QLabel(self.client_info)
        self.messege_number.setObjectName(u"messege_number")
        self.messege_number.setGeometry(QRect(213, 23, 30, 20))
        font5 = QFont()
        font5.setPointSize(8)
        self.messege_number.setFont(font5)
        self.messege_number.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	color:rgba(255, 255, 255, 0.6);\n"
"\n"
"}")
        self.messege_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.envelop_msg = QFrame(self.client_info)
        self.envelop_msg.setObjectName(u"envelop_msg")
        self.envelop_msg.setGeometry(QRect(247, 27, 12, 12))
        self.envelop_msg.setStyleSheet(u"QFrame{\n"
"	background-color:transparent;\n"
"	image: url(:/cils/cils/cil-envelope-closed.png);\n"
"	border:none;}")
        self.envelop_msg.setFrameShape(QFrame.StyledPanel)
        self.envelop_msg.setFrameShadow(QFrame.Raised)
        self.last_seen_0 = QLabel(self.client_info)
        self.last_seen_0.setObjectName(u"last_seen_0")
        self.last_seen_0.setGeometry(QRect(198, 39, 61, 20))
        self.last_seen_0.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	color:rgb(0, 255, 0);\n"
"}")
        self.last_seen_0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.client_picture.raise_()
        self.msg_countrer.raise_()
        self.online_toast.raise_()
        self.last_message.raise_()
        self.client_name.raise_()
        self.messege_number.raise_()
        self.envelop_msg.raise_()
        self.last_seen_0.raise_()

        self.chat_list_layout.addWidget(self.client_info)

        self.client_info_2 = QWidget(self.chat_list_widget)
        self.client_info_2.setObjectName(u"client_info_2")
        self.client_info_2.setMinimumSize(QSize(271, 61))
        self.client_info_2.setMaximumSize(QSize(271, 61))
        self.client_info_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_info_2.setStyleSheet(u"#client_info_2{\n"
"	border-radius:8px;\n"
"	background-color: rgba(50, 50, 50, 50);\n"
"}\n"
"\n"
"#client_info_2:hover{\n"
"	background-color: rgba(50, 50, 50, 255);\n"
"}\n"
"")
        self.client_picture_3 = QLabel(self.client_info_2)
        self.client_picture_3.setObjectName(u"client_picture_3")
        self.client_picture_3.setGeometry(QRect(3, 3, 56, 56))
        self.client_picture_3.setStyleSheet(u"background-image: url(:/icons/icons/1.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"border-radius:28px;")
        self.client_picture_3.setPixmap(QPixmap(u":/image/1.png"))
        self.client_picture_3.setScaledContents(True)
        self.online_toast_3 = QLabel(self.client_info_2)
        self.online_toast_3.setObjectName(u"online_toast_3")
        self.online_toast_3.setGeometry(QRect(47, 41, 12, 12))
        self.online_toast_3.setStyleSheet(u"QLabel{\n"
"	border-radius:6px;\n"
"	border:2px solid rgb(20,20,20);\n"
"	background-color: gray;	\n"
"}")
        self.online_toast_3.setFrameShadow(QFrame.Raised)
        self.last_message_3 = QLabel(self.client_info_2)
        self.last_message_3.setObjectName(u"last_message_3")
        self.last_message_3.setGeometry(QRect(70, 36, 131, 20))
        self.last_message_3.setFont(font1)
        self.last_message_3.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	color:rgba(255, 255, 255, 0.5);\n"
"}")
        self.client_name_3 = QLabel(self.client_info_2)
        self.client_name_3.setObjectName(u"client_name_3")
        self.client_name_3.setGeometry(QRect(70, 6, 131, 31))
        self.client_name_3.setFont(font4)
        self.client_name_3.setStyleSheet(u"QLabel{\n"
"	background-color:none;\n"
"	color: white;\n"
"}")
        self.messege_number_5 = QLabel(self.client_info_2)
        self.messege_number_5.setObjectName(u"messege_number_5")
        self.messege_number_5.setGeometry(QRect(213, 23, 30, 20))
        self.messege_number_5.setFont(font5)
        self.messege_number_5.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	color:rgba(255, 255, 255, 0.6);\n"
"\n"
"}")
        self.messege_number_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.envelop_msg_3 = QFrame(self.client_info_2)
        self.envelop_msg_3.setObjectName(u"envelop_msg_3")
        self.envelop_msg_3.setGeometry(QRect(247, 27, 12, 12))
        self.envelop_msg_3.setStyleSheet(u"QFrame{\n"
"	background-color:transparent;\n"
"	image: url(:/cils/cils/cil-envelope-closed.png);\n"
"	border:none;}")
        self.envelop_msg_3.setFrameShape(QFrame.StyledPanel)
        self.envelop_msg_3.setFrameShadow(QFrame.Raised)
        self.last_seen_2 = QLabel(self.client_info_2)
        self.last_seen_2.setObjectName(u"last_seen_2")
        self.last_seen_2.setGeometry(QRect(198, 39, 61, 20))
        self.last_seen_2.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	color:rgb(255, 128, 0);\n"
"}")
        self.last_seen_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.chat_list_layout.addWidget(self.client_info_2)

        self.verticalSpacer_4 = QSpacerItem(1, 800, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.chat_list_layout.addItem(self.verticalSpacer_4)

        self.chat_list_scroll.setWidget(self.chat_list_widget)

        self.verticalLayout_4.addWidget(self.chat_list_scroll)

        self.contacts_stack.addWidget(self.chat_list_page)
        self.scan_page = QWidget()
        self.scan_page.setObjectName(u"scan_page")
        self.scan_page.setStyleSheet(u"background:transparent;")
        self.verticalLayout_29 = QVBoxLayout(self.scan_page)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(9, 9, 9, 9)
        self.scan_scroll = QScrollArea(self.scan_page)
        self.scan_scroll.setObjectName(u"scan_scroll")
        self.scan_scroll.setStyleSheet(u"QScrollArea{border:none;}")
        self.scan_scroll.setWidgetResizable(True)
        self.scan_widget = QWidget()
        self.scan_widget.setObjectName(u"scan_widget")
        self.scan_widget.setGeometry(QRect(0, 0, 273, 551))
        self.scan_list_layout = QVBoxLayout(self.scan_widget)
        self.scan_list_layout.setObjectName(u"scan_list_layout")
        self.scan_list_layout.setContentsMargins(0, 0, 0, 0)
        self.socket_info = QFrame(self.scan_widget)
        self.socket_info.setObjectName(u"socket_info")
        self.socket_info.setMinimumSize(QSize(0, 42))
        self.socket_info.setMaximumSize(QSize(16777215, 42))
        self.socket_info.setStyleSheet(u"#socket_info{background-color:rgb(16, 17, 18);\n"
"border-radius:21px;\n"
"}\n"
"\n"
"#device_icon{\n"
"	background-color:rgb(30, 32, 33);\n"
"	background-image: url(:/cils/cils/cil-screen-desktop.png);\n"
"	background-repeat:no-repeat;\n"
"	background-position:center;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}\n"
"\n"
"#host_name, #host_address{\n"
"	padding-left:5px;\n"
"	background-color:rgb(30, 32, 33);}\n"
"\n"
"	\n"
"#add_to_contact_btn{\n"
"	background-color:rgb(30, 32, 33);\n"
"	background-repeat:no-repeat;\n"
"	background-position:center;\n"
"	border-top-right-radius:20px;\n"
"	border-bottom-right-radius:20px;}\n"
"\n"
"#add_to_contact_btn:hover{\n"
"	background-color:rgb(56, 57, 58);}\n"
"\n"
"#add_to_contact_btn:pressed{\n"
"	background-color:rgb(27, 28, 29);}")
        self.horizontalLayout_4 = QHBoxLayout(self.socket_info)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 1, 0, 1)
        self.device_icon = QLabel(self.socket_info)
        self.device_icon.setObjectName(u"device_icon")
        self.device_icon.setMinimumSize(QSize(40, 40))
        self.device_icon.setMaximumSize(QSize(40, 40))
        self.device_icon.setStyleSheet(u"")
        self.device_icon.setPixmap(QPixmap(u":/image/1.png"))
        self.device_icon.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.device_icon)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.host_name = QLabel(self.socket_info)
        self.host_name.setObjectName(u"host_name")
        self.host_name.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.host_name)

        self.host_address = QLabel(self.socket_info)
        self.host_address.setObjectName(u"host_address")
        self.host_address.setStyleSheet(u"color:gray;")
        self.host_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.host_address)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.add_to_contact_btn = QPushButton(self.socket_info)
        self.add_to_contact_btn.setObjectName(u"add_to_contact_btn")
        self.add_to_contact_btn.setMinimumSize(QSize(40, 40))
        self.add_to_contact_btn.setMaximumSize(QSize(40, 40))
        self.add_to_contact_btn.setStyleSheet(u"background-image: url(:/cils/cils/cil-user-follow.png);\n"
"")

        self.horizontalLayout_4.addWidget(self.add_to_contact_btn)

        self.add_to_contact_btn.raise_()
        self.device_icon.raise_()

        self.scan_list_layout.addWidget(self.socket_info)

        self.verticalSpacer_7 = QSpacerItem(20, 526, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.scan_list_layout.addItem(self.verticalSpacer_7)

        self.scan_scroll.setWidget(self.scan_widget)

        self.verticalLayout_29.addWidget(self.scan_scroll)

        self.start_scan_btn = QPushButton(self.scan_page)
        self.start_scan_btn.setObjectName(u"start_scan_btn")
        self.start_scan_btn.setMinimumSize(QSize(261, 40))
        self.start_scan_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(21, 22, 23);\n"
"	border-radius:20px;\n"
"	padding:8px;\n"
"	border:2px solid rgb(31,32,33);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 32, 33);\n"
"	border:2px solid rgb(21,22,23);\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(51, 52, 53);\n"
"}\n"
"")

        self.verticalLayout_29.addWidget(self.start_scan_btn)

        self.contacts_stack.addWidget(self.scan_page)

        self.verticalLayout_5.addWidget(self.contacts_stack)

        self.signal_status_container = QFrame(self.contact_page)
        self.signal_status_container.setObjectName(u"signal_status_container")
        self.signal_status_container.setMinimumSize(QSize(291, 41))
        self.signal_status_container.setMaximumSize(QSize(291, 41))
        self.signal_status_container.setStyleSheet(u"")
        self.signal_icon = QFrame(self.signal_status_container)
        self.signal_icon.setObjectName(u"signal_icon")
        self.signal_icon.setGeometry(QRect(10, 7, 21, 31))
        self.signal_icon.setStyleSheet(u"background-image: url(:/cils/cils/cil-rss.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;")
        self.signal_icon.setFrameShape(QFrame.StyledPanel)
        self.signal_icon.setFrameShadow(QFrame.Raised)
        self.signal_text = QLabel(self.signal_status_container)
        self.signal_text.setObjectName(u"signal_text")
        self.signal_text.setGeometry(QRect(39, 11, 241, 23))
        font6 = QFont()
        font6.setBold(True)
        self.signal_text.setFont(font6)

        self.verticalLayout_5.addWidget(self.signal_status_container)

        self.left_side_container.addWidget(self.contact_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_6 = QLabel(self.about_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 740, 221, 61))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.left_side_container.addWidget(self.about_page)

        self.app_margins.addWidget(self.left_side_container)

        self.right_side_container = QWidget(self.app_bg)
        self.right_side_container.setObjectName(u"right_side_container")
        self.right_side_container.setMinimumSize(QSize(651, 696))
        self.right_side_container.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.right_side_container)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QWidget(self.right_side_container)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 61))
        self.title_bar.setMaximumSize(QSize(16777215, 61))
        self.title_bar.setStyleSheet(u"#widget_5{\n"
"	border-bottom:1px dashed rgb(55, 56, 57);	\n"
"}")
        self.title_bar_layout = QHBoxLayout(self.title_bar)
        self.title_bar_layout.setObjectName(u"title_bar_layout")
        self.title_bar_layout.setContentsMargins(12, 0, 0, 0)
        self.app_title = QLabel(self.title_bar)
        self.app_title.setObjectName(u"app_title")
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.app_title.setFont(font7)
        self.app_title.setStyleSheet(u"")

        self.title_bar_layout.addWidget(self.app_title)

        self.title_bar_spacer = QSpacerItem(2, 2, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.title_bar_layout.addItem(self.title_bar_spacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.systel_menu_layout = QHBoxLayout()
        self.systel_menu_layout.setSpacing(18)
        self.systel_menu_layout.setObjectName(u"systel_menu_layout")
        self.settings_btn = QPushButton(self.title_bar)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(28, 28))
        self.settings_btn.setMaximumSize(QSize(28, 28))
        self.settings_btn.setStyleSheet(u"")

        self.systel_menu_layout.addWidget(self.settings_btn)

        self.system_menu = QWidget(self.title_bar)
        self.system_menu.setObjectName(u"system_menu")
        self.system_menu.setMinimumSize(QSize(92, 31))
        self.system_menu.setMaximumSize(QSize(92, 31))
        self.system_menu.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.system_menu)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.system_menu)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(28, 28))
        self.minimize_btn.setMaximumSize(QSize(28, 28))
        self.minimize_btn.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.minimize_btn)

        self.maximize_restore_btn = QPushButton(self.system_menu)
        self.maximize_restore_btn.setObjectName(u"maximize_restore_btn")
        self.maximize_restore_btn.setMinimumSize(QSize(28, 28))
        self.maximize_restore_btn.setMaximumSize(QSize(28, 28))
        self.maximize_restore_btn.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.maximize_restore_btn)

        self.close_btn = QPushButton(self.system_menu)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(28, 28))
        self.close_btn.setMaximumSize(QSize(28, 28))
        self.close_btn.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.close_btn)


        self.systel_menu_layout.addWidget(self.system_menu)


        self.verticalLayout_8.addLayout(self.systel_menu_layout)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.title_bar_layout.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addWidget(self.title_bar)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.chat_stacked_widget = QStackedWidget(self.right_side_container)
        self.chat_stacked_widget.setObjectName(u"chat_stacked_widget")
        self.chat_stacked_widget.setMinimumSize(QSize(585, 581))
        self.chat_stacked_widget.setStyleSheet(u"")
        self.widgets_page = QWidget()
        self.widgets_page.setObjectName(u"widgets_page")
        self.bubble_container_2 = QFrame(self.widgets_page)
        self.bubble_container_2.setObjectName(u"bubble_container_2")
        self.bubble_container_2.setGeometry(QRect(120, 20, 120, 71))
        sizePolicy.setHeightForWidth(self.bubble_container_2.sizePolicy().hasHeightForWidth())
        self.bubble_container_2.setSizePolicy(sizePolicy)
        self.bubble_container_2.setMinimumSize(QSize(120, 71))
        self.bubble_container_2.setStyleSheet(u"")
        self.bubble_container_2.setFrameShape(QFrame.StyledPanel)
        self.bubble_container_2.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.bubble_container_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(96, 8, 14, 14))
        self.frame_7.setStyleSheet(u"	background-color: rgba(51, 153, 204, .7);\n"
"border-radius:7px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.bubble_container_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(107, 2, 8, 8))
        self.frame_8.setStyleSheet(u"background-color: rgb(51, 153, 204);\n"
"border-radius:4px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.bubble_container_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(2, 15, 101, 51))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setStyleSheet(u"	border-radius:20px;\n"
"	border-top-right-radius:8px;\n"
"	background-color: rgb(51, 153, 204);\n"
"\n"
"	\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_9)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(12, 6, 12, 0)
        self.left_bubble_3 = QLabel(self.frame_9)
        self.left_bubble_3.setObjectName(u"left_bubble_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_bubble_3.sizePolicy().hasHeightForWidth())
        self.left_bubble_3.setSizePolicy(sizePolicy2)
        self.left_bubble_3.setMaximumSize(QSize(304, 16777215))
        self.left_bubble_3.setFont(font4)
        self.left_bubble_3.setStyleSheet(u"QLabel{\n"
"	color: #000;\n"
"    background-color:transparent;\n"
"}")
        self.left_bubble_3.setScaledContents(False)
        self.left_bubble_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.left_bubble_3.setWordWrap(True)
        self.left_bubble_3.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_6.addWidget(self.left_bubble_3, 0, 0, 1, 2)

        self.horizontalSpacer_11 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.time_3 = QLabel(self.frame_9)
        self.time_3.setObjectName(u"time_3")
        self.time_3.setMinimumSize(QSize(31, 14))
        self.time_3.setMaximumSize(QSize(31, 14))
        self.time_3.setFont(font5)
        self.time_3.setStyleSheet(u"\n"
"color:#ddd;\n"
"border-radius:7px;\n"
"background-color:transparent;\n"
"")
        self.time_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.time_3)

        self.ticks_3 = QLabel(self.frame_9)
        self.ticks_3.setObjectName(u"ticks_3")
        self.ticks_3.setMinimumSize(QSize(24, 14))
        self.ticks_3.setMaximumSize(QSize(24, 14))
        font8 = QFont()
        font8.setPointSize(7)
        self.ticks_3.setFont(font8)
        self.ticks_3.setStyleSheet(u"\n"
"image: url(:/cils/cils/cil-check-circle-green.png);\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding:1px;")
        self.ticks_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.ticks_3)


        self.gridLayout_6.addLayout(self.horizontalLayout_18, 1, 1, 1, 1)

        self.left_msg_frame_2 = QFrame(self.widgets_page)
        self.left_msg_frame_2.setObjectName(u"left_msg_frame_2")
        self.left_msg_frame_2.setGeometry(QRect(10, 10, 120, 71))
        self.left_msg_frame_2.setMinimumSize(QSize(120, 71))
        self.left_msg_frame_2.setStyleSheet(u"")
        self.left_msg_frame_2.setFrameShape(QFrame.StyledPanel)
        self.left_msg_frame_2.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.left_msg_frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(10, 10, 14, 14))
        self.frame_16.setStyleSheet(u"\n"
"border-radius:7px;\n"
"background-color: rgba(255, 170, 0, .7);\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.left_msg_frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(5, 4, 8, 8))
        self.frame_17.setStyleSheet(u"border-radius:4px;\n"
"background-color: rgb(255, 170, 0);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.left_msg_frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(17, 17, 81, 51))
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setStyleSheet(u"	border-radius:20px;\n"
"	border-top-left-radius:8px;\n"
"	background-color: rgb(255, 170, 0);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_18)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(12, 6, 12, 0)
        self.left_bubble_4 = QLabel(self.frame_18)
        self.left_bubble_4.setObjectName(u"left_bubble_4")
        sizePolicy2.setHeightForWidth(self.left_bubble_4.sizePolicy().hasHeightForWidth())
        self.left_bubble_4.setSizePolicy(sizePolicy2)
        self.left_bubble_4.setMaximumSize(QSize(304, 16777215))
        self.left_bubble_4.setFont(font4)
        self.left_bubble_4.setStyleSheet(u"QLabel{\n"
"	color: #f1f1f1;\n"
"background-color:transparent;\n"
"}")
        self.left_bubble_4.setScaledContents(False)
        self.left_bubble_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.left_bubble_4.setWordWrap(True)
        self.left_bubble_4.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.left_bubble_4, 0, 0, 1, 2)

        self.horizontalSpacer_12 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_12, 1, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.time_6 = QLabel(self.frame_18)
        self.time_6.setObjectName(u"time_6")
        self.time_6.setMinimumSize(QSize(31, 14))
        self.time_6.setMaximumSize(QSize(31, 14))
        self.time_6.setFont(font5)
        self.time_6.setStyleSheet(u"QLabel{\n"
"color:#999;\n"
"border-radius:7px;\n"
"}")
        self.time_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.time_6)


        self.gridLayout_7.addLayout(self.horizontalLayout_19, 1, 1, 1, 1)

        self.left_msg_frame_5 = QFrame(self.widgets_page)
        self.left_msg_frame_5.setObjectName(u"left_msg_frame_5")
        self.left_msg_frame_5.setGeometry(QRect(10, 100, 320, 111))
        self.left_msg_frame_5.setMinimumSize(QSize(320, 111))
        self.left_msg_frame_5.setStyleSheet(u"")
        self.left_msg_frame_5.setFrameShape(QFrame.StyledPanel)
        self.left_msg_frame_5.setFrameShadow(QFrame.Raised)
        self.frame_19 = QFrame(self.left_msg_frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(5, 4, 8, 8))
        self.frame_19.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"border-radius:4px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.left_msg_frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 10, 14, 14))
        self.frame_20.setStyleSheet(u"background-color: rgba(255, 170, 0, .7);\n"
"border-radius:7px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_21 = QFrame(self.left_msg_frame_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(17, 17, 304, 91))
        self.frame_21.setMaximumSize(QSize(304, 16777215))
        self.frame_21.setStyleSheet(u"	border-radius:10px;\n"
"	border-top-left-radius:8px;\n"
"	background-color: rgb(255, 170, 0);\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_21)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(1, 1, 1, 0)
        self.horizontalSpacer_13 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 1, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.time_7 = QLabel(self.frame_21)
        self.time_7.setObjectName(u"time_7")
        self.time_7.setMinimumSize(QSize(31, 14))
        self.time_7.setMaximumSize(QSize(31, 14))
        self.time_7.setFont(font5)
        self.time_7.setStyleSheet(u"QLabel{\n"
"color:#ddd;\n"
"border-radius:7px;\n"
"}")
        self.time_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.time_7)


        self.gridLayout_8.addLayout(self.horizontalLayout_20, 1, 1, 1, 1)

        self.arv_bubble_3 = QFrame(self.frame_21)
        self.arv_bubble_3.setObjectName(u"arv_bubble_3")
        self.arv_bubble_3.setMinimumSize(QSize(300, 70))
        self.arv_bubble_3.setMaximumSize(QSize(300, 70))
        self.arv_bubble_3.setStyleSheet(u"QFrame{\n"
"	background-color:#88FFFFFF;\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.arv_bubble_3.setFrameShape(QFrame.StyledPanel)
        self.arv_bubble_3.setFrameShadow(QFrame.Raised)
        self.title_3 = QLabel(self.arv_bubble_3)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(52, 3, 241, 20))
        self.title_3.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"    color:#000;\n"
"}")
        self.title_3.setAlignment(Qt.AlignCenter)
        self.title_3.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.elapsed_time_3 = QLabel(self.arv_bubble_3)
        self.elapsed_time_3.setObjectName(u"elapsed_time_3")
        self.elapsed_time_3.setGeometry(QRect(52, 49, 51, 16))
        self.elapsed_time_3.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"    color:#333;\n"
"	border-radius:8px;\n"
"}")
        self.elapsed_time_3.setAlignment(Qt.AlignCenter)
        self.total_time_3 = QLabel(self.arv_bubble_3)
        self.total_time_3.setObjectName(u"total_time_3")
        self.total_time_3.setGeometry(QRect(241, 49, 51, 16))
        self.total_time_3.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"    color:#333;\n"
"	border-radius:8px;\n"
"}")
        self.total_time_3.setAlignment(Qt.AlignCenter)
        self.slider_3 = QSlider(self.arv_bubble_3)
        self.slider_3.setObjectName(u"slider_3")
        self.slider_3.setGeometry(QRect(52, 30, 241, 12))
        self.slider_3.setStyleSheet(u"QSlider{\n"
"            background:none;}\n"
"    \n"
"        QSlider::groove:horizontal{ \n"
"            height:4px;\n"
"            border:none;}\n"
"        \n"
"        QSlider::handle:horizontal{\n"
"            height:12px;\n"
"            width:12px;\n"
"            border-radius:6px;\n"
"            margin:-4px 0px -4px 0px;\n"
"            background-color: rgba(0, 121, 215, 255);}\n"
"            \n"
"        QSlider::handle:hover{\n"
"            background-color: rgba(0, 52, 93, 255);}\n"
"        \n"
"        QSlider::handle:pressed{\n"
"            background-color: rgba(0, 121, 215, 255);}\n"
"        \n"
"        QSlider::add-page:horizontal{\n"
"            background-color:#55FFFFFF;}\n"
"        \n"
"        QSlider::sub-page:horizontal{\n"
"            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"            stop:0 rgba(0, 52, 93, 255), stop:1 rgba(0, 121, 215, 255));}")
        self.slider_3.setMaximum(100)
        self.slider_3.setValue(0)
        self.slider_3.setSliderPosition(0)
        self.slider_3.setOrientation(Qt.Horizontal)
        self.play_button_3 = QPushButton(self.arv_bubble_3)
        self.play_button_3.setObjectName(u"play_button_3")
        self.play_button_3.setGeometry(QRect(7, 16, 41, 41))
        self.play_button_3.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/cils/cils/cil-media-play.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position:center;\n"
"	border-radius:6px;\n"
"	border:none;\n"
"}\n"
"QPushButton::hover{\n"
"    border:1px inset rgba(255, 255, 255, 0.6);\n"
"}\n"
"        \n"
"QPushButton::pressed{\n"
"     border:2px inset rgba(255, 255, 255, 1);\n"
"}")

        self.gridLayout_8.addWidget(self.arv_bubble_3, 0, 0, 1, 1)

        self.left_msg_frame_6 = QFrame(self.widgets_page)
        self.left_msg_frame_6.setObjectName(u"left_msg_frame_6")
        self.left_msg_frame_6.setGeometry(QRect(30, 230, 320, 111))
        self.left_msg_frame_6.setMinimumSize(QSize(320, 111))
        self.left_msg_frame_6.setStyleSheet(u"")
        self.left_msg_frame_6.setFrameShape(QFrame.StyledPanel)
        self.left_msg_frame_6.setFrameShadow(QFrame.Raised)
        self.frame_22 = QFrame(self.left_msg_frame_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(297, 8, 14, 14))
        self.frame_22.setStyleSheet(u"	background-color: rgba(51, 153, 204, .7);\n"
"border-radius:7px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.left_msg_frame_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(308, 2, 8, 8))
        self.frame_23.setStyleSheet(u"background-color: rgb(51, 153, 204);\n"
"border-radius:4px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_24 = QFrame(self.left_msg_frame_6)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(2, 15, 302, 91))
        sizePolicy1.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy1)
        self.frame_24.setStyleSheet(u"	border-radius:10px;\n"
"	border-top-right-radius:8px;\n"
"	background-color: rgb(51, 153, 204);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_24)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(1, 1, 1, 0)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.time_8 = QLabel(self.frame_24)
        self.time_8.setObjectName(u"time_8")
        self.time_8.setMinimumSize(QSize(31, 14))
        self.time_8.setMaximumSize(QSize(31, 14))
        self.time_8.setFont(font5)
        self.time_8.setStyleSheet(u"QLabel{\n"
"color:#ddd;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.time_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.time_8)

        self.ticks_5 = QLabel(self.frame_24)
        self.ticks_5.setObjectName(u"ticks_5")
        self.ticks_5.setMinimumSize(QSize(24, 14))
        self.ticks_5.setMaximumSize(QSize(24, 14))
        self.ticks_5.setFont(font8)
        self.ticks_5.setStyleSheet(u"\n"
"image: url(:/cils/cils/cil-check-circle-green.png);\n"
"background-color:rgba(255, 255, 255, 1);\n"
"border-radius:7px;\n"
"padding:1px;")
        self.ticks_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.ticks_5)


        self.gridLayout_9.addLayout(self.horizontalLayout_21, 1, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_14, 1, 0, 1, 1)

        self.arv_bubble_4 = QFrame(self.frame_24)
        self.arv_bubble_4.setObjectName(u"arv_bubble_4")
        self.arv_bubble_4.setMinimumSize(QSize(300, 70))
        self.arv_bubble_4.setMaximumSize(QSize(300, 70))
        self.arv_bubble_4.setStyleSheet(u"QFrame{\n"
"	background-color:#88FFFFFF;\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.arv_bubble_4.setFrameShape(QFrame.StyledPanel)
        self.arv_bubble_4.setFrameShadow(QFrame.Raised)
        self.title_4 = QLabel(self.arv_bubble_4)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(52, 3, 241, 20))
        self.title_4.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"    color:#000;\n"
"}")
        self.title_4.setAlignment(Qt.AlignCenter)
        self.title_4.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.elapsed_time_4 = QLabel(self.arv_bubble_4)
        self.elapsed_time_4.setObjectName(u"elapsed_time_4")
        self.elapsed_time_4.setGeometry(QRect(52, 49, 51, 16))
        self.elapsed_time_4.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"    color:#333;\n"
"	border-radius:8px;\n"
"}")
        self.elapsed_time_4.setAlignment(Qt.AlignCenter)
        self.total_time_4 = QLabel(self.arv_bubble_4)
        self.total_time_4.setObjectName(u"total_time_4")
        self.total_time_4.setGeometry(QRect(241, 49, 51, 16))
        self.total_time_4.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"    color:#333;\n"
"	border-radius:8px;\n"
"}")
        self.total_time_4.setAlignment(Qt.AlignCenter)
        self.slider_4 = QSlider(self.arv_bubble_4)
        self.slider_4.setObjectName(u"slider_4")
        self.slider_4.setGeometry(QRect(52, 30, 241, 12))
        self.slider_4.setStyleSheet(u"QSlider{\n"
"            background:none;}\n"
"    \n"
"        QSlider::groove:horizontal{ \n"
"            height:4px;\n"
"            border:none;}\n"
"        \n"
"        QSlider::handle:horizontal{\n"
"            height:12px;\n"
"            width:12px;\n"
"            border-radius:6px;\n"
"            margin:-4px 0px -4px 0px;\n"
"            background-color: rgba(0, 121, 215, 255);}\n"
"            \n"
"        QSlider::handle:hover{\n"
"            background-color: rgba(0, 52, 93, 255);}\n"
"        \n"
"        QSlider::handle:pressed{\n"
"            background-color: rgba(0, 121, 215, 255);}\n"
"        \n"
"        QSlider::add-page:horizontal{\n"
"            background-color:#55FFFFFF;}\n"
"        \n"
"        QSlider::sub-page:horizontal{\n"
"            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"            stop:0 rgba(0, 52, 93, 255), stop:1 rgba(0, 121, 215, 255));}")
        self.slider_4.setMaximum(100)
        self.slider_4.setValue(0)
        self.slider_4.setSliderPosition(0)
        self.slider_4.setOrientation(Qt.Horizontal)
        self.play_button_4 = QPushButton(self.arv_bubble_4)
        self.play_button_4.setObjectName(u"play_button_4")
        self.play_button_4.setGeometry(QRect(7, 16, 41, 41))
        self.play_button_4.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/cils/cils/cil-media-play.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position:center;\n"
"	border-radius:6px;\n"
"	border:none;\n"
"}\n"
"QPushButton::hover{\n"
"    border:1px inset rgba(255, 255, 255, 0.6);\n"
"}\n"
"        \n"
"QPushButton::pressed{\n"
"     border:2px inset rgba(255, 255, 255, 1);\n"
"}")

        self.gridLayout_9.addWidget(self.arv_bubble_4, 0, 0, 1, 1)

        self.document_bubble_frame = QFrame(self.widgets_page)
        self.document_bubble_frame.setObjectName(u"document_bubble_frame")
        self.document_bubble_frame.setGeometry(QRect(350, 110, 201, 101))
        self.document_bubble_frame.setMinimumSize(QSize(201, 101))
        self.document_bubble_frame.setStyleSheet(u"")
        self.document_bubble_frame.setFrameShape(QFrame.StyledPanel)
        self.document_bubble_frame.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.document_bubble_frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(5, 4, 8, 8))
        self.frame_25.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"border-radius:4px;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_26 = QFrame(self.document_bubble_frame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(10, 10, 14, 14))
        self.frame_26.setStyleSheet(u"background-color: rgba(255, 170, 0, .7);\n"
"border-radius:7px;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.document_bubble = QFrame(self.document_bubble_frame)
        self.document_bubble.setObjectName(u"document_bubble")
        self.document_bubble.setGeometry(QRect(17, 17, 181, 71))
        self.document_bubble.setStyleSheet(u"	border-radius:10px;\n"
"	border-top-left-radius:8px;\n"
"	background-color: rgb(255, 170, 0);\n"
"")
        self.document_bubble.setFrameShape(QFrame.StyledPanel)
        self.document_bubble.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.document_bubble)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 1, 2, 0)
        self.document = QFrame(self.document_bubble)
        self.document.setObjectName(u"document")
        self.document.setStyleSheet(u".QFrame{\n"
"	background-color:#88FFFFFF;\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.document.setFrameShape(QFrame.StyledPanel)
        self.document.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.document)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 6, 9, 6)
        self.document_icon = QLabel(self.document)
        self.document_icon.setObjectName(u"document_icon")
        self.document_icon.setMinimumSize(QSize(35, 35))
        self.document_icon.setMaximumSize(QSize(35, 35))
        font9 = QFont()
        font9.setPointSize(8)
        font9.setBold(True)
        self.document_icon.setFont(font9)
        self.document_icon.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: #bbb;\n"
"	border-radius:4px;\n"
"    color:#fff;\n"
"	image: url(:/cils/cils/blacks/cil-file.png);\n"
"}")
        self.document_icon.setAlignment(Qt.AlignCenter)
        self.document_icon.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_23.addWidget(self.document_icon)

        self.document_title_size_layout = QVBoxLayout()
        self.document_title_size_layout.setSpacing(0)
        self.document_title_size_layout.setObjectName(u"document_title_size_layout")
        self.document_title = QLabel(self.document)
        self.document_title.setObjectName(u"document_title")
        self.document_title.setFont(font6)
        self.document_title.setStyleSheet(u"QLabel{\n"
"    color:#000;\n"
"background-color:transparent;\n"
"}")
        self.document_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.document_title.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.document_title_size_layout.addWidget(self.document_title)

        self.document_size = QLabel(self.document)
        self.document_size.setObjectName(u"document_size")
        self.document_size.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"    color:gray;\n"
"}")
        self.document_size.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.document_size.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.document_title_size_layout.addWidget(self.document_size)


        self.horizontalLayout_23.addLayout(self.document_title_size_layout)


        self.verticalLayout_17.addWidget(self.document)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_16 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)

        self.time_9 = QLabel(self.document_bubble)
        self.time_9.setObjectName(u"time_9")
        self.time_9.setMinimumSize(QSize(31, 14))
        self.time_9.setMaximumSize(QSize(31, 14))
        self.time_9.setFont(font5)
        self.time_9.setStyleSheet(u"QLabel{\n"
"color:#ddd;\n"
"border-radius:7px;\n"
"}")
        self.time_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.time_9)


        self.verticalLayout_17.addLayout(self.horizontalLayout_24)

        self.left_msg_frame_8 = QFrame(self.widgets_page)
        self.left_msg_frame_8.setObjectName(u"left_msg_frame_8")
        self.left_msg_frame_8.setGeometry(QRect(370, 220, 201, 101))
        self.left_msg_frame_8.setStyleSheet(u"")
        self.left_msg_frame_8.setFrameShape(QFrame.StyledPanel)
        self.left_msg_frame_8.setFrameShadow(QFrame.Raised)
        self.frame_28 = QFrame(self.left_msg_frame_8)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(178, 8, 14, 14))
        self.frame_28.setStyleSheet(u"	background-color: rgba(51, 153, 204, .7);\n"
"border-radius:7px;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_29 = QFrame(self.left_msg_frame_8)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(189, 2, 8, 8))
        self.frame_29.setStyleSheet(u"background-color: rgb(51, 153, 204);\n"
"border-radius:4px;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.frame_30 = QFrame(self.left_msg_frame_8)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(4, 15, 181, 71))
        sizePolicy1.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy1)
        self.frame_30.setMaximumSize(QSize(181, 81))
        self.frame_30.setStyleSheet(u"	border-radius:10px;\n"
"	border-top-right-radius:8px;\n"
"	background-color: rgb(51, 153, 204);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_30)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(2, 1, 2, 0)
        self.arv_bubble_6 = QFrame(self.frame_30)
        self.arv_bubble_6.setObjectName(u"arv_bubble_6")
        self.arv_bubble_6.setStyleSheet(u".QFrame{\n"
"	background-color:#88FFFFFF;\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.arv_bubble_6.setFrameShape(QFrame.StyledPanel)
        self.arv_bubble_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.arv_bubble_6)
        self.horizontalLayout_26.setSpacing(6)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(9, 6, 9, 6)
        self.title_8 = QLabel(self.arv_bubble_6)
        self.title_8.setObjectName(u"title_8")
        self.title_8.setMinimumSize(QSize(35, 35))
        self.title_8.setMaximumSize(QSize(35, 35))
        self.title_8.setFont(font9)
        self.title_8.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: #bbb;\n"
"	border-radius:4px;\n"
"    color:#fff;\n"
"	image: url(:/cils/cils/blacks/cil-file.png);\n"
"}")
        self.title_8.setAlignment(Qt.AlignCenter)
        self.title_8.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_26.addWidget(self.title_8)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.title_9 = QLabel(self.arv_bubble_6)
        self.title_9.setObjectName(u"title_9")
        self.title_9.setFont(font6)
        self.title_9.setStyleSheet(u"QLabel{\n"
"    color:#000;\n"
"background-color:transparent;\n"
"}")
        self.title_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.title_9.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_18.addWidget(self.title_9)

        self.title_10 = QLabel(self.arv_bubble_6)
        self.title_10.setObjectName(u"title_10")
        self.title_10.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"    color:gray;\n"
"}")
        self.title_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.title_10.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_18.addWidget(self.title_10)


        self.horizontalLayout_26.addLayout(self.verticalLayout_18)


        self.verticalLayout_19.addWidget(self.arv_bubble_6)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_15 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_15)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.time_10 = QLabel(self.frame_30)
        self.time_10.setObjectName(u"time_10")
        self.time_10.setMinimumSize(QSize(31, 14))
        self.time_10.setMaximumSize(QSize(31, 14))
        self.time_10.setFont(font5)
        self.time_10.setStyleSheet(u"QLabel{\n"
"color:#ddd;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.time_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.time_10)

        self.ticks_6 = QLabel(self.frame_30)
        self.ticks_6.setObjectName(u"ticks_6")
        self.ticks_6.setMinimumSize(QSize(24, 14))
        self.ticks_6.setMaximumSize(QSize(24, 14))
        self.ticks_6.setFont(font8)
        self.ticks_6.setStyleSheet(u"\n"
"image: url(:/cils/cils/cil-check-circle-green.png);\n"
"background-color:rgba(255, 255, 255, 1);\n"
"border-radius:7px;\n"
"padding:1px;")
        self.ticks_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.ticks_6)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_22)


        self.verticalLayout_19.addLayout(self.horizontalLayout_25)

        self.left_msg_frame_9 = QFrame(self.widgets_page)
        self.left_msg_frame_9.setObjectName(u"left_msg_frame_9")
        self.left_msg_frame_9.setGeometry(QRect(290, 350, 221, 221))
        self.left_msg_frame_9.setStyleSheet(u"")
        self.left_msg_frame_9.setFrameShape(QFrame.StyledPanel)
        self.left_msg_frame_9.setFrameShadow(QFrame.Raised)
        self.frame_31 = QFrame(self.left_msg_frame_9)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(193, 10, 14, 14))
        self.frame_31.setStyleSheet(u"	background-color: rgba(51, 153, 204, .7);\n"
"border-radius:7px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.frame_32 = QFrame(self.left_msg_frame_9)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(204, 4, 8, 8))
        self.frame_32.setStyleSheet(u"background-color: rgb(51, 153, 204);\n"
"border-radius:4px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.frame_33 = QFrame(self.left_msg_frame_9)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(4, 17, 198, 201))
        self.frame_33.setStyleSheet(u"	border-radius:10px;\n"
"	border-top-right-radius:8px;\n"
"	background-color: rgb(51, 153, 204);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_33)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 2, 2, 0)
        self.title_12 = QLabel(self.frame_33)
        self.title_12.setObjectName(u"title_12")
        self.title_12.setMinimumSize(QSize(180, 180))
        self.title_12.setMaximumSize(QSize(16777215, 180))
        font10 = QFont()
        font10.setBold(False)
        self.title_12.setFont(font10)
        self.title_12.setStyleSheet(u"QLabel{\n"
"	border-radius:10px;\n"
"	border-image: url(:/icons/icons/test.jpg);\n"
"	color:#000;\n"
"	padding:2px;\n"
"\n"
"}")
        self.title_12.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.title_12.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_21.addWidget(self.title_12)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_17)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.time_11 = QLabel(self.frame_33)
        self.time_11.setObjectName(u"time_11")
        self.time_11.setMinimumSize(QSize(31, 14))
        self.time_11.setMaximumSize(QSize(31, 14))
        self.time_11.setFont(font5)
        self.time_11.setStyleSheet(u"QLabel{\n"
"color:#ddd;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.time_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.time_11)

        self.ticks_7 = QLabel(self.frame_33)
        self.ticks_7.setObjectName(u"ticks_7")
        self.ticks_7.setMinimumSize(QSize(24, 14))
        self.ticks_7.setMaximumSize(QSize(24, 14))
        self.ticks_7.setFont(font8)
        self.ticks_7.setStyleSheet(u"\n"
"image: url(:/cils/cils/cil-check-circle-green.png);\n"
"background-color:rgba(255, 255, 255, 1);\n"
"border-radius:7px;\n"
"padding:1px;")
        self.ticks_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.ticks_7)


        self.horizontalLayout_27.addLayout(self.horizontalLayout_29)


        self.verticalLayout_21.addLayout(self.horizontalLayout_27)

        self.image_bubble_frame = QFrame(self.widgets_page)
        self.image_bubble_frame.setObjectName(u"image_bubble_frame")
        self.image_bubble_frame.setGeometry(QRect(30, 350, 221, 241))
        self.image_bubble_frame.setMinimumSize(QSize(201, 101))
        self.image_bubble_frame.setStyleSheet(u"")
        self.image_bubble_frame.setFrameShape(QFrame.StyledPanel)
        self.image_bubble_frame.setFrameShadow(QFrame.Raised)
        self.frame_37 = QFrame(self.image_bubble_frame)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(5, 4, 8, 8))
        self.frame_37.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"border-radius:4px;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.frame_38 = QFrame(self.image_bubble_frame)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setGeometry(QRect(10, 10, 14, 14))
        self.frame_38.setStyleSheet(u"background-color: rgba(255, 170, 0, .7);\n"
"border-radius:7px;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.image_bubble = QFrame(self.image_bubble_frame)
        self.image_bubble.setObjectName(u"image_bubble")
        self.image_bubble.setGeometry(QRect(17, 17, 191, 201))
        self.image_bubble.setStyleSheet(u"	border-radius:10px;\n"
"	border-top-left-radius:8px;\n"
"	background-color: rgb(255, 170, 0);\n"
"")
        self.image_bubble.setFrameShape(QFrame.StyledPanel)
        self.image_bubble.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.image_bubble)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(2, 1, 2, 0)
        self.image = QLabel(self.image_bubble)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(180, 180))
        self.image.setMaximumSize(QSize(16777215, 180))
        self.image.setFont(font10)
        self.image.setStyleSheet(u"QLabel{\n"
"	border-radius:10px;\n"
"	border-image: url(:/icons/icons/test.jpg);\n"
"	color:#000;\n"
"	padding:2px;\n"
"\n"
"}")
        self.image.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.image.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_23.addWidget(self.image)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_19)

        self.time_13 = QLabel(self.image_bubble)
        self.time_13.setObjectName(u"time_13")
        self.time_13.setMinimumSize(QSize(31, 14))
        self.time_13.setMaximumSize(QSize(31, 14))
        self.time_13.setFont(font5)
        self.time_13.setStyleSheet(u"QLabel{\n"
"color:#ddd;\n"
"border-radius:7px;\n"
"}")
        self.time_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.time_13)


        self.verticalLayout_23.addLayout(self.horizontalLayout_32)

        self.label_2 = QLabel(self.widgets_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 10, 120, 20))
        self.label_2.setMaximumSize(QSize(120, 20))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color:black;\n"
"padding:4px;\n"
"border-radius:4px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.chat_stacked_widget.addWidget(self.widgets_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_layout = QVBoxLayout(self.home_page)
        self.home_layout.setSpacing(0)
        self.home_layout.setObjectName(u"home_layout")
        self.home_layout.setContentsMargins(90, -1, 90, -1)
        self.verticalSpacer_5 = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.home_layout.addItem(self.verticalSpacer_5)

        self.home_logo = QLabel(self.home_page)
        self.home_logo.setObjectName(u"home_logo")
        self.home_logo.setMinimumSize(QSize(201, 181))
        self.home_logo.setStyleSheet(u"image: url(:/icons/icons/ARsoftlogo.png);\n"
"")
        self.home_logo.setAlignment(Qt.AlignCenter)

        self.home_layout.addWidget(self.home_logo)

        self.home_app_name = QLabel(self.home_page)
        self.home_app_name.setObjectName(u"home_app_name")
        self.home_app_name.setMinimumSize(QSize(261, 51))
        font11 = QFont()
        font11.setPointSize(18)
        self.home_app_name.setFont(font11)
        self.home_app_name.setAlignment(Qt.AlignCenter)

        self.home_layout.addWidget(self.home_app_name)

        self.home_app_description = QLabel(self.home_page)
        self.home_app_description.setObjectName(u"home_app_description")
        self.home_app_description.setMinimumSize(QSize(451, 91))
        self.home_app_description.setFont(font1)
        self.home_app_description.setLayoutDirection(Qt.LeftToRight)
        self.home_app_description.setAlignment(Qt.AlignCenter)
        self.home_app_description.setWordWrap(True)

        self.home_layout.addWidget(self.home_app_description)

        self.verticalSpacer_6 = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.home_layout.addItem(self.verticalSpacer_6)

        self.chat_stacked_widget.addWidget(self.home_page)
        self.chat_page = QWidget()
        self.chat_page.setObjectName(u"chat_page")
        self.chat_page.setStyleSheet(u"")
        self.chat_page_layout = QVBoxLayout(self.chat_page)
        self.chat_page_layout.setSpacing(6)
        self.chat_page_layout.setObjectName(u"chat_page_layout")
        self.chat_page_layout.setContentsMargins(9, 9, 9, 0)
        self.active_chat_header = QWidget(self.chat_page)
        self.active_chat_header.setObjectName(u"active_chat_header")
        self.active_chat_header.setMinimumSize(QSize(551, 61))
        self.active_chat_header.setMaximumSize(QSize(16777215, 61))
        self.active_chat_header.setStyleSheet(u"")
        self.active_chat_header_layout = QHBoxLayout(self.active_chat_header)
        self.active_chat_header_layout.setObjectName(u"active_chat_header_layout")
        self.active_chat_header_layout.setContentsMargins(9, 6, 9, 6)
        self.active_client_picture = QLabel(self.active_chat_header)
        self.active_client_picture.setObjectName(u"active_client_picture")
        self.active_client_picture.setMinimumSize(QSize(50, 50))
        self.active_client_picture.setMaximumSize(QSize(50, 50))
        font12 = QFont()
        font12.setPointSize(26)
        font12.setBold(True)
        self.active_client_picture.setFont(font12)
        self.active_client_picture.setStyleSheet(u"")
        self.active_client_picture.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.active_chat_header_layout.addWidget(self.active_client_picture)

        self.client_info_layout = QVBoxLayout()
        self.client_info_layout.setSpacing(0)
        self.client_info_layout.setObjectName(u"client_info_layout")
        self.active_client_name = QLabel(self.active_chat_header)
        self.active_client_name.setObjectName(u"active_client_name")
        self.active_client_name.setMinimumSize(QSize(251, 31))
        self.active_client_name.setMaximumSize(QSize(16777215, 31))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(12)
        font13.setBold(True)
        font13.setItalic(False)
        self.active_client_name.setFont(font13)

        self.client_info_layout.addWidget(self.active_client_name)

        self.active_client_status = QLabel(self.active_chat_header)
        self.active_client_status.setObjectName(u"active_client_status")
        self.active_client_status.setMinimumSize(QSize(251, 20))
        self.active_client_status.setMaximumSize(QSize(16777215, 20))
        self.active_client_status.setFont(font2)
        self.active_client_status.setStyleSheet(u"")

        self.client_info_layout.addWidget(self.active_client_status)


        self.active_chat_header_layout.addLayout(self.client_info_layout)

        self.last_seen = QLabel(self.active_chat_header)
        self.last_seen.setObjectName(u"last_seen")
        self.last_seen.setMinimumSize(QSize(131, 20))
        self.last_seen.setMaximumSize(QSize(16777215, 20))
        self.last_seen.setStyleSheet(u"")
        self.last_seen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.active_chat_header_layout.addWidget(self.last_seen)

        self.attachment_btn = QPushButton(self.active_chat_header)
        self.attachment_btn.setObjectName(u"attachment_btn")
        self.attachment_btn.setMinimumSize(QSize(36, 36))
        self.attachment_btn.setMaximumSize(QSize(36, 36))
        self.attachment_btn.setStyleSheet(u"#attachment_btn {	\n"
"	background-image: url(:/svg/svg//icon_attachment.svg);\n"
"}\n"
"")

        self.active_chat_header_layout.addWidget(self.attachment_btn)

        self.delete_btn = QPushButton(self.active_chat_header)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(36, 36))
        self.delete_btn.setMaximumSize(QSize(36, 36))
        self.delete_btn.setStyleSheet(u"background-image: url(:/cils/cils/cil-trash.png);\n"
"")

        self.active_chat_header_layout.addWidget(self.delete_btn)


        self.chat_page_layout.addWidget(self.active_chat_header)

        self.chat_scroll = QScrollArea(self.chat_page)
        self.chat_scroll.setObjectName(u"chat_scroll")
        self.chat_scroll.setMinimumSize(QSize(551, 50))
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll_widget = QWidget()
        self.chat_scroll_widget.setObjectName(u"chat_scroll_widget")
        self.chat_scroll_widget.setGeometry(QRect(0, 0, 567, 187))
        self.chat_scroll_layout = QVBoxLayout(self.chat_scroll_widget)
        self.chat_scroll_layout.setSpacing(9)
        self.chat_scroll_layout.setObjectName(u"chat_scroll_layout")
        self.chat_scroll_layout.setContentsMargins(6, 12, 6, 12)
        self.date_label = QLabel(self.chat_scroll_widget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setMinimumSize(QSize(551, 40))
        self.date_label.setStyleSheet(u"background-color: rgb(31, 32, 33);\n"
"color:#aa77ff;\n"
"padding:8px;\n"
"border-radius:8px;")
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setWordWrap(True)

        self.chat_scroll_layout.addWidget(self.date_label, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.chat_scroll_layout.addItem(self.verticalSpacer_2)

        self.chat_scroll.setWidget(self.chat_scroll_widget)

        self.chat_page_layout.addWidget(self.chat_scroll)

        self.emoji_widget = QWidget(self.chat_page)
        self.emoji_widget.setObjectName(u"emoji_widget")
        self.emoji_widget.setMinimumSize(QSize(0, 100))
        self.emoji_widget.setMaximumSize(QSize(16777215, 196))
        self.emoji_widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.emoji_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.emoji_tab_widget = QTabWidget(self.emoji_widget)
        self.emoji_tab_widget.setObjectName(u"emoji_tab_widget")
        self.emoji_tab_widget.setStyleSheet(u"")
        self.emoji_tab_widget.setTabPosition(QTabWidget.North)
        self.emoji_tab_widget.setTabShape(QTabWidget.Rounded)
        self.emoji_tab_widget.setTabsClosable(False)
        self.tab_smileys = QWidget()
        self.tab_smileys.setObjectName(u"tab_smileys")
        self.verticalLayout_12 = QVBoxLayout(self.tab_smileys)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.tab_smileys)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 541, 142))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(35, 35))

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.emoji_tab_widget.addTab(self.tab_smileys, "")
        self.tab_animals = QWidget()
        self.tab_animals.setObjectName(u"tab_animals")
        self.verticalLayout_6 = QVBoxLayout(self.tab_animals)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.tab_animals)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 541, 142))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_15.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)

        self.emoji_tab_widget.addTab(self.tab_animals, "")
        self.tab_foods = QWidget()
        self.tab_foods.setObjectName(u"tab_foods")
        self.verticalLayout_7 = QVBoxLayout(self.tab_foods)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.tab_foods)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 541, 142))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(3)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_14.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_7.addWidget(self.scrollArea_3)

        self.emoji_tab_widget.addTab(self.tab_foods, "")
        self.tab_travels = QWidget()
        self.tab_travels.setObjectName(u"tab_travels")
        self.verticalLayout_10 = QVBoxLayout(self.tab_travels)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.tab_travels)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 541, 142))
        self.gridLayout_13 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_13.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_10.addWidget(self.scrollArea_4)

        self.emoji_tab_widget.addTab(self.tab_travels, "")
        self.tab_activities = QWidget()
        self.tab_activities.setObjectName(u"tab_activities")
        self.verticalLayout_11 = QVBoxLayout(self.tab_activities)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.tab_activities)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 541, 142))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_12.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_11.addWidget(self.scrollArea_6)

        self.emoji_tab_widget.addTab(self.tab_activities, "")
        self.tab_objects = QWidget()
        self.tab_objects.setObjectName(u"tab_objects")
        self.verticalLayout_24 = QVBoxLayout(self.tab_objects)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.tab_objects)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 541, 142))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_11.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_24.addWidget(self.scrollArea_7)

        self.emoji_tab_widget.addTab(self.tab_objects, "")
        self.tab_symbols = QWidget()
        self.tab_symbols.setObjectName(u"tab_symbols")
        self.verticalLayout_20 = QVBoxLayout(self.tab_symbols)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_8 = QScrollArea(self.tab_symbols)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 541, 142))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents_8)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_10.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_20.addWidget(self.scrollArea_8)

        self.emoji_tab_widget.addTab(self.tab_symbols, "")
        self.tab_flags = QWidget()
        self.tab_flags.setObjectName(u"tab_flags")
        self.verticalLayout_13 = QVBoxLayout(self.tab_flags)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_9 = QScrollArea(self.tab_flags)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 541, 142))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_3.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_13.addWidget(self.scrollArea_9)

        self.emoji_tab_widget.addTab(self.tab_flags, "")

        self.horizontalLayout_3.addWidget(self.emoji_tab_widget)

        self.close_emoji_btn = QPushButton(self.emoji_widget)
        self.close_emoji_btn.setObjectName(u"close_emoji_btn")
        self.close_emoji_btn.setMaximumSize(QSize(20, 20))
        self.close_emoji_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color:#111;\n"
"border:none;\n"
"border-radius:10px;\n"
"image: url(:/cils/cils/cil-x.png);\n"
"padding:4px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"}")

        self.horizontalLayout_3.addWidget(self.close_emoji_btn, 0, Qt.AlignTop)


        self.chat_page_layout.addWidget(self.emoji_widget)

        self.media_bg = QWidget(self.chat_page)
        self.media_bg.setObjectName(u"media_bg")
        self.media_bg.setMaximumSize(QSize(46, 190))
        self.media_bg.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.media_bg)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 0, 3, 0)
        self.media_doc = QPushButton(self.media_bg)
        self.media_doc.setObjectName(u"media_doc")
        self.media_doc.setMinimumSize(QSize(40, 40))
        self.media_doc.setMaximumSize(QSize(40, 40))
        self.media_doc.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/cils/cils/cil-paperclip.png);\n"
"	background-color: rgb(0, 0, 127);}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 62, 63);}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(31, 32, 34);}")

        self.verticalLayout.addWidget(self.media_doc)

        self.media_audio = QPushButton(self.media_bg)
        self.media_audio.setObjectName(u"media_audio")
        self.media_audio.setMinimumSize(QSize(40, 40))
        self.media_audio.setMaximumSize(QSize(40, 40))
        self.media_audio.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/cils/cils/blacks/cil-music-note.png);\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(201, 202, 203);}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(101, 102, 103);}")

        self.verticalLayout.addWidget(self.media_audio)

        self.media_image = QPushButton(self.media_bg)
        self.media_image.setObjectName(u"media_image")
        self.media_image.setMinimumSize(QSize(40, 40))
        self.media_image.setMaximumSize(QSize(40, 40))
        self.media_image.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/cils/cils/cil-image1.png);\n"
"	background-color: rgb(156, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 62, 63);}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(31, 32, 34);}")

        self.verticalLayout.addWidget(self.media_image)

        self.media_video = QPushButton(self.media_bg)
        self.media_video.setObjectName(u"media_video")
        self.media_video.setMinimumSize(QSize(40, 40))
        self.media_video.setMaximumSize(QSize(40, 40))
        self.media_video.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/cils/cils/blacks/cil-movie.png);\n"
"	background-color: rgb(0, 105, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(201, 202, 203);}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(101, 102, 103);}")

        self.verticalLayout.addWidget(self.media_video)


        self.chat_page_layout.addWidget(self.media_bg)

        self.footer = QWidget(self.chat_page)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(551, 61))
        self.footer.setMaximumSize(QSize(16777215, 61))
        self.footer.setStyleSheet(u"QWidget.QPushButton{\n"
"border-radius:20px;}")
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.media_btn = QPushButton(self.footer)
        self.media_btn.setObjectName(u"media_btn")
        self.media_btn.setMinimumSize(QSize(40, 40))
        self.media_btn.setMaximumSize(QSize(40, 40))
        self.media_btn.setStyleSheet(u"background-image: url(:/cils/cils/cil-plus.png);")

        self.horizontalLayout_2.addWidget(self.media_btn)

        self.input_container = QWidget(self.footer)
        self.input_container.setObjectName(u"input_container")
        self.input_container.setMinimumSize(QSize(431, 51))
        self.input_container.setMaximumSize(QSize(16777215, 51))
        self.input_container.setStyleSheet(u"")
        self.input_container_layout = QHBoxLayout(self.input_container)
        self.input_container_layout.setSpacing(0)
        self.input_container_layout.setObjectName(u"input_container_layout")
        self.input_container_layout.setContentsMargins(9, 3, 16, 3)
        self.emoji_btn = QPushButton(self.input_container)
        self.emoji_btn.setObjectName(u"emoji_btn")
        self.emoji_btn.setMinimumSize(QSize(40, 40))
        self.emoji_btn.setMaximumSize(QSize(40, 40))
        self.emoji_btn.setStyleSheet(u"background-image: url(:/cils/cils/cil-mood-good.png);")

        self.input_container_layout.addWidget(self.emoji_btn)

        self.input = QTextEdit(self.input_container)
        self.input.setObjectName(u"input")
        self.input.setMaximumSize(QSize(16777215, 30))
        self.input.setFont(font4)
        self.input.setStyleSheet(u"")
        self.input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.input.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.input.setCursorWidth(1)

        self.input_container_layout.addWidget(self.input)


        self.horizontalLayout_2.addWidget(self.input_container)

        self.record_widget = QFrame(self.footer)
        self.record_widget.setObjectName(u"record_widget")
        self.record_widget.setMinimumSize(QSize(151, 31))
        self.record_widget.setMaximumSize(QSize(151, 51))
        self.record_widget.setStyleSheet(u"")
        self.record_widget.setFrameShape(QFrame.StyledPanel)
        self.record_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.record_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.end = QPushButton(self.record_widget)
        self.end.setObjectName(u"end")
        self.end.setMaximumSize(QSize(31, 20))
        self.end.setStyleSheet(u"QPushButton{\n"
"	image: url(:/cils/cils/cil-media-record-bl.png);\n"
"	background:#009900;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}")

        self.horizontalLayout.addWidget(self.end)

        self.time = QLabel(self.record_widget)
        self.time.setObjectName(u"time")
        self.time.setMaximumSize(QSize(71, 20))
        self.time.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"	border-radius:none;\n"
"}")
        self.time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.time)

        self.cancel = QPushButton(self.record_widget)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMaximumSize(QSize(31, 20))
        self.cancel.setStyleSheet(u"QPushButton{\n"
"	image: url(:/cils/cils/cil-media-stop-bl.png);\n"
"	background:#FF0000;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}")

        self.horizontalLayout.addWidget(self.cancel)


        self.horizontalLayout_2.addWidget(self.record_widget)

        self.send_btn = QPushButton(self.footer)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setMinimumSize(QSize(40, 40))
        self.send_btn.setMaximumSize(QSize(40, 40))
        self.send_btn.setStyleSheet(u"background-image: url(:/cils/cils/cil-microphone.png);")

        self.horizontalLayout_2.addWidget(self.send_btn)

        self.media_btn.raise_()
        self.send_btn.raise_()
        self.input_container.raise_()
        self.record_widget.raise_()

        self.chat_page_layout.addWidget(self.footer)

        self.chat_stacked_widget.addWidget(self.chat_page)

        self.horizontalLayout_7.addWidget(self.chat_stacked_widget)

        self.right_stacked_widget = QStackedWidget(self.right_side_container)
        self.right_stacked_widget.setObjectName(u"right_stacked_widget")
        self.right_stacked_widget.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_25 = QVBoxLayout(self.page_1)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 6, 9, 6)
        self.settings_title = QLabel(self.page_1)
        self.settings_title.setObjectName(u"settings_title")
        self.settings_title.setMaximumSize(QSize(16777215, 21))
        self.settings_title.setFont(font)

        self.verticalLayout_25.addWidget(self.settings_title)

        self.breadcrumb = QLabel(self.page_1)
        self.breadcrumb.setObjectName(u"breadcrumb")
        self.breadcrumb.setMaximumSize(QSize(16777215, 21))
        self.breadcrumb.setFont(font5)
        self.breadcrumb.setStyleSheet(u"padding-bottom:4px;\n"
"color:gray;\n"
"border-bottom:3px solid red;\n"
"")

        self.verticalLayout_25.addWidget(self.breadcrumb)

        self.settings_stacked_widget = QStackedWidget(self.page_1)
        self.settings_stacked_widget.setObjectName(u"settings_stacked_widget")
        self.settings_stacked_widget.setStyleSheet(u"")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.checkBox = QCheckBox(self.page_7)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 39, 201, 31))
        self.label_5 = QLabel(self.page_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 90, 171, 16))
        self.settings_stacked_widget.addWidget(self.page_7)
        self.account_settings = QWidget()
        self.account_settings.setObjectName(u"account_settings")
        self.verticalLayout_22 = QVBoxLayout(self.account_settings)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.profile_picture_frame = QFrame(self.account_settings)
        self.profile_picture_frame.setObjectName(u"profile_picture_frame")
        self.profile_picture_frame.setMinimumSize(QSize(221, 91))
        self.profile_picture_frame.setMaximumSize(QSize(229, 91))
        self.profile_picture_frame.setStyleSheet(u"background-color:#000;\n"
"border-radius:8px;")
        self.profile_picture_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_picture_frame.setFrameShadow(QFrame.Raised)
        self.edit_profile_picture_btn = QPushButton(self.profile_picture_frame)
        self.edit_profile_picture_btn.setObjectName(u"edit_profile_picture_btn")
        self.edit_profile_picture_btn.setGeometry(QRect(129, 54, 30, 30))
        self.edit_profile_picture_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"image: url(:/cils/cils/cil-camera.png);\n"
"padding:7px;\n"
"background-color:rgb(30,32,33);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color:rgb(40,42,43);\n"
"}\n"
"\n"
"")
        self.user_profile_picture = QLabel(self.profile_picture_frame)
        self.user_profile_picture.setObjectName(u"user_profile_picture")
        self.user_profile_picture.setGeometry(QRect(67, 4, 81, 81))
        self.user_profile_picture.setStyleSheet(u"border-radius:40px;\n"
"border-image: url(:/icons/icons/avatar.png);")
        self.user_profile_picture.setScaledContents(True)
        self.user_profile_picture.raise_()
        self.edit_profile_picture_btn.raise_()

        self.verticalLayout_22.addWidget(self.profile_picture_frame)

        self.profile_form_layout = QVBoxLayout()
        self.profile_form_layout.setSpacing(4)
        self.profile_form_layout.setObjectName(u"profile_form_layout")
        self.set_profile_label = QLabel(self.account_settings)
        self.set_profile_label.setObjectName(u"set_profile_label")
        self.set_profile_label.setMaximumSize(QSize(16777215, 26))
        self.set_profile_label.setFont(font)
        self.set_profile_label.setStyleSheet(u"")

        self.profile_form_layout.addWidget(self.set_profile_label)

        self.name_layout = QGridLayout()
        self.name_layout.setObjectName(u"name_layout")
        self.name_layout.setVerticalSpacing(0)
        self.label_19 = QLabel(self.account_settings)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 20))
        self.label_19.setMaximumSize(QSize(16777215, 20))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color:gray;")

        self.name_layout.addWidget(self.label_19, 0, 0, 1, 1)

        self.username = QLabel(self.account_settings)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setStyleSheet(u"border-radius:4px;\n"
"background-color:rgb(30,32,33);\n"
"padding:4px;")
        self.username.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.name_layout.addWidget(self.username, 2, 0, 1, 1)

        self.username_btn = QPushButton(self.account_settings)
        self.username_btn.setObjectName(u"username_btn")
        self.username_btn.setMinimumSize(QSize(30, 30))
        self.username_btn.setMaximumSize(QSize(30, 30))
        self.username_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:4px;\n"
"	border:1px solid rgb(30,32,33);\n"
"	image: url(:/cils/cils/cil-pencil.png);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(30,32,33);\n"
"}")

        self.name_layout.addWidget(self.username_btn, 2, 1, 1, 1)


        self.profile_form_layout.addLayout(self.name_layout)

        self.email_layout = QGridLayout()
        self.email_layout.setObjectName(u"email_layout")
        self.email_layout.setVerticalSpacing(0)
        self.label_20 = QLabel(self.account_settings)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 20))
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color:gray;")

        self.email_layout.addWidget(self.label_20, 0, 0, 1, 1)

        self.user_email = QLabel(self.account_settings)
        self.user_email.setObjectName(u"user_email")
        self.user_email.setMinimumSize(QSize(0, 30))
        self.user_email.setStyleSheet(u"border-radius:4px;\n"
"background-color:rgb(30,32,33);\n"
"padding:4px;")
        self.user_email.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.email_layout.addWidget(self.user_email, 1, 0, 1, 1)

        self.user_eail_btn = QPushButton(self.account_settings)
        self.user_eail_btn.setObjectName(u"user_eail_btn")
        self.user_eail_btn.setMinimumSize(QSize(30, 30))
        self.user_eail_btn.setMaximumSize(QSize(30, 30))
        self.user_eail_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:4px;\n"
"	border:1px solid rgb(30,32,33);\n"
"	image: url(:/cils/cils/cil-pencil.png);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(30,32,33);\n"
"}")

        self.email_layout.addWidget(self.user_eail_btn, 1, 1, 1, 1)


        self.profile_form_layout.addLayout(self.email_layout)

        self.status_layout = QGridLayout()
        self.status_layout.setObjectName(u"status_layout")
        self.status_layout.setVerticalSpacing(0)
        self.label_21 = QLabel(self.account_settings)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 20))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"color:gray;")

        self.status_layout.addWidget(self.label_21, 0, 0, 1, 1)

        self.user_status = QLabel(self.account_settings)
        self.user_status.setObjectName(u"user_status")
        self.user_status.setMinimumSize(QSize(0, 30))
        self.user_status.setStyleSheet(u"border-radius:4px;\n"
"background-color:rgb(30,32,33);\n"
"padding:4px;")
        self.user_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_status.setWordWrap(True)
        self.user_status.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.status_layout.addWidget(self.user_status, 1, 0, 1, 1)

        self.user_status_btn = QPushButton(self.account_settings)
        self.user_status_btn.setObjectName(u"user_status_btn")
        self.user_status_btn.setMinimumSize(QSize(30, 30))
        self.user_status_btn.setMaximumSize(QSize(30, 30))
        self.user_status_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:4px;\n"
"	border:1px solid rgb(30,32,33);\n"
"	image: url(:/cils/cils/cil-pencil.png);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(30,32,33);\n"
"}")

        self.status_layout.addWidget(self.user_status_btn, 1, 1, 1, 1)


        self.profile_form_layout.addLayout(self.status_layout)

        self.role_layout = QGridLayout()
        self.role_layout.setObjectName(u"role_layout")
        self.role_layout.setVerticalSpacing(0)
        self.label_28 = QLabel(self.account_settings)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 20))
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"color:gray;")

        self.role_layout.addWidget(self.label_28, 0, 0, 1, 1)

        self.user_role = QLabel(self.account_settings)
        self.user_role.setObjectName(u"user_role")
        self.user_role.setMinimumSize(QSize(0, 30))
        self.user_role.setStyleSheet(u"border-radius:4px;\n"
"background-color:rgb(30,32,33);\n"
"padding:4px;")
        self.user_role.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_role.setWordWrap(True)
        self.user_role.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.role_layout.addWidget(self.user_role, 1, 0, 1, 1)

        self.user_role_btn = QPushButton(self.account_settings)
        self.user_role_btn.setObjectName(u"user_role_btn")
        self.user_role_btn.setMinimumSize(QSize(30, 30))
        self.user_role_btn.setMaximumSize(QSize(30, 30))
        self.user_role_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:4px;\n"
"	border:1px solid rgb(30,32,33);\n"
"	image: url(:/cils/cils/cil-pencil.png);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(30,32,33);\n"
"}")

        self.role_layout.addWidget(self.user_role_btn, 1, 1, 1, 1)


        self.profile_form_layout.addLayout(self.role_layout)

        self.department_layout = QGridLayout()
        self.department_layout.setObjectName(u"department_layout")
        self.department_layout.setVerticalSpacing(0)
        self.label_29 = QLabel(self.account_settings)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 20))
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"color:gray;")

        self.department_layout.addWidget(self.label_29, 0, 0, 1, 1)

        self.user_department = QLabel(self.account_settings)
        self.user_department.setObjectName(u"user_department")
        self.user_department.setMinimumSize(QSize(0, 30))
        self.user_department.setStyleSheet(u"border-radius:4px;\n"
"background-color:rgb(30,32,33);\n"
"padding:4px;")
        self.user_department.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_department.setWordWrap(True)
        self.user_department.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.department_layout.addWidget(self.user_department, 1, 0, 1, 1)

        self.user_department_btn = QPushButton(self.account_settings)
        self.user_department_btn.setObjectName(u"user_department_btn")
        self.user_department_btn.setMinimumSize(QSize(30, 30))
        self.user_department_btn.setMaximumSize(QSize(30, 30))
        self.user_department_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:4px;\n"
"	border:1px solid rgb(30,32,33);\n"
"	image: url(:/cils/cils/cil-pencil.png);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(30,32,33);\n"
"}")

        self.department_layout.addWidget(self.user_department_btn, 1, 1, 1, 1)


        self.profile_form_layout.addLayout(self.department_layout)


        self.verticalLayout_22.addLayout(self.profile_form_layout)

        self.password_form_layout = QVBoxLayout()
        self.password_form_layout.setSpacing(4)
        self.password_form_layout.setObjectName(u"password_form_layout")
        self.set_password_title = QLabel(self.account_settings)
        self.set_password_title.setObjectName(u"set_password_title")
        self.set_password_title.setMaximumSize(QSize(16777215, 26))
        self.set_password_title.setFont(font)
        self.set_password_title.setStyleSheet(u"")

        self.password_form_layout.addWidget(self.set_password_title)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_23 = QLabel(self.account_settings)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 20))
        self.label_23.setMaximumSize(QSize(16777215, 20))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color:gray;")

        self.verticalLayout_14.addWidget(self.label_23)

        self.active_password = QLineEdit(self.account_settings)
        self.active_password.setObjectName(u"active_password")
        self.active_password.setMinimumSize(QSize(0, 30))
        self.active_password.setStyleSheet(u"QLineEdit{\n"
"	border-radius:4px;\n"
"	border: 2px solid rgb(30,32,33);\n"
"	padding:4px;\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus{\n"
"	border: 2px solid rgb(40,42,43);\n"
"}")

        self.verticalLayout_14.addWidget(self.active_password)


        self.password_form_layout.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_24 = QLabel(self.account_settings)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 20))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"color:gray;")

        self.verticalLayout_15.addWidget(self.label_24)

        self.new_password = QLineEdit(self.account_settings)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setMinimumSize(QSize(0, 30))
        self.new_password.setStyleSheet(u"QLineEdit{\n"
"	border-radius:4px;\n"
"	border: 2px solid rgb(30,32,33);\n"
"	padding:4px;\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus{\n"
"	border: 2px solid rgb(40,42,43);\n"
"}")

        self.verticalLayout_15.addWidget(self.new_password)


        self.password_form_layout.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_25 = QLabel(self.account_settings)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 20))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"color:gray;")

        self.verticalLayout_16.addWidget(self.label_25)

        self.confirm_password = QLineEdit(self.account_settings)
        self.confirm_password.setObjectName(u"confirm_password")
        self.confirm_password.setMinimumSize(QSize(0, 30))
        self.confirm_password.setMaximumSize(QSize(16777215, 30))
        self.confirm_password.setStyleSheet(u"QLineEdit{\n"
"	border-radius:4px;\n"
"	border: 2px solid rgb(30,32,33);\n"
"	padding:4px;\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus{\n"
"	border: 2px solid rgb(40,42,43);\n"
"}")

        self.verticalLayout_16.addWidget(self.confirm_password)


        self.password_form_layout.addLayout(self.verticalLayout_16)

        self.error_label = QLabel(self.account_settings)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setMaximumSize(QSize(16777215, 16))
        self.error_label.setFont(font5)
        self.error_label.setStyleSheet(u"color:red;\n"
"padding-left:4px;")

        self.password_form_layout.addWidget(self.error_label)

        self.save_password_btn = QPushButton(self.account_settings)
        self.save_password_btn.setObjectName(u"save_password_btn")
        self.save_password_btn.setMinimumSize(QSize(0, 30))
        self.save_password_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius:4px;\n"
"	background-color: rgb(30,32,33);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(40,42,43);\n"
"}")

        self.password_form_layout.addWidget(self.save_password_btn)


        self.verticalLayout_22.addLayout(self.password_form_layout)

        self.settings_stacked_widget.addWidget(self.account_settings)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.settings_stacked_widget.addWidget(self.page_3)

        self.verticalLayout_25.addWidget(self.settings_stacked_widget)

        self.right_stacked_widget.addWidget(self.page_1)
        self.settings_title.raise_()
        self.settings_stacked_widget.raise_()
        self.breadcrumb.raise_()
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.right_stacked_widget.addWidget(self.page_6)

        self.horizontalLayout_7.addWidget(self.right_stacked_widget)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.status_bar = QLabel(self.right_side_container)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setMinimumSize(QSize(0, 20))
        self.status_bar.setMaximumSize(QSize(16777215, 20))
        self.status_bar.setStyleSheet(u"background:transparent;\n"
"color:rgb(75, 77, 79);\n"
"padding-right:16px;\n"
"border-right:4px solid transparent;\n"
"background-image: url(:/cils/cils/cil-size-grip.png);\n"
"background-repeat:no-repeat;\n"
"background-position:right;")
        self.status_bar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.status_bar)


        self.app_margins.addWidget(self.right_side_container)


        self.main_window_layout.addWidget(self.app_bg)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.left_side_container.setCurrentIndex(0)
        self.contacts_stack.setCurrentIndex(1)
        self.chat_stacked_widget.setCurrentIndex(2)
        self.emoji_tab_widget.setCurrentIndex(0)
        self.right_stacked_widget.setCurrentIndex(0)
        self.settings_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AR Intercom", None))
        self.actionAide.setText(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"AR Intercom", None))
        self.app_logo.setText("")
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Hide menu", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.scan_btn.setText(QCoreApplication.translate("MainWindow", u"Scan network", None))
        self.chat_btn.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.me_online_toast.setText("")
        self.me_status.setText(QCoreApplication.translate("MainWindow", u"Coding...", None))
        self.me_username.setText(QCoreApplication.translate("MainWindow", u"Antares", None))
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search chat, message, ...", None))
        self.msg_countrer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">1</span></p></body></html>", None))
        self.client_picture.setText("")
        self.online_toast.setText("")
        self.last_message.setText(QCoreApplication.translate("MainWindow", u"Last message strip...", None))
        self.client_name.setText(QCoreApplication.translate("MainWindow", u"Charlie", None))
        self.messege_number.setText(QCoreApplication.translate("MainWindow", u"1268", None))
        self.last_seen_0.setText(QCoreApplication.translate("MainWindow", u"online", None))
        self.client_picture_3.setText("")
        self.online_toast_3.setText("")
        self.last_message_3.setText(QCoreApplication.translate("MainWindow", u"Seems like a see a...", None))
        self.client_name_3.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.messege_number_5.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.last_seen_2.setText(QCoreApplication.translate("MainWindow", u"27 min ago", None))
        self.device_icon.setText("")
        self.host_name.setText(QCoreApplication.translate("MainWindow", u"DESKTOP-ID", None))
        self.host_address.setText(QCoreApplication.translate("MainWindow", u"192.168.1.100", None))
        self.add_to_contact_btn.setText("")
        self.start_scan_btn.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
        self.signal_text.setText(QCoreApplication.translate("MainWindow", u"You're connected !", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; color:#4b4b4d;\">AR Intercom<br/>From a Creative Mind !</span></p><p align=\"center\"><span style=\" font-size:8pt; color:#4b4b4d;\">www.artrevolutionlabel.com</span></p></body></html>", None))
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>AR Intercom <span style=\" font-weight:400; color:#878787;\">Enterprise</span></p></body></html>", None))
        self.settings_btn.setText("")
#if QT_CONFIG(statustip)
        self.minimize_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(statustip)
        self.minimize_btn.setText("")
#if QT_CONFIG(statustip)
        self.maximize_restore_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(statustip)
        self.maximize_restore_btn.setText("")
#if QT_CONFIG(statustip)
        self.close_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(statustip)
        self.close_btn.setText("")
        self.left_bubble_3.setText(QCoreApplication.translate("MainWindow", u"Bonjour !", None))
        self.time_3.setText(QCoreApplication.translate("MainWindow", u"23:35", None))
        self.ticks_3.setText("")
        self.left_bubble_4.setText(QCoreApplication.translate("MainWindow", u"Hello !", None))
        self.time_6.setText(QCoreApplication.translate("MainWindow", u"23:33", None))
        self.time_7.setText(QCoreApplication.translate("MainWindow", u"23:36", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"ARV-20062021-1200.arv", None))
        self.elapsed_time_3.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.total_time_3.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.time_8.setText(QCoreApplication.translate("MainWindow", u"23:38", None))
        self.ticks_5.setText("")
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"ARV-20062021-1200.arv", None))
        self.elapsed_time_4.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.total_time_4.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.document_icon.setText(QCoreApplication.translate("MainWindow", u"EXT", None))
        self.document_title.setText(QCoreApplication.translate("MainWindow", u"Document.ext", None))
        self.document_size.setText(QCoreApplication.translate("MainWindow", u"2Mb", None))
        self.time_9.setText(QCoreApplication.translate("MainWindow", u"23:36", None))
        self.title_8.setText(QCoreApplication.translate("MainWindow", u"EXT", None))
        self.title_9.setText(QCoreApplication.translate("MainWindow", u"Document.ext", None))
        self.title_10.setText(QCoreApplication.translate("MainWindow", u"2Mb", None))
        self.time_10.setText(QCoreApplication.translate("MainWindow", u"23:38", None))
        self.ticks_6.setText("")
        self.title_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#848484;\">1.2Mb</span> \u2022 Image.ext</p></body></html>", None))
        self.time_11.setText(QCoreApplication.translate("MainWindow", u"23:38", None))
        self.ticks_7.setText("")
        self.image.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#848484;\">1.2Mb</span> \u2022 Image.ext</p></body></html>", None))
        self.time_13.setText(QCoreApplication.translate("MainWindow", u"23:36", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"23 SEPTEMBRE 2023", None))
        self.home_logo.setText("")
        self.home_app_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Art Revolution <span style=\" font-weight:700;\">Intercom</span></p></body></html>", None))
        self.home_app_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#878787;\">Facilitate business communication - the key of seamless and instant professional exchanges, unlocking the collaborative potential of your team !</span></p><p><span style=\" color:#878787;\">Easy to use - Free - Secure</span></p></body></html>", None))
        self.active_client_picture.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.active_client_name.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.active_client_status.setText(QCoreApplication.translate("MainWindow", u"Hello, i'm using AR Intercom !", None))
        self.last_seen.setText(QCoreApplication.translate("MainWindow", u"online a  few min ago", None))
        self.attachment_btn.setText("")
        self.delete_btn.setText("")
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Messages in this conversation are end-to-end encrypted. <br/>No one outside this chat can read or listen to them.</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u":)", None))
        self.emoji_tab_widget.setTabText(self.emoji_tab_widget.indexOf(self.tab_smileys), QCoreApplication.translate("MainWindow", u"Sm", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.emoji_tab_widget.setTabText(self.emoji_tab_widget.indexOf(self.tab_animals), QCoreApplication.translate("MainWindow", u"An", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.emoji_tab_widget.setTabText(self.emoji_tab_widget.indexOf(self.tab_foods), QCoreApplication.translate("MainWindow", u"Fo", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.emoji_tab_widget.setTabText(self.emoji_tab_widget.indexOf(self.tab_travels), QCoreApplication.translate("MainWindow", u"Tr", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.emoji_tab_widget.setTabText(self.emoji_tab_widget.indexOf(self.tab_activities), QCoreApplication.translate("MainWindow", u"Ac", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.emoji_tab_widget.setTabText(self.emoji_tab_widget.indexOf(self.tab_objects), QCoreApplication.translate("MainWindow", u"Ob", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.emoji_tab_widget.setTabText(self.emoji_tab_widget.indexOf(self.tab_symbols), QCoreApplication.translate("MainWindow", u"Sy", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.emoji_tab_widget.setTabText(self.emoji_tab_widget.indexOf(self.tab_flags), QCoreApplication.translate("MainWindow", u"Fl", None))
        self.close_emoji_btn.setText("")
        self.media_doc.setText("")
        self.media_audio.setText("")
        self.media_image.setText("")
        self.media_video.setText("")
        self.media_btn.setText("")
        self.emoji_btn.setText("")
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your message ...", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.send_btn.setText("")
        self.settings_title.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.breadcrumb.setText(QCoreApplication.translate("MainWindow", u"Settings > Account", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Mode clair", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mon compte", None))
        self.edit_profile_picture_btn.setText("")
        self.user_profile_picture.setText("")
        self.set_profile_label.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.username_btn.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.user_email.setText(QCoreApplication.translate("MainWindow", u"user@artrev.com", None))
        self.user_eail_btn.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.user_status.setText(QCoreApplication.translate("MainWindow", u"We live we love we die !", None))
        self.user_status_btn.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.user_role.setText(QCoreApplication.translate("MainWindow", u"Worker", None))
        self.user_role_btn.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.user_department.setText(QCoreApplication.translate("MainWindow", u"AR Label", None))
        self.user_department_btn.setText("")
        self.set_password_title.setText(QCoreApplication.translate("MainWindow", u"Change password", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Actual password", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"New password", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"New password again", None))
        self.error_label.setText(QCoreApplication.translate("MainWindow", u"Incorrect password", None))
        self.save_password_btn.setText(QCoreApplication.translate("MainWindow", u"Update password", None))
        self.status_bar.setText(QCoreApplication.translate("MainWindow", u"Creative Mind", None))
    # retranslateUi

