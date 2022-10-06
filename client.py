# -*- This python file uses the following encoding : coding:utf-8 -*-

import socket
from Popup import popup

print("\n██████ AR INTERCOM Beta ██████\n Designed by a Creative Mind.\n"
      "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

class Client:

    def __init__(self):

        self.user_code = "Zulu"
        self.hote = "127.0.0.1" #"192.168.1.101"
        self.port = 12101
        self.connected = False

        self.create_socket_client()
        self.connect_to_server()

    def create_socket_client(self):
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Connecting...\n")
        i = 0
        while not self.connected:
            self.connect_to_server()
            i += 1
            if i % 4 == 0:
                print("Impossible de se conecter au serveur distant!")

            retry = str(input("\nAppuyez sur 'R' pour reessayer."))
            if retry.lower() == "r":
                i = 0

    def connect_to_server(self):
        """Essaye de connecter le client au serveur demandé."""

        try:
            sock.connect((self.hote, self.port))

        except ConnectionRefusedError:
            print("Connection error, retryng...")

        except:
            pass

        else:
            self.connected = True
            print("Connexion établie.\nCommencez la discussion.\n")
            self.send_message()

    def send_message(self):
        """Envoi le message au destinataire et essaie de montrer l'accusé de réception."""
        msg_body = str(input(f"{self.user_code} | "))
        msg_body = self.user_code + "." + msg_body
        # Coding in utf-8 to enable the send of print charaters
        msg_body = msg_body.encode("utf8")

        try:
            sock.send(msg_body)     # Try to send message

        except ConnectionResetError:
            print("Impossible d'envoyer le message car le serveur a été déconnecté.")

        except OSError:
            print("Erreur d'envoie.")

        try:
            msg_recu = sock.recv(1024).decode("utf8")
            splited = msg_recu.split(".")

            self.sender = splited[0]
            self.body = splited[1]

            popup(self.sender)
            print(f"{self.sender} | {self.body}")

        except OSError:
            print("Connexion interrompue.")

        else:
            self.send_message()

    def disconnect(self):
        """Ferme le socket."""
        sock.close()

# Client test
if __name__ == "__main__":
    run = Client()