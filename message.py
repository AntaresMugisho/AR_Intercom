# -*- This python file uses the following encoding : utf-8 -*-

from datetime import datetime

from PyQt6.QtCore import QObject, pyqtSignal

from database import Database


class Message(QObject):
    textMessageReceived = pyqtSignal([str, str])
    mediaMessageReceived = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.sender_id = None
        self.receiver_id = None
        self.kind = None
        self.body = None
        self.created_at = None
        self.updated_at = None
        self.deleted_at = None

    # SETTERS
    def set_sender_id(self, sender_id):
        self.sender_id = sender_id

    def set_receiver_id(self, receiver_id):
        self.receiver_id = receiver_id

    def set_kind(self, kind):
        self.kind = kind

    def set_body(self, body):
        self.body = body

    def set_created_at(self):
        self.created_at = datetime.now()

    def set_updated_at(self):
        self.updated_at = datetime.now()

    def set_deleted_at(self):
        self.deleted_at = datetime.now()

    # GETTERS
    def get_sender_id(self):
        return self.sender_id

    def get_receiver_id(self):
        return self.receiver_id

    def get_kind(self):
        return self.kind

    def get_body(self):
        return self.body

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

    def get_deleted_at(self):
        return self.deleted_at

    def text_message_received(self, kind, message_body):
        # EMIT NEW TEXT MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        self.textMessageReceived.emit(kind, message_body)

    def media_message_received(self, kind, file_name=None):
        # EMIT NEW MEDIA MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        self.mediaMessageReceived.emit(kind, file_name)


class MessageController:
    def __init__(self):
        self.db = Database()

    def with_user(self, user_id: int):
        statement = f"SELECT * FROM messages WHERE sender_id = {user_id} OR receiver_id = {user_id}"
        return self.db.fetch(statement)

    def store(self, message: Message):
        statement = """
        INSERT INTO messages (
            sender_id, receiver_id, kind, body, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        data = [
            message.get_sender_id(),
            message.get_receiver_id(),
            message.get_kind(),
            message.get_body(),
            message.get_created_at(),
            message.get_updated_at()
        ]

        self.db.execute(statement, data)


if __name__ == "__main__":
    message = Message()

    # message.set_sender_id(2),
    # message.set_receiver_id(1),
    # message.set_kind("text"),
    # message.set_body("I'm okay thanks!"),
    # message.set_created_at()
    # message.set_updated_at()

    controller = MessageController()
    # controller.store(message)
    for message in controller.with_user(3):
        print(message[4])
