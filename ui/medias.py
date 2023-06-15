# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'medias.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QWidget)
from resources import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(722, 411)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 40, 91, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.arv_bubble = QFrame(self.centralwidget)
        self.arv_bubble.setObjectName(u"arv_bubble")
        self.arv_bubble.setGeometry(QRect(20, 20, 301, 70))
        self.arv_bubble.setStyleSheet(u"QFrame{\n"
"	background-color:#88FFFFFF;\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.arv_bubble.setFrameShape(QFrame.StyledPanel)
        self.arv_bubble.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.arv_bubble)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(52, 3, 241, 20))
        self.title.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)
        self.elapsed_time = QLabel(self.arv_bubble)
        self.elapsed_time.setObjectName(u"elapsed_time")
        self.elapsed_time.setGeometry(QRect(52, 49, 51, 16))
        self.elapsed_time.setStyleSheet(u"QLabel{\n"
"	background:#22FFFFFF;\n"
"	border-radius:8px;\n"
"}")
        self.elapsed_time.setAlignment(Qt.AlignCenter)
        self.total_time = QLabel(self.arv_bubble)
        self.total_time.setObjectName(u"total_time")
        self.total_time.setGeometry(QRect(241, 49, 51, 16))
        self.total_time.setStyleSheet(u"QLabel{\n"
"	background:#22FFFFFF;\n"
"	border-radius:8px;\n"
"}")
        self.total_time.setAlignment(Qt.AlignCenter)
        self.progress = QProgressBar(self.arv_bubble)
        self.progress.setObjectName(u"progress")
        self.progress.setGeometry(QRect(52, 33, 241, 5))
        self.progress.setStyleSheet(u"QProgressBar{\n"
"		background-color:#AAC5C5C5;\n"
"		border-radius:2px;\n"
"		border:none;\n"
"		text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{	\n"
"	   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 52, 93, 255), stop:1 rgba(0, 121, 215, 255));\n"
"		border-radius:2px;\n"
"\n"
"}")
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.slider = QSlider(self.arv_bubble)
        self.slider.setObjectName(u"slider")
        self.slider.setGeometry(QRect(52, 30, 241, 12))
        self.slider.setStyleSheet(u"QSlider{\n"
"	background:none;\n"
"}\n"
"\n"
"QSlider::groove{\n"
"	background:none;\n"
"	border:none;}\n"
"\n"
"QSlider::handle{\n"
"	height:12px;\n"
"	width:12px;\n"
"    background-color: rgb(0, 121, 215, 255);\n"
"	border-radius:6px;}\n"
"\n"
"QSlider::handle:hover{\n"
"	background-color: rgb(0, 52, 93, 255);}\n"
"\n"
"QSlider::handle:pressed{\n"
"	background-color: rgb(0, 121, 215, 255);}")
        self.slider.setMaximum(100)
        self.slider.setValue(0)
        self.slider.setSliderPosition(0)
        self.slider.setOrientation(Qt.Horizontal)
        self.play_button = QPushButton(self.arv_bubble)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(7, 16, 41, 41))
        self.play_button.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/cils/cils/cil-media-play.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position:center;\n"
"	border-radius:6px;\n"
"	border:none;\n"
"}")
        self.record_tip = QFrame(self.centralwidget)
        self.record_tip.setObjectName(u"record_tip")
        self.record_tip.setGeometry(QRect(20, 110, 161, 31))
        self.record_tip.setStyleSheet(u"QFrame{\n"
"	background-color:#88FFFFFF;\n"
"	border-radius:15px;\n"
"\n"
"}")
        self.record_tip.setFrameShape(QFrame.StyledPanel)
        self.record_tip.setFrameShadow(QFrame.Raised)
        self.record_time = QLabel(self.record_tip)
        self.record_time.setObjectName(u"record_time")
        self.record_time.setGeometry(QRect(45, 5, 71, 20))
        self.record_time.setStyleSheet(u"QLabel{\n"
"	background:#44FFFFFF;\n"
"	border-radius:none;\n"
"}")
        self.record_time.setAlignment(Qt.AlignCenter)
        self.end_record = QPushButton(self.record_tip)
        self.end_record.setObjectName(u"end_record")
        self.end_record.setGeometry(QRect(10, 5, 31, 20))
        self.end_record.setStyleSheet(u"QPushButton{\n"
"	image: url(:/cils/cils/cil-media-record-bl.png);\n"
"	background:#00FF00;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}")
        self.cancel_record = QPushButton(self.record_tip)
        self.cancel_record.setObjectName(u"cancel_record")
        self.cancel_record.setGeometry(QRect(119, 5, 31, 20))
        self.cancel_record.setStyleSheet(u"QPushButton{\n"
"	image: url(:/cils/cils/cil-media-stop-bl.png);\n"
"	background:#FF0000;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}")
        self.arv_bubble_2 = QFrame(self.centralwidget)
        self.arv_bubble_2.setObjectName(u"arv_bubble_2")
        self.arv_bubble_2.setGeometry(QRect(90, 220, 421, 101))
        self.arv_bubble_2.setStyleSheet(u"QFrame{\n"
"	background-color:#88FFFFFF;\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.arv_bubble_2.setFrameShape(QFrame.StyledPanel)
        self.arv_bubble_2.setFrameShadow(QFrame.Raised)
        self.slider_2 = QSlider(self.arv_bubble_2)
        self.slider_2.setObjectName(u"slider_2")
        self.slider_2.setGeometry(QRect(80, 30, 241, 12))
        self.slider_2.setStyleSheet(u"QSlider{\n"
"	background:none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"	background:none;\n"
"	height:4px;\n"
"	border:none;\n"
"	}\n"
"\n"
"QSlider::handle:horizontal{\n"
"	height:12px;\n"
"	width:12px;\n"
"	border-radius:6px;\n"
"	margin:-4px 10px -4px 10px;\n"
"    background-color: rgb(0, 121, 215, 255);}\n"
"	\n"
"QSlider::handle:hover{\n"
"	background-color: rgb(0, 52, 93, 255);}\n"
"\n"
"QSlider::handle:pressed{\n"
"	background-color: rgb(0, 121, 215, 255);}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"	background-color:grey;}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 52, 93, 255), stop:1 rgba(0, 121, 215, 255));}")
        self.slider_2.setMaximum(100)
        self.slider_2.setValue(0)
        self.slider_2.setSliderPosition(0)
        self.slider_2.setOrientation(Qt.Horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 722, 19))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.slider.sliderMoved.connect(self.progress.setValue)
        self.progress.valueChanged.connect(self.slider.setValue)
        self.progress.valueChanged.connect(self.label_3.setNum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"ARV-20062021-1200", None))
        self.elapsed_time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.total_time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.record_time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
    # retranslateUi

