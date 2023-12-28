# -*- This python file uses the following encoding : utf-8 -*-
import os.path
import socket
import select
import threading
import sys
import time

from PySide6.QtCore import QObject, Signal

import utils
from message import Message
from user import User


class Server(QObject):
    """
    Server to listen, accept connections and receive text messages and files from other connected devices.
    """
    messageReceived = Signal(int)
    idRequested = Signal(str)
    userAdded = Signal()

    # ONLINE CLIENTS LIST
    CONNECTED_CLIENTS = []
    CONNECTED_CLIENTS_IPS = []

    def __init__(self):
        QObject.__init__(self)
        self.host = "0.0.0.0"
        self.port = 33522
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
                print("[-] Error in server :", e)
                break

    def start(self):
        """
        Launch socket server and accept incoming connections.
        """
        try:
            self.sock.bind((self.host, self.port))
        except OSError as e:
            print("[-] Error while trying to bind host", e)
        else:
            self.sock.listen(5)
            print(f"[+] Server listening on {self.host}:{self.port}")

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
        print("[i] Server closed.")

    def receive_massages(self):
        """
        Receive messages and send status report
        """
        print("[+] Waiting for messages...")
        while True:
            try:
                rlist, wlist, xlist = select.select(self.CONNECTED_CLIENTS, [], [], 0.50)
            except select.error:
                # This error can occur if CONNECTED_CLIENTS list is empty
                pass
            else:
                for client in rlist:
                    try:
                        packet = client.recv(1024).decode()
                        client.send("[+] Message sent and received successfully".encode())
                        packet = packet.split("|")
                        client_id = packet[0]
                        client_address = client.getpeername()[0]
                        message_kind = packet[1]

                    except BrokenPipeError:
                        pass

                    except IndexError:
                        pass

                    except ConnectionAbortedError:
                        pass

                    except Exception as e:
                        # pass
                        print("[-] Error while receiving message", e)

                    else:

                        sender = User.first_where("uuid", "=", client_id)
                        if sender is not None:
                            sender_id = sender.get_id()
                        else:
                            sender_id = 1

                        message = Message()
                        message.set_sender_id(sender_id)
                        message.set_receiver_id(1)
                        message.set_kind(message_kind)

                        if message_kind == "ID_REQUEST":
                            self.idRequested.emit(client_address)

                        elif message_kind == "ID_RESPONSE":
                            profile_picture_size = int(packet[2])
                            profile_picture_path = packet[3]
                            host_name = packet[4]
                            user_name = packet[5]
                            user_status = packet[6]
                            department = packet[7]
                            role = packet[8]
                            phone = packet[9]

                            if profile_picture_path != "user/default.png":
                                extension = os.path.splitext(profile_picture_path)[1]
                                file_name = f"{client_id[:7]}_profile{extension}"
                                self.download_file(client, message_kind, profile_picture_size, file_name)

                            # Store or update user's information in database
                            if sender is not None:
                                user = sender
                            else:
                                user = User()

                            user.set_uuid(client_id)
                            user.set_host_name(host_name)
                            user.set_user_name(user_name)
                            user.set_host_address(client_address)
                            user.set_phone(phone)
                            user.set_image_path(profile_picture_path)
                            user.set_user_status(user_status)
                            user.set_department(department)
                            user.set_role(role)

                            print(f"User received info : {user.__dict__}")

                            if sender is not None:
                                user.update()
                            else:
                                user.save()

                            self.userAdded.emit()

                        elif message_kind == "text":
                            # Call signal sender
                            message_body = packet[2]

                            message.set_body(message_body)
                            # Save message and emit signal so that it can be displayed in the GUI
                            message.save()
                            self.messageReceived.emit(message.get_id())

                        elif message_kind in ["image", "document", "video", "audio", "voice"]:
                            # Download file
                            file_size = int(packet[2])
                            file_name = packet[3]
                            path = self.download_file(client, message_kind, file_size, file_name)

                            message.set_body(path)

                            # Save message and emit signal so that it can be displayed in the GUI
                            message.save()
                            self.messageReceived.emit(message.get_id())



    @staticmethod
    def download_file(client_socket, kind: str, file_size: int, file_name: str):
        """
        Download and save file from distant client machine.
        """
        home_directory = utils.get_home_directory()
        directory = f"{home_directory}/AR_Intercom/Media/{kind.capitalize()}s"

        # SET DIFFERENT DIRECTORY IF IT IS A PROFILE PICTURE
        if kind == "ID":
            directory = "user"

        # SET FILE NAME IF IT IS A VOICE
        elif kind == "voice":
            # file_extension = ".arv" if sys.platform == "win32" else ".wav"
            file_name = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}"

        # DOWNLOAD FILE
        with open(f"{directory}/{file_name}", "wb") as file:
            downloaded = b""
            while len(downloaded) < file_size:
                chunk = client_socket.recv(5_242_880)  # 5Mb per transaction
                file.write(chunk)
                downloaded += chunk
                # Show progression in console mode
                print("Downloading file...", str(round(len(downloaded) * 100 / file_size)), "%")

            # ONCE DOWNLOAD IS DONE
            client_socket.send("[!] File Received".encode())

        # Return the path where the file was stored so that we can save it in database
        return f"{directory}/{file_name}"


if __name__ == "__main__":
    server = Server()
    server.start()
