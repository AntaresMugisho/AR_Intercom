# -*- This python file uses the following encoding : utf-8 -*-

import os
import socket

import utils
from model import User, Message


class Client:
    """
    Client to ask connection on different servers, and send them messages.
    """
    # OWNER SERVER IP ADDRESS
    PRIVATE_IP = utils.get_private_ip()
    UUID = None

    # Port Unique for all clients
    PORT = 33522

    CONNECTED_SERVERS = []

    def __init__(self, server_host):
        if Client.UUID is None:
            Client.UUID = User.query.first().uuid

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

        except Exception as e:
            print(f"ERR client : {e}")
            self.online = False
            try:
                self.CONNECTED_SERVERS.remove(self.server_host)
            except ValueError:
                pass

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
            # Another if the mess age was sent but the server didn't send feedback
            self.message_delivered = False

    def send_message(self, message: Message):
        """
        Try to establish connection with the distant server and sends the given message.
        Returns the message after adding the report status (if received or not)
        """

        self.connect_to_server()
        message_kind = message.get_kind()

        if message_kind == "ID_REQUEST":
            # SEND ID MESSAGE
            id_request = f"{self.UUID}|{message_kind}"
            self.reliable_send(id_request)

        elif message_kind == "ID_RESPONSE":
            # GET MY IDS FROM DATABASE
            me: User = User.filter(User.uuid == self.UUID).first()

            profile_picture_path = me.image_path
            if profile_picture_path is not None:
                profile_picture_size = os.path.getsize(profile_picture_path)
                self.upload_file(profile_picture_path)
            else:
                profile_picture_size = 0

            id_message = f"{self.UUID}|{message.kind}|{profile_picture_size}|{me.image_path}|" \
                         f"{me.host_name}|{me.user_name}|{me.user_status}|{me.department}|{me.role}|{me.phone}"
            self.reliable_send(id_message)

        elif message_kind == "text":
            # SEND CLIENT ID AND HIS TEXT MESSAGE
            text_message = f"{self.UUID}|{message.kind}|{message.body}"
            self.reliable_send(text_message)
            message.received = self.message_delivered

        elif message_kind in ["image", "document", "video", "audio", "voice"]:
            path = message.body

            # COLLECT MEDIA METADATA FIRST
            file_size = os.path.getsize(path)
            file_name = os.path.basename(path)

            # SEND CLIENT ID AND FILE INFORMATION THEN UPLOAD FILE
            media_message = f"{self.UUID}|{message_kind}|{file_size}|{file_name}"
            self.reliable_send(media_message)
            self.upload_file(path)

            message.received = self.message_delivered

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
    from model import Message

    client = Client("192.168.1.109")
    client.connect_to_server()

    # This while loop will run only if the connection is established
    while True:
        message_type = input("Choose an option :\n0.ID REQ\n1.Text message\n2.Media message\n3.Exit\n>>> ")
        message = Message()

        if message_type == "0":
            message.set_kind("ID_REQUEST")

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
