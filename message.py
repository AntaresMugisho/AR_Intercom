# -*- This python file uses the following encoding : utf-8 -*-

from model import Model


class Message(Model):
    """
    Message model class representing a message as stored in database.
    This class contains also some signals that the server can emit on new incoming message
    to show GUI bubble
    """

    def __init__(self):
        self.id = None
        self.sender_id = None
        self.receiver_id = None
        self.kind = None
        self.body = None
        self.received = True
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

    def set_status(self, status: bool):
        self.received = status

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

    def get_status(self):
        return self.received


if __name__ == "__main__":
    message = Message()
    message.set_body("Hello world !")

    message.save()