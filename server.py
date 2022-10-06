# -*- This python file uses the following encoding : coding:utf-8 -*-

import socket
import select
from interface import UserInteface

# Création de la classe Server
class Serveur(UserInteface) :

    def __init__(self):

        self.user_code = ""
        self.port = ""

        # Creatind list of connected clients
        self.connected = []

        # list of clients that have sent messages
        self.readlist = []

    # Creation des setters
    def set_usercode(self, p):
        self.user_code = p

    def set_port(self):
        self.get_user_code()
        for x in self.dictionnary.keys():
            if x == self.user_code:
                self.port = self.dictionnary[x]

    # Création des getters
    def get_user_code(self):
        return self.user_code

    def get_port(self):
        return self.port

    # Creation du socket
    def create_socket_server(self):
        global connexion_principale

        hote = "0.0.0.0"

        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connexion_principale.bind((hote, self.port))
        except OSError:
            pass
            #messagebox.showwarning("Nom de code reservé",
               # "Une autre personne est connecté avec votre nom de code!")
        else:
            connexion_principale.listen(5)

    # Accept connections and wait for messages
    def launch_server(self):
        """ Cette fonction a pour rôle d'acceter des connexions multiples venant des clients différents
        qui demandent probablement à se connecter,
        ainsi que de lire les messages reçus grêce à l'appel de la fontion 'receive_message'."""

        while True :
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

            except ConnectionError:
                pass
                # If the current client is disconnected, pass and search for another

            else:
                # Send status
                server_reply = "Received"
                server_reply = server_reply.encode("utf8")
                try:
                    client.send(server_reply)
                except:
                    pass

                # Save mesasge and show popup
                lf_text = self.cadre_discussions.cget("text")

                if self.msg_recu != "":
                    if lf_text == "" or lf_text[0] != self.msg_recu[0]:
                        self.put_inbox()    # Save message in the file

                    else:
                        self.receive_msg_bubble()

    def close_socket_server(self):
        connexion_principale.close()

# ===================================================== END ============================================================