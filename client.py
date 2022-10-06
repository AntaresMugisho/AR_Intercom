# -*- This python file uses the following encoding : coding:utf-8 -*-

import socket
from tkinter import messagebox

class Client:

    prefixe = ""

    def __init__(self, port):

        self.hote = "ANTARES.local"
        self.port = port

        # Setting the status of connection at False by default
        self.connected = False

    def create_socket_client(self):
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        """Essaye de connecter le client au serveur demandé."""

        try:
            sock.connect((self.hote, self.port))
            self.connected = True   # The user will be informed by the green online toast canvas.

        except ConnectionRefusedError:
            pass
            #self.connected = False    # Do nothing if the requested server is not online

        except:  # Other Errors
            self.connected = False

    def send_message(self, msg_body):
        """Envoi le message au destinataire et essaie de montrer l'accusé de réception."""
        # Concatenate prefixe
        msg_body = Client.prefixe + msg_body

        # Coding in utf-8 to enable the send of print charaters
        msg_body = msg_body.encode("utf8")

        try:
            sock.send(msg_body)     # Try to send message

        except ConnectionResetError:
            # Show error if message is not received
            messagebox.showerror("Message non envoyé",
                "Le message n'a pas pu être envoyé car le destinataire s'est déconnecté.")

        except OSError:
            pass

        try:
            msg_recu = sock.recv(1024).decode("utf8")

        except OSError:
            pass

    def disconnect(self):
        """Ferme le socket."""
        sock.close()

# NO TRYING IN THIS