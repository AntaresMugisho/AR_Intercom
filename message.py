# -*- This python file uses the following encoding : utf-8 -*-

from PyQt6.QtCore import QObject, pyqtSignal as Signal


class Message(QObject):
    TEXT_MESSAGE_RECEIVED = Signal()
    MEDIA_MESSAGE_RECEIVED = Signal()

    @classmethod
    def text_message_received(cls):
        # EMIT NEW TEXT MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        #cls.TEXT_MESSAGE_RECEIVED.emit()
        print("Text message received")

    @classmethod
    def media_message_received(cls):
        # EMIT NEW MEDIA MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        #cls.MEDIA_MESSAGE_RECEIVED.emit()
        print("Media message received")
