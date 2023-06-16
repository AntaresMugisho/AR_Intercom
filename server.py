# -*- This python file uses the following encoding : utf-8 -*-

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

        thread = threading.Thread(target=self.accept_connections)
        thread.start()

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
                for client in rlist:
                    try:
                        message = client.recv(1024).decode()
                        client.send("Text Message Received".encode())
                        client_id = message.split("|")[0]
                        message_kind = message.split("|")[1]
                        print(message)

                        if message_kind == "text":
                            Message.text_message_received()
                        else:
                            file_size = int(message.split("|")[2])
                            file_name = message.split("|")[3]
                            self.download_file(client, message_kind, file_size, file_name)
                            Message.media_message_received()
                    except BrokenPipeError:
                        pass

                    except Exception as e:
                        print("Error while receiving message", e)

            except select.error:
                # This error can occur if CONNECTED_CLIENTS list is empty
                print("Empty list")

    @staticmethod
    def download_file(client_socket, kind, file_size, file_name):
        # SET FILE NAME IF IT IS A VOICE
        if kind == "voice":
            file_extension = ".arv" if sys.platform == "win32" else ".wav"
            file_name = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}{file_extension}"

        home_directory = utils.get_home_directory()
        directory = f"{home_directory}/AR Intercom/Media/{kind.capitalize()}s"

        with open(f"{directory}/{file_name}", "wb") as file:
            downloaded = b""
            while len(downloaded) < file_size:
                chunk = client_socket.recv(20480)
                file.write(chunk)
                downloaded += chunk
                # Show progression in console mode
                print("Downloading file...", str(round(len(downloaded) * 100 / file_size)), "%")

            # ONCE DOWNLOAD IS DONE
            client_socket.send("Media Message Received".encode())


if __name__ == "__main__":
    server = Server()
    server.start()
    server.receive_massages()
