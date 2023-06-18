# -*- This python file uses the following encoding : utf-8 -*-
import os.path
import sys
import socket
import time


class Client:
    """
    Client to ask connection on different servers, and send them messages.
    """
    # CLIENT ID DEFINED BY HOST ADDRESS
    CLIENT_ID = socket.gethostbyname(socket.gethostname())

    # Port Unique for all clients
    PORT = 12001

    def __init__(self, server_host="localhost"):
        self.host = server_host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect_to_server(self):
        """
        Try to connect to a distant server.
        """
        while True:
            time.sleep(5)
            try:
                self.sock.connect((self.host, self.PORT))
                print(f"Connected with host {self.host}:{self.PORT}")
                self.connected = True
                break
            except Exception as e:
                print(f"Error while trying to connect on server {self.host}:{self.PORT} : ", e)
                self.connect_to_server()

    def reliable_send(self, message):
        try:
            self.sock.send(message)
            server_response = self.sock.recv(1024).decode()
            print(server_response)
        except Exception as e:
            print("Error while sending message: ", e)
            # Need to catch 2 exceptions,
            # One if the message was not sent
            # Another if the server doesn't respond
            message_sent = False

    def upload_file(self, path):
        size = os.path.getsize(path)
        print(f"Sending file {size} KB")
        with open(path, "rb") as file:
            self.sock.send(file.read())

    def send_message(self, kind, message):
        """
        Send message and try to receive status report
        """
        if kind == "text":
            # SEND CLIENT ID AND HIS TEXT MESSAGE
            text_message = f"{self.CLIENT_ID}|{kind}|{message}".encode()
            self.reliable_send(text_message)

        else:  # If kind in [image, document, video, audio, voice]
            path = message

            # COLLECT MEDIA METADATA FIRST
            file_size = os.path.getsize(path)
            file_name = os.path.split(path)[1]

            # SEND CLIENT ID AND FILE INFORMATION THEN UPLOAD FILE
            media_message = f"{self.CLIENT_ID}|{kind}|{file_size}|{file_name}".encode()
            self.reliable_send(media_message)
            self.upload_file(path)

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
        message_type = input("Choose an option :\n1.Text message\n2.Media message\n3.Exit\n>>> ")

        if message_type == "1":
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
