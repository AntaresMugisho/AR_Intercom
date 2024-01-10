import hashlib
import uuid

from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import Relationship
from sqlalchemy.exc import InvalidRequestError

from model.base import engine, Model, TimeStampedModel


class User(TimeStampedModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(256))
    host_address = Column(String(16))
    host_name = Column(String(64))
    user_name = Column(String(64))
    email = Column(String(128))
    phone = Column(String(16))
    user_status = Column(String(512))
    password = Column(String(256))
    image_path = Column(String(512))
    department = Column(String(256))
    role = Column(String(256))

    sent_messages = Relationship("Message",
                                back_populates="sender",
                                foreign_keys="Message.sender_id",
                                uselist=True,
                                passive_deletes=True
                                )

    received_messages = Relationship("Message",
                                     back_populates="receiver",
                                     foreign_keys="Message.receiver_id",
                                     uselist=True,
                                     passive_deletes=True
                                     )

    def __repr__(self):
        return f"{self.__class__.__name__} => id: {self.id}, uuid: {self.uuid}, username: {self.user_name}, " \
               f"hostname: {self.host_name}, ip: {self.host_address}, phone: {self.phone}, email: {self.email}, " \
               f"password: {self.password}, image: {self.image_path}, department: {self.department}, role: {self.role}"

    def set_uuid(self):
        self.uuid = str(uuid.uuid4())

    def set_password(self, password: str):
        self.password = hashlib.sha1(password.encode()).hexdigest()


class Message(TimeStampedModel):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    receiver_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    kind = Column(String(32))
    body = Column(Text())
    received = Column(Boolean)

    sender = Relationship('User', foreign_keys=[sender_id])
    receiver = Relationship('User', foreign_keys=[receiver_id])

    def __repr__(self):
        return f"{self.__class__.__name__}, sender: {self.sender_id}, receiver: {self.receiver_id} message: {self.body}," \
               f"sent_at: {self.created_at}, received: {self.received}"


if __name__ == "__main__":
    try:
        Model.metadata.create_all(engine)
    except InvalidRequestError:
        pass

