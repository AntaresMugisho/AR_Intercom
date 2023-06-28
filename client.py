# -*- This python file uses the following encoding : utf-8 -*-
import os
import socket
import time

import utils
from user import UserController, User


class Client:
    """
    Client to ask connection on different servers, and send them messages.
    """
    # OWNER SERVER IP ADDRESS
    SERVER_IP = utils.get_private_ip()

    # Port Unique for all clients
    PORT = 12000

    def __init__(self, server_host="localhost"):
        self.server_host = server_host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.online = False

    def connect_to_server(self):
        """
        Try to connect to a distant server every 5 seconds.
        """
        try:
            self.sock.connect((self.server_host, self.PORT))
            print(f"[*] Connected on {self.server_host}:{self.PORT}")
            self.online = True

            # Save user in the database if not exist
            user_exists = UserController().where("host_address", "=", self.server_host)
            if not user_exists:
                user = User()
                user.set_uuid(self.server_host)
                user.set_host_address(self.server_host)
                user.set_user_name("Inconnu")
                UserController().store(user)
        except ConnectionRefusedError:
            print(f"[X] Connection refused on {self.server_host}:{self.PORT}")

        except Exception as e:
            print(f"[X] Error while trying to connect on server {self.server_host}:{self.PORT} : ", e)

    def reliable_send(self, message):
        """
        Sends message using socket's 'send' function and receive feed back from the server.
        """
        try:
            self.sock.send(message.encode())
            server_response = self.sock.recv(1024).decode()
            print(server_response)
        except Exception as e:
            print("Error while sending message: ", e)
            # Need to catch 2 exceptions,
            # One if the message was not sent
            # Another if the server doesn't respond
            message_sent = False

    def send_message(self, kind: str, message: str = None):
        """
        Determines the kind of message and sends it.
        """
        if kind == "id":
            # GET MY IDS FROM DATABASE
            user_name = "Antares"
            user_status = "We live, we love, we die"
            department = "AR Software"
            role = "Security Analyst"
            profile_picture_path = 'user/profile.jpg'
            profile_picture_size = os.path.getsize(profile_picture_path)
            id_message = f"{self.SERVER_IP}|{kind}|{profile_picture_size}|{profile_picture_path}|" \
                         f"{user_name}|{user_status}|{department}|{role}"

            # SEND MY IDS
            self.reliable_send(id_message)
            if profile_picture_path != "user/default.png":
                self.upload_file(profile_picture_path)

        elif kind == "text":
            # SEND CLIENT ID AND HIS TEXT MESSAGE
            text_message = f"{self.SERVER_IP}|{kind}|{message}"
            self.reliable_send(text_message)

        else:  # If kind in ["image", "document", "video", "audio", "voice"]
            path = message

            # COLLECT MEDIA METADATA FIRST
            file_size = os.path.getsize(path)
            file_name = os.path.split(path)[1]

            # SEND CLIENT ID AND FILE INFORMATION THEN UPLOAD FILE
            media_message = f"{self.SERVER_IP}|{kind}|{file_size}|{file_name}"
            self.reliable_send(media_message)
            self.upload_file(path)

    def upload_file(self, path: str):
        """
        Sends file to the distant server
        """
        with open(path, "rb") as file:
            self.sock.send(file.read())

    def disconnect(self):
        """
        Close the client socket.
        """
        self.sock.close()


if __name__ == "__main__":
    client = Client()
    client.connect_to_server()

    # This while loop will run only if the connection is established
    while True:
        message_type = input("Choose an option :\n0.IDs\n1.Text message\n2.Media message\n3.Exit\n>>> ")

        if message_type == "0":
            message_type = "id"
            message = "user/profile.jpg"

        elif message_type == "1":
            message_type = "text"
            message = input("Type your text message\n>>> ")

        elif message_type == "2":
            media_types = ["audio", "image", "video", "document", "voice"]
            media_type = input("1.Audio 2.Image 3.Video 4.Document 5.Voice\n>>> ")
            message_type = media_types[int(media_type)-1]

            message = input("Enter the file path\n>>> ")
        else:
            client.disconnect()
            print("See you again !")
            break

        # SEND MESSAGE
        client.send_message(message_type, message)
