# -*- This python file uses the following encoding : utf-8 -*-

from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton
from PySide6.QtGui import QFont, QCursor
from PySide6.QtCore import QSize, Qt, QRect


class DateLabel(QLabel):

    def __init__(self, text):
        QLabel.__init__(self)

        self.text = text

        self.setObjectName(u"date_label")
        self.setMaximumSize(QSize(120, 20))
        self.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
                                      "color:black;\n"
                                      "padding:4px;\n"
                                      "border-radius:4px;")
        self.setAlignment(Qt.AlignCenter)
        self.setText(self.text)