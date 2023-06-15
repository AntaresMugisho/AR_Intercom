# Form implementation generated from reading ui file 'popup_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Popup_win(object):
    def setupUi(self, Popup_win):
        Popup_win.setObjectName("Popup_win")
        Popup_win.resize(340, 105)
        self.global_frame = QtWidgets.QFrame(parent=Popup_win)
        self.global_frame.setGeometry(QtCore.QRect(5, 11, 331, 81))
        self.global_frame.setStyleSheet("QFrame{\n"
"    outline:none;\n"
"    background-color:grey;\n"
"    border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    background:none;\n"
"    font-family:Kirvy;\n"
"}")
        self.global_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.global_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.global_frame.setObjectName("global_frame")
        self.title = QtWidgets.QLabel(parent=self.global_frame)
        self.title.setGeometry(QtCore.QRect(80, 2, 221, 31))
        self.title.setStyleSheet("QLabel{\n"
"    background:none;\n"
"    font:bold 18px;\n"
"}")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.title.setObjectName("title")
        self.logo = QtWidgets.QPushButton(parent=self.global_frame)
        self.logo.setGeometry(QtCore.QRect(2, -1, 85, 85))
        self.logo.setStyleSheet("QPushButton{\n"
"    image: url(:/icons/icons/AR_logo.png);\n"
"    background:none;\n"
"    border:none;\n"
"}")
        self.logo.setObjectName("logo")
        self.sender_name = QtWidgets.QLabel(parent=self.global_frame)
        self.sender_name.setGeometry(QtCore.QRect(80, 32, 221, 31))
        self.sender_name.setStyleSheet("QLabel{\n"
"    background:none;\n"
"    font: bold 16px;\n"
"}")
        self.sender_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sender_name.setObjectName("sender_name")
        self.app_name = QtWidgets.QLabel(parent=self.global_frame)
        self.app_name.setGeometry(QtCore.QRect(215, 60, 101, 20))
        self.app_name.setStyleSheet("QLabel{\n"
"    background:none;\n"
"    color:#EcEcEc;\n"
"}")
        self.app_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.app_name.setObjectName("app_name")

        self.retranslateUi(Popup_win)
        QtCore.QMetaObject.connectSlotsByName(Popup_win)

    def retranslateUi(self, Popup_win):
        _translate = QtCore.QCoreApplication.translate
        Popup_win.setWindowTitle(_translate("Popup_win", "AR Notifier"))
        self.title.setText(_translate("Popup_win", "<html><head/><body><p><span style=\" font-size:10pt;\">Nouveau message</span></p></body></html>"))
        self.sender_name.setText(_translate("Popup_win", "<html><head/><body><p>Un message de Antares</p></body></html>"))
        self.app_name.setText(_translate("Popup_win", "<html><head/><body><p><span style=\" font-size:7pt;\">AR Intercom 2</span></p></body></html>"))
