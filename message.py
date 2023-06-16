# -*- This python file uses the following encoding : utf-8 -*-

import select
import sys
import time

from PyQt6.QtCore import QObject, pyqtSignal as Signal

from server import Server
import utils


class Message(QObject):
    TEXT_MESSAGE_RECEIVED = Signal()
    MEDIA_MESSAGE_RECEIVED = Signal()

    # MESSAGE QUEUE LIST
    MESSAGE_QUEUE = []

    def receive_message(self):
        """
        Receive message and send status report
        """
        try:
            rlist, wlist, xlist = select.select(Server.CONNECTED_CLIENTS, [], [], 0.50)
            for client in rlist:
                try:
                    message = client.recv(1024).decode()
                    client.send("Received")
                except UnicodeDecodeError as e:
                    print("Seems that is media file", e)
                except Exception as e:
                    print(e)
        except select.error:
            # This error can occur if CONNECTED_CLIENTS list is empty
            pass

    def receive_text_message(self):
        # EMIT NEW TEXT MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        self.TEXT_MESSAGE_RECEIVED.emit()

    def receive_media_message(self, kind, filename):
        home_directory = utils.get_home_directory()
        kind = kind.capitalize()
        directory = f"{home_directory}/AR Intercom/Media/{kind}s/"

        # SET FILE NAME
        if kind == "voice":
            file_name = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}"
            file_extension = ".arv" if sys.platform == "win32" else ".wav"

        with open(f"{directory}{file_name}{file_extension}", "wb") as file:
            chunk = client.recv(1024)
            while chunk:
                file.write(chunk)
                try:
                    chunk = client.recv(1024)
                except Exception as e:
                    print("Erreur lors de la réception du fichier")
                    break

        # EMIT NEW MEDIA MESSAGE SIGNAL > TO SHOW GUI BUBBLE
        self.MEDIA_MESSAGE_RECEIVED.emit()
