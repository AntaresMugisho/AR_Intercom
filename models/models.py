

from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import Relationship

from models.base import engine, Model, TimeStampedModel


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
                                     uselist=True, passive_deletes=True
                                     )

    def __repr__(self):
        return f"{self.__class__.__name__}, hostname: {self.host_name} address: {self.host_address} username: {self.user_name}"


class Message(TimeStampedModel):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    receiver_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    kind = Column(String(32))
    body = Column(Text())
    received = Column(Boolean)

    sender = Relationship('User', foreign_keys=[sender_id], back_populates="sent_messages")
    receiver = Relationship('User', foreign_keys=[receiver_id], back_populates="received_messages")

    def __repr__(self):
        return f"{self.__class__.__name__}, message: {self.body} sent_at: {self.created_at}"


if __name__ == "__main__":
    Model.metadata.create_all(engine)

