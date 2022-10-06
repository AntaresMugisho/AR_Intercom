# -*- This python file uses the following encoding : coding:utf-8 -*-

import socket
import select
from Popup import popup

class Serveur:

    def __init__(self):

        self.port = 12101
        self.user_code = "Alpha"

        # Creating list of connected clients
        self.connected = []

        # List of clients that have sent messages
        self.readlist = []

        self.create_socket_server()
        self.launch_server()

    # Creation du socket
    def create_socket_server(self):
        global connexion_principale

        host = "0.0.0.0"

        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connexion_principale.bind((host, self.port))
        except OSError:
            pass

        else:
            connexion_principale.listen(5)
            print("Waiting for connections ...\n")

    # Accept connections and wait for messages
    def launch_server(self):
        """ Cette fonction a pour rôle d'accepter des connexions multiples venant des clients différents
        qui demandent probablement à se connecter,
        ainsi que de lire les messages reçus grêce à l'appel de la fontion 'receive_message'."""

        while True:
            attente, wlist, xlist = select.select([connexion_principale], [], [], 0.50)

            for connexion in attente:
                connexion_avec_client, adresse = connexion.accept()  # Acceptation de la connexion pour chaque demande
                self.connected.append(connexion_avec_client)  # Incrémentation de la liste des clients connectés

            try:
                self.readlist, wlist, xlist = select.select(self.connected, [], [], 0.50)

            except select.error:  # Exception lévée au cas où la liste des clients connectés serait vide
                pass

            else:
                self.receive_message()

    # Recieve message and send status
    def receive_message(self):
        """Parcours la liste des clients à lire."""
        for client in self.readlist:

            try:
                self.msg_recu = client.recv(1024)
                self.msg_recu = self.msg_recu.decode("utf8")

                splited = self.msg_recu.split(".")

                self.sender = splited[0]
                self.body = splited[1]

                popup(self.sender)
                print(f"{self.sender} | {self.body}")

            except ConnectionError:
                print("Erreur de connexion.")

            else:
                # Reply
                server_reply = input(f"{self.user_code} | ")
                server_reply = self.user_code + "." + server_reply
                server_reply = server_reply.encode("utf8")
                try:
                    client.send(server_reply)
                except:
                    pass

    def close_socket_server(self):
        connexion_principale.close()

# Server test
if __name__ == "__main__":
    run = Serveur()