# -*- This python file uses the following encoding : utf-8 -*-

from datetime import datetime

from PyQt6.QtCore import QObject, pyqtSignal

from controller import Controller


class Message(QObject, Controller):
    """
    Message model class representing a message as stored in database.
    This class contains also some signals that the server can emit on new incoming message
    to show GUI bubble
    """
    messageReceived = pyqtSignal(int)
    # mediaMessageReceived = pyqtSignal()
    time_format = "%d-%m-%Y %H:%M"

    def __init__(self):
        QObject.__init__(self)

        self.id = None
        self.sender_id = None
        self.receiver_id = None
        self.kind = None
        self.body = None
        self.created_at = None
        self.updated_at = None
        self.deleted_at = None
        self.received = True

    # SETTERS
    def set_sender_id(self, sender_id):
        self.sender_id = sender_id

    def set_receiver_id(self, receiver_id):
        self.receiver_id = receiver_id

    def set_kind(self, kind):
        self.kind = kind

    def set_body(self, body):
        self.body = body

    def set_status(self, status: bool):
        self.received = status

    def set_created_at(self):
        self.created_at = datetime.now()

    def set_updated_at(self):
        self.updated_at = datetime.now()

    def set_deleted_at(self):
        self.deleted_at = datetime.now()

    # GETTERS
    def get_id(self):
        return self.id

    def get_sender_id(self):
        return self.sender_id

    def get_receiver_id(self):
        return self.receiver_id

    def get_kind(self):
        return self.kind

    def get_body(self):
        return self.body

    def get_created_at(self):
        return datetime.fromisoformat(self.created_at).strftime(self.time_format)

    def get_updated_at(self):
        return datetime.fromisoformat(self.updated_at).strftime(self.time_format)

    def get_deleted_at(self):
        return datetime.fromisoformat(self.deleted_at).strftime(self.time_format)

    def get_status(self):
        return self.received
