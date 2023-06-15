# -*- This python file uses the following encoding : coding:utf-8 -*-

import os
import sys
import threading
import time
import socket
import select

from PyQt6.QtCore import QObject, pyqtSignal


class Message(QObject):
    new_message = pyqtSignal()
    new_file = pyqtSignal()


class Server:
    """
    Server to listen, accept connections and receive text messages and files from other connected devices.
    """
    thread = None

    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 12000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # ONLINE CLIENTS LIST
        self.connected = []
        self.ips = []

        # MESSAGE QUEUE LIST
        self.queue = []

    def accept_connections(self):
        """
        Accept all incoming connections
        """
        while True:
            try:
                rlist, wlist, xlist = select.select([self.sock], [], [], 0.50)
                for connection in rlist:

                        client, ip_address = connection.accept()
                        self.connected.append(client)
                        self.ips.append(ip_address)
            except Exception as e:
                print("Error in server :", e)
                break

    def start(self):
        """
        Launch server and accept incoming connections.
        """
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        self.thread = threading.Thread(target=self.accept_connections)
        self.thread.start()
        # self.accept_connections()

    def stop(self):
        self.sock.close()
        print("Server closed !")


    def receive_message(self):
        """
        Receive message and send status report
        """

        # Receive message
        try:
            rlist, wlist, xlist = select.select(self.connected, [], [], 0.50)

        except select.error:
            # If 'connected' list is empty
            pass

        else:
            self.receive_message()

        for client in self.readlist:

            # TRY TO RECEIVE MESSAGE
            try:
                self.received_message = client.recv(1024)

            except ConnectionError:
                # If this error occurs (probably ConnectionAbortedError) no message will be received.
                pass

            else:
                # TRY TO DECODE IT
                try:
                    self.received_message = self.received_message.decode("utf8")

                except UnicodeDecodeError:
                    # If this error occurs, it means the message is a media file. It's not a problem.
                    pass

                finally:
                    # SEND STATUS REPORT
                    received = "1"
                    self.confirm_reception = received.encode("utf8")

                    try:
                        client.send(self.confirm_reception)
                    except:
                        pass

                    try:
                        if self.received_message[1] == "S":
                            # EMIT NEW TEXT MESSAGE SIGNAL > TO SHOW GUI BUBBLE
                            self.new_message.emit()

                        elif self.received_message[1] == "B":
                            # IF MESSAGE IS NOT STRING, COLLECT MEDIA INFO THEN EMIT 'NEW FILE' SIGNAL > TO SHOW  BUBBLE

                            spliter = self.received_message[2:].split(",")
                            self.media_info = {"Kind": f"{spliter[0]}", "Size": f"{spliter[1]}",
                                               "Title": f"{spliter[2]}", "Extension": f"{spliter[3]}"}

                            # CHOOSE FOLDER WHERE TO SAVE FILE (BYTES) ACCORDING TO OS
                            if sys.platform == "win32":
                                home = os.environ["USERPROFILE"]
                            else:
                                home = os.environ["HOME"]

                            # Building folder / path
                            file_folder = self.media_info["Kind"].capitalize() + "s"
                            directory = f"{home}/Documents/AR Intercom/Media/{file_folder}/"

                            # Set file title
                            if self.media_info["Kind"] == "voice":
                                f_title = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}"
                                self.media_info["Extension"] = ".wav" if sys.platform == "darwin" else ".arv"
                            else:
                                f_title = self.media_info["Title"]

                            self.media_info["Title"] = f_title

                            # RECEIVE AND WRITE BLOB (MEDIA CONTENT)
                            file = open(f"{directory}{self.media_info['Title']}{self.media_info['Extension']}", "ab")

                            self.data = b""
                            while len(self.data) < int(self.media_info["Size"]):

                                blob = client.recv(10240)   # Receive  10Kb/transaction

                                file.write(blob)

                                self.data += blob

                            # When it's done close file and emit new file signal to show widget
                            file.close()
                            self.new_file.emit()

                    except IndexError:
                        pass

                    except Exception as e:
                        print("ERR166 SR: ", e)



if __name__ == "__main__":
    server = Server()
    server.start()