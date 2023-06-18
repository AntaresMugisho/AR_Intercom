# -*- This python file uses the following encoding : utf-8 -*-

from PyQt6.QtCore import QObject, pyqtSignal


class Message(QObject):
    textMessageReceived = pyqtSignal([str, str])
    mediaMessageReceived = pyqtSignal()

    def text_message_received(self, kind, message_body):
        # EMIT NEW TEXT MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        self.textMessageReceived.emit(kind, message_body)

    def media_message_received(self, kind, file_name=None):
        # EMIT NEW MEDIA MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        self.mediaMessageReceived.emit(kind, file_name)





if __name__ == "__main__":
    message = Message()
    message.textMessageReceived.connect(lambda x, y:print(y))
    message.textMessageReceived.emit("text", "Hello world !")