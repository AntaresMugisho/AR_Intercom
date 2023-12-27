# -*- This python file uses the following encoding : utf-8 -*-

import os
import socket

import utils
from user import User
from message import Message


class Client:
    """
    Client to ask connection on different servers, and send them messages.
    """
    # OWNER SERVER IP ADDRESS
    PRIVATE_IP = utils.get_private_ip()
    user = User.first_where("id", "=", 1)
    if user:
        UUID = user.get_uuid()

    # Port Unique for all clients
    PORT = 33511

    CONNECTED_SERVERS = []

    def __init__(self, server_host="127.0.0.1"):
        self.server_host = server_host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.online = False
        self.message_delivered = False

    def connect_to_server(self):
        """
        Try to connect to a distant server
        """
        try:
            self.sock.settimeout(1)
            self.sock.connect((self.server_host, self.PORT))
            print(f"[+] Connected on {self.server_host}:{self.PORT}")
            self.online = True
            self.sock.settimeout(None)
            self.CONNECTED_SERVERS.append(self.server_host)

        except ConnectionRefusedError:
            pass
            # print(f"[-] Connection refused on {self.server_host}:{self.PORT}")

        except Exception as e:
            pass
            # print(f"[-] Error while trying to connect on server {self.server_host}:{self.PORT} : ", e)

    def reliable_send(self, packet):
        """
        Sends message using socket's 'send' function and receive feed back from the server.
        """
        try:
            self.sock.send(packet.encode())
            server_response = self.sock.recv(1024).decode()
            self.message_delivered = True
            print(server_response)

        except Exception as e:
            print("[-] Error while sending message: ", e)
            # Need to catch 2 exceptions,
            # One if the message was not sent
            # Another if the message was sent but the server didn't send feedback
            self.message_delivered = False

    def send_message(self, message: Message):
        """
        Try to establish connection with the distant server and sends the given message.
        Returns the message after adding the report status (if received or not)
        """

        self.connect_to_server()
        message_kind = message.get_kind()

        if message_kind == "ID":
            # GET MY IDS FROM DATABASE
            me = User.first_where("id", "=", 1)
            print(f"User to send info : {me.__dict__}")
            host_name = me.get_host_name()
            user_name = me.get_user_name()
            user_status = me.get_user_status()
            department = me.get_department()
            role = me.get_role()
            profile_picture_path = me.get_image_path()

            profile_picture_size = os.path.getsize(profile_picture_path)

            id_message = f"{self.UUID}|{message_kind}|{profile_picture_size}|{profile_picture_path}|" \
                         f"{host_name}|{user_name}|{user_status}|{department}|{role}"

            # SEND ID MESSAGE
            # id_message = f"{self.UUID}|{message_kind}"
            self.reliable_send(id_message)
            if profile_picture_path != "user/default.png":
                self.upload_file(profile_picture_path)

        elif message_kind == "text":
            # SEND CLIENT ID AND HIS TEXT MESSAGE
            text_message = f"{self.UUID}|{message_kind}|{message.get_body()}"
            self.reliable_send(text_message)
            message.set_status(self.message_delivered)

        else:  # If kind in ["image", "document", "video", "audio", "voice"]
            path = message.get_body()

            # COLLECT MEDIA METADATA FIRST
            file_size = os.path.getsize(path)
            file_name = os.path.basename(path)

            # SEND CLIENT ID AND FILE INFORMATION THEN UPLOAD FILE
            media_message = f"{self.UUID}|{message_kind}|{file_size}|{file_name}"
            self.reliable_send(media_message)
            self.upload_file(path)

            message.set_status(self.message_delivered)

        return message



    def upload_file(self, path: str):
        """
        Sends file to the distant server and returns delivery status
        """
        with open(path, "rb") as file:
            try:
                self.sock.send(file.read())
                self.sock.recv(1024)
                self.message_delivered = True
            except Exception as e:
                self.message_delivered = False
                print("[-] Error while sending file: ", e)

    def disconnect(self):
        """
        Close the client socket.
        """
        self.sock.close()


if __name__ == "__main__":
    from message import Message

    client = Client()
    client.connect_to_server()

    # This while loop will run only if the connection is established
    while True:
        message_type = input("Choose an option :\n0.IDs\n1.Text message\n2.Media message\n3.Exit\n>>> ")
        message = Message()

        if message_type == "0":
            message.set_kind("ID")

        elif message_type == "1":
            text = input("Type your text message\n>>> ")
            message.set_kind("text")
            message.set_body(text)

        elif message_type == "2":
            media_types = ["audio", "image", "video", "document", "voice"]
            media_type = input("1.Audio 2.Image 3.Video 4.Document 5.Voice\n>>> ")
            message_type = media_types[int(media_type)-1]

            path = input("Enter the file path\n>>> ")
            message.set_kind(message_type)
            message.set_body(path)

        else:
            client.disconnect()
            print("See you again !")
            break

        # SEND MESSAGE
        client.send_message(message)
