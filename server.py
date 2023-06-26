# -*- This python file uses the following encoding : utf-8 -*-
import os.path
import socket
import select
import threading
import sys
import time

import utils
from message import Message


class Server:
    """
    Server to listen, accept connections and receive text messages and files from other connected devices.
    """

    # ONLINE CLIENTS LIST
    CONNECTED_CLIENTS = []
    CONNECTED_CLIENTS_IPS = []

    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 12000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # MESSAGE OBJECT TO EMIT SIGNALS
        self.message = Message()

    def accept_connections(self):
        """
        Accept all incoming connections
        """
        while True:
            try:
                rlist, wlist, xlist = select.select([self.sock], [], [], 0.50)
                for connection in rlist:
                    client, ip_address = connection.accept()
                    self.CONNECTED_CLIENTS.append(client)
                    self.CONNECTED_CLIENTS_IPS.append(ip_address[0])
            except Exception as e:
                print("Error in server :", e)
                break

    def start(self):
        """
        Launch socket server and accept incoming connections.
        """
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        # Wait for connections and messages
        connections_thread = threading.Thread(target=self.accept_connections)
        messages_thread = threading.Thread(target=self.receive_massages)
        connections_thread.start()
        messages_thread.start()

    def stop(self):
        """
        Close socket server.
        """
        self.sock.close()
        print("Server closed !")

    def receive_massages(self):
        """
        Receive messages and send status report
        """
        print("Waiting for messages...")
        while True:
            try:
                rlist, wlist, xlist = select.select(self.CONNECTED_CLIENTS, [], [], 0.50)
            except select.error:
                # This error can occur if CONNECTED_CLIENTS list is empty
                print("Empty list")
            else:
                for client in rlist:
                    try:
                        packet = client.recv(1024).decode()
                        packet = packet.split("|")
                        client.send("Message Received".encode())
                        client_id = packet[0]
                        message_kind = packet[1]
                        print(packet)

                        if message_kind == "id":
                            profile_picture_size = int(packet[2])
                            profile_picture_path = packet[3]
                            user_name = packet[4]
                            user_status = packet[5]
                            department = packet[6]
                            role = packet[7]

                            if profile_picture_path != "user/default.png":
                                extension = os.path.splitext(profile_picture_path)[1]
                                file_name = f"{client_id}_profile{extension}"
                                self.download_file(client, message_kind, profile_picture_size, file_name)

                        elif message_kind == "text":
                            # Call signal sender
                            message_body = packet[2]
                            self.message.text_message_received(message_kind, message_body)

                        else:
                            # Download file
                            file_size = int(packet[2])
                            file_name = packet[3]
                            self.download_file(client, message_kind, file_size, file_name)
                            # Call signal sender
                            self.message.media_message_received(message_kind)

                    except BrokenPipeError:
                        pass

                    except IndexError:
                        pass

                    except Exception as e:
                        print("Error while receiving message", e)

    @staticmethod
    def download_file(client_socket, kind: str, file_size: int, file_name: str):
        """
        Download and save file from distant client machine.
        """
        home_directory = utils.get_home_directory()
        directory = f"{home_directory}/AR Intercom/Media/{kind.capitalize()}s"

        # SET DIFFERENT DIRECTORY IF IT IS A PROFILE PICTURE
        if kind == "id":
            directory = "user"

        # SET FILE NAME IF IT IS A VOICE
        elif kind == "voice":
            file_extension = ".arv" if sys.platform == "win32" else ".wav"
            file_name = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}{file_extension}"

        # DOWNLOAD FILE
        with open(f"{directory}/{file_name}", "wb") as file:
            downloaded = b""
            while len(downloaded) < file_size:
                chunk = client_socket.recv(10240)
                file.write(chunk)
                downloaded += chunk
                # Show progression in console mode
                print("Downloading file...", str(round(len(downloaded) * 100 / file_size)), "%")

            # ONCE DOWNLOAD IS DONE
            client_socket.send("File Received".encode())


if __name__ == "__main__":
    server = Server()
    server.start()
