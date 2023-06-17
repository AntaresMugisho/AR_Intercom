# -*- This python file uses the following encoding : utf-8 -*-

from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal as Signal


class Message(QObject):
    textMessageReceived = Signal(str)
    mediaMessageReceived = Signal()

    # def __init__(self):
    #     QObject.__init__(self)

    def text_message_received(self):
        # EMIT NEW TEXT MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        self.textMessageReceived.emit()
        print("Text message signal")

    def media_message_received(self):
        # EMIT NEW MEDIA MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        self.mediaMessageReceived.emit()
        print("Media message signal")


if __name__ == "__main__":
    message = Message()
    print(message.textMessageReceived.emit("Hello"))