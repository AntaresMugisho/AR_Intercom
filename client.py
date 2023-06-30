# -*- This python file uses the following encoding : utf-8 -*-
import os
import socket
import time

import utils
from user import User
from message import Message

class Client:
    """
    Client to ask connection on different servers, and send them messages.
    """
    # OWNER SERVER IP ADDRESS
    SERVER_IP = utils.get_private_ip()

    # Port Unique for all clients
    PORT = 12000

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
            self.sock.connect((self.server_host, self.PORT))
            print(f"[+] Connected on {self.server_host}:{self.PORT}")
            self.online = True

        except ConnectionRefusedError:
            print(f"[-] Connection refused on {self.server_host}:{self.PORT}")

        except Exception as e:
            print(f"[-] Error while trying to connect on server {self.server_host}:{self.PORT} : ", e)

        else:
            pass
            # Save user in the database if not exist
            # user_exists = User.where("host_address", "=", self.server_host)
            # if not user_exists:
            #     user = User()
            #     user.set_host_address(self.server_host)
            #     user.set_user_name(f"<{self.server_host}>")
            #     user.save()

            # If I find the user online, just send him my IDS, he will do the same
            # print(f"Hello {self.server_host}, take my IDs")
            # self.send_message("id")

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
            print("Error while sending message: ", e)
            # Need to catch 2 exceptions,
            # One if the message was not sent
            # Another if the message was sent but the server didn't respond
            self.message_delivered = False

        self.message_delivered

    def send_message(self, kind: str, body: str = None):
        """
        Determines the kind of message and sends it.
        """
        self.connect_to_server()

        receiver = User.where("host_address", "=", self.server_host)[0]
        receiver_id = receiver.get_id()

        message = Message()
        message.set_sender_id(3)
        message.set_receiver_id(receiver_id)
        message.set_kind(kind)
        message.set_body(body)

        if kind == "text":
            # SEND CLIENT ID AND HIS TEXT MESSAGE
            text_message = f"{self.SERVER_IP}|{kind}|{body}"
            self.reliable_send(text_message)

            message.set_status(self.message_delivered)

        else:  # If kind in ["image", "document", "video", "audio", "voice"]
            path = body

            # COLLECT MEDIA METADATA FIRST
            file_size = os.path.getsize(path)
            file_name = os.path.split(path)[1]

            # SEND CLIENT ID AND FILE INFORMATION THEN UPLOAD FILE
            media_message = f"{self.SERVER_IP}|{kind}|{file_size}|{file_name}"
            self.reliable_send(media_message)
            self.upload_file(path)

            message.set_status(self.message_delivered)

        print(message.get_status())
        message.save()

        # if kind == "id":
        #     # GET MY IDS FROM DATABASE
        #     user_name = "Antares"
        #     user_status = "We live, we love, we die"
        #     department = "AR Software"
        #     role = "Security Analyst"
        #     profile_picture_path = 'user/profile.jpg'
        #     profile_picture_size = os.path.getsize(profile_picture_path)
        #     id_message = f"{self.SERVER_IP}|{kind}|{profile_picture_size}|{profile_picture_path}|" \
        #                  f"{user_name}|{user_status}|{department}|{role}"
        #
        #     # SEND MY IDS
        #     self.reliable_send(id_message)
        #     if profile_picture_path != "user/default.png":
        #         self.upload_file(profile_picture_path)

    def upload_file(self, path: str):
        """
        Sends file to the distant server and returns delivery status
        """
        with open(path, "rb") as file:
            self.sock.send(file.read())
            try:
                self.sock.recv(1024)
                self.message_delivered = True
            except Exception as e:
                self.message_delivered = False
                print("Error while sending file: ", e)

        return self.message_delivered

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
