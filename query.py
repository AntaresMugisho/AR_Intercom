
from model.base import session
from model import User, Message
from sqlalchemy.orm import joinedload



# Inserting
user1 = User()
user1.user_name = "Art Reception"
user1.host_name = "ART-RECEPTION"
user1.host_address = "192.168.1.112"
user1.department = "Reception"
user1.role = "Receptioniste"
user1.user_status = "We live, we love, we die !"
user1.phone = "+2439790"
user1.set_uuid()
user1.set_password("1234")

# session.add(user1)
# session.commit()

owner = User.query.first()
u4 = User.query.filter(User.id == 4).first()
u5 = User.query.filter(User.id == 5).first()


message = Message()
message.sender = owner
message.receiver = u4
message.body = "Hello"
message.kind = "text"
message.received = True


message1 = Message()
message1.sender = u4
message1.receiver = owner
message1.body = "Hello, how is it ?"
message1.kind = "text"
message1.received = True

message2 = Message()
message2.sender = u4
message2.receiver = owner
message2.body = "Hey ??"
message2.kind = "text"
message2.received = True

message3 = Message()
message3.sender = u4
message3.receiver = u5
message3.body = "Jabo"
message3.kind = "text"
message3.received = True

# session.add_all([message, message1, message2, message3])
# session.commit()


# # Querying
# users: list = User.query.all()
# first_user = User.query.first()
#
# print(first_user)
#
# messages = Message.query.all()

ms = u4.sent_messages

for m in ms:
    print(m)

# for message in messages:
#     print(message.sender)
# #
#
# # Updating
#
# # Deleting
