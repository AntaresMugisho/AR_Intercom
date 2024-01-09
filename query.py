
from models import User, Message


users: list = User.query.all()

first_user = User.query.first()

print(first_user)
