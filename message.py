# -*- This python file uses the following encoding : utf-8 -*-

import select
import os
import sys
import time

from PyQt6.QtCore import QObject, pyqtSignal as Signal

from server import Server


class Message(QObject):
    new_message = Signal()
    new_file = Signal()

    def receive_message(self):
        """
        Receive message and send status report
        """
        try:
            rlist, wlist, xlist = select.select(Server.CONNECTED_CLIENTS, [], [], 0.50)

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