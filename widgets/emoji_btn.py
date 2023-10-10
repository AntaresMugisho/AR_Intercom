# -*- This python file uses the following encoding : utf-8 -*-

from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize, Signal


class EmojiButton(QPushButton):

    emojiClicked = Signal(str)

    def __init__(self, emoji):
        QPushButton.__init__(self)

        self.emoji = emoji

        self.setObjectName(u"select_emoji_btn")
        self.setMinimumSize(QSize(35, 35))
        self.setMaximumSize(QSize(35, 35))
        font12 = QFont()
        font12.setPointSize(16)
        self.setFont(font12)
        self.setStyleSheet(u"QPushButton{border:none;background-color:#333;}"
                           u"QPushButton:hover{background-color:#444;}")
        self.setText(self.emoji)

        self.clicked.connect(lambda : self.emojiClicked.emit(self.text))
