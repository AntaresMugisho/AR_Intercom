# -*- This python file uses the following encoding : coding:utf-8 -*-

# ================================================ IMPORTING PACKAGES ==================================================

# My own modules
from server import Serveur
from interface import UserInteface
from client import Client
from popup import popup

# Python Library
import time, threading, os

from sqlite3 import *
from tkinter import *
from tkinter import messagebox

# ----------------------------------------------------------------------------------------------------------------------

class Callbacks (Serveur, UserInteface):
    """Commandes de l'interface du logiciel pour interagir avec l'utilisateur."""

    last_row = 1

    def __init__(self) -> object:
        Serveur.__init__(self)
        UserInteface.__init__(self)

# ------------------------------------------------ COMMAND FUNCTIONS ---------------------------------------------------
    def quitter(self):
        """Quitter le programme"""
        if messagebox.askyesno("Quitter AR Intercom", "Voulez-vous vraiment quitter AR Intetcom ?"):
            try:
                self.close_socket_server()
                self.client.disconnect()
            except:
                pass
            self.window.quit()

    def signin(self, *event):
        """Cache la fênetre de connexion (Login window) et affiche celle d'Inscription ("Signin window)."""
        # Called on clicked "Créer un compte" in the login window

        self.central_login.pack_forget()  # Hiding the login window
        self.signin_window()

    def hide_signin_window(self, *event):
        """Cache la fenêtre d'inscription (Sign in window) et affiche celle de connexion (Log in window)."""
        # Called on clicked button "Créer un compte" in the log in window
        # Also called as event funtion on clicked "Left arrow" in the sign in window

        self.central_signin.pack_forget()
        self.login_window()

    def registrer(self):
        """Vérifie si l'utilisateur a saisi toutes les données lui demandées avec leur conformité.
        Si toutes les conditions sont respectées, alors elle appelle les autres fonctions nécessaires
        notamment pour l'enregistrement dans la base de données."""
        # Called on clicked button "Valider" in the sign in window

        self.client_id["nom"] = self.var_nom.get()
        self.client_id["code"] = self.var_codename.get()
        self.client_id["mdp"] = self.var_mdp.get()
        self.client_id["conf_mdp"] = self.var_conf_mdp.get()
        #self.client_id["phone"] = self.var_number.get()

        for i in self.client_id.keys():

            if self.client_id[i] == "":
                messagebox.showerror("Champs vides détectés",
                                     "Veuillez remplir correctement tous les champs avant de poursuivre.")
                break

        if self.client_id["mdp"] != "" and self.client_id["mdp"] != self.client_id["conf_mdp"]:
            messagebox.showwarning("Mots de passe non identiques",
                                   "Les mots de passe que vous saisissez doivent être identiques.")

        elif self.client_id["nom"] != "" and\
            self.client_id["code"] != "" and\
            self.client_id["mdp"] != "" and\
            self.client_id["conf_mdp"] != "" :
            #self.client_id["phone"] != "" :

            messagebox.showinfo("Inscription réussie", f"Bienvenue parmi nous {self.client_id['nom']} !\n\n"
                                "Connectez-vous à présent et chatter sans limite.")

            # If everything is correct, call these functions:
            self.create_data_base()
            self.hide_signin_window()

    def create_data_base(self):
        """Crée la base de données et la charge."""
        # (This is called by another function "registrer")

        connexion = connect("ressources/dluif.db")
        curseur = connexion.cursor()

        db_list = [curseur.lastrowid,
                   self.var_nom.get(),
                   self.var_codename.get(),
                   self.var_mdp.get(),
                   #self.var_number.get(),
                   0000000000,
                   self.port] # Attribut d'instance Server

        curseur.execute("INSERT INTO tt_user_info VALUES(?, ?, ?, ?, ?, ?)", db_list)

        connexion.commit()
        connexion.close()

    # Called on clicked button "Connexion" in the log in window
    def connect_myself(self, *event):
        """Vérifie si le nom d'utilisateur et le mot de passe saisis par l'utilisateur sont conformes au contenu de la
        base de données, et si c'est le cas, appelle les fonctions nécessaires.
        Si la base de données ne contient aucune information, il est demandé à l'utilisateur de créer un compte."""

        index = 1
        index = str(index)
        nom_d_utilisateur = self.var_log_nom.get()
        mot_de_passe = self.var_log_mdp.get()

        try:
            connexion = connect("ressources/dluif.db")

            # Request username cursor
            curseur_usrn = connexion.cursor()
            curseur_usrn.execute("SELECT * FROM tt_user_info WHERE user_id = ?", index)
            requette_username = curseur_usrn.fetchone()[1]

            # Request usercode cursor
            curseur_usrc = connexion.cursor()
            curseur_usrc.execute("SELECT * FROM tt_user_info WHERE user_id = ?", index)
            requette_usrc = curseur_usrc.fetchone()[2]
            self.client_id["code"] = requette_usrc

            # Assign prefix
            Client.prefixe = requette_usrc[0]

            # Request password cursor
            curseur_psw = connexion.cursor()
            curseur_psw.execute("SELECT * FROM tt_user_info WHERE user_id = ?", index)
            requette_mdp = curseur_psw.fetchone()[3]

        except :

            messagebox.showerror("Erreur d'identification",
                "Il semble que c'est votre première utilisation de AR Intercom.\n\n"
                "Veillez commencer par créer un compte. Cela  vous prendra moins de 90 secondes.")

            self.log_username.delete(0, END)
            self.log_password.delete(0, END)
            connexion.close()

        else:
            if nom_d_utilisateur != requette_username:
                # Change Entry color to show error
                self.log_username.config(bg="#FDCBCD", relief=SOLID)

            elif mot_de_passe != requette_mdp:
                # Change Entry color to show error
                self.log_password.config(bg="#FDCBCD", relief=SOLID)

            else:
                # Close data base connexion
                connexion.close()

                # Create and Connect server (Attributes from 'Server')
                self.create_server()
                self.create_socket_server()
                thread = threading.Thread(target=self.launch_server)
                thread.start()

                # Hide log in window and show chat window
                self.central_login.pack_forget()
                self.container()
                self.show_left_side()
                self.show_right_side()

    # Called on KeyPressed-any in an entry field of log in window after an occured error
    def reset_psw_entry(self, event):
        self.log_password.config(bg="#fff", bd=2, relief=GROOVE)

    def reset_usrn_entry(self, event):
        self.log_username.config(bg="#fff", bd=2, relief=GROOVE)

    # Called by another function, "connect_myself".
    def show_left_side(self):
        """Affiche la liste des contacts à gauche."""
        self.frame_with_quick_menu()
        self.frame_with_chat_list()

    # Called by another function, "connect_myself".
    def show_right_side(self):
        """Affiche et les conversations avec contact sélectionné à gauche, et le champ de saisie d'un nouveau message"""
        self.frame_with_chat()
        self.frame_entry_zone()

    # Called on any clicked name in the contact list
    def ask_connection(self, event):
        """Indique le nom cliqué sur le label frame à droite,
        pour permettre à l'utilisateur de savair à qui il parle. Et demande à se connecter au serveur du nom cliqué."""

        # Get the clicked name
        clef = self.nom_contact.cget('text')
        self.cadre_discussions.config(text=clef)

        # Reset message counter
        self.canevas_msgcounter.itemconfig(self.msg_cc, fill="#FFF", outline="#FFF")
        self.canevas_msgcounter.itemconfig(self.msg_ct, text=0)

        # Create client port
        port = self.dictionnary.get(clef)
        self.client = Client(port)

        # Create client port
        if not self.client.connected:  # If client is not connected
            self.client.create_socket_client()
            self.client.connect_to_server()

            if self.client.connected:   # If client is connected
                # Show green button to mean that connection is on
                self.canevas_onlinetoast.config(bg="#00FF00")
            else:
                self.canevas_onlinetoast.config(bg="#FFF")

    def ask_connection1(self, event):
        """Indique le nom cliqué sur le label frame à droite,
        pour permettre à l'utilisateur de savair à qui il parle. Et demande à se connecter au serveur du nom cliqué."""

        # Get the clicked name
        clef = self.nom_contact1.cget('text')
        self.cadre_discussions.config(text=clef)

        # Reset message counter
        self.canevas_msgcounter1.itemconfig(self.msg_cc1, fill="#FFF", outline="#FFF")
        self.canevas_msgcounter1.itemconfig(self.msg_ct1, text=0)

        # Create client port
        port = self.dictionnary.get(clef)
        self.client = Client(port)

        # Try to connect client to server
        if not self.client.connected:  # If client is not connected
            self.client.create_socket_client()
            self.client.connect_to_server()

            if self.client.connected:  # If client is connected
                # Show green button to mean that connection is on
                self.canevas_onlinetoast1.config(bg="#00FF00")
            else:
                self.canevas_onlinetoast1.config(bg="#FFF")

    def ask_connection2(self, event):
        # Get the clicket name
        clef = self.nom_contact2.cget('text')
        self.cadre_discussions.config(text=clef)

        # Reset message counter
        self.canevas_msgcounter2.itemconfig(self.msg_cc2, fill="#FFF", outline="#FFF")
        self.canevas_msgcounter2.itemconfig(self.msg_ct2, text=0)

        # Create client port
        port = self.dictionnary.get(clef)
        self.client = Client(port)

        # Try to connect to server
        if not self.client.connected:  # If client is not connected
            self.client.create_socket_client()
            self.client.connect_to_server()

            if self.client.connected:  # If client is connected
                # Show green button to mean that connection is on
                self.canevas_onlinetoast2.config(bg="#00FF00")
            else:
                self.canevas_onlinetoast2.config(bg="#FFF")

    def ask_connection3(self, event):
        # Get the clicked name
        clef = self.nom_contact3.cget('text')
        self.cadre_discussions.config(text=clef)

        # Reset message counter
        self.canevas_msgcounter3.itemconfig(self.msg_cc3, fill="#FFF", outline="#FFF")
        self.canevas_msgcounter3.itemconfig(self.msg_ct3, text=0)

        # Create client port
        port = self.dictionnary.get(clef)
        self.client = Client(port)

        # Try to connect to server
        if not self.client.connected:  # If client is not connected
            self.client.create_socket_client()
            self.client.connect_to_server()

            if self.client.connected:  # If client is connected
                # Show green button to mean that connection is on
                self.canevas_onlinetoast3.config(bg="#00FF00")
            else:
                self.canevas_onlinetoast3.config(bg="#FFF")

    def ask_connection4(self, event) :
        # Get the clicked name
        clef = self.nom_contact4.cget('text')
        self.cadre_discussions.config(text=clef)

        # Reset message counter
        self.canevas_msgcounter4.itemconfig(self.msg_cc4, fill="#FFF", outline="#FFF")
        self.canevas_msgcounter4.itemconfig(self.msg_ct4, text=0)

        # Create client port
        port = self.dictionnary.get(clef)
        self.client = Client(port)

        # Try t connect to server
        if not self.client.connected :  # If client is not connected
            self.client.create_socket_client()
            self.client.connect_to_server()

            if self.client.connected :  # If client is connected
                # Show green button to mean that connection is on
                self.canevas_onlinetoast4.config(bg="#00FF00")
            else:
                self.canevas_onlinetoast4.config(bg="#FFF")

    def layout_msg(self, chaine):
        """Prend en paramètre une chaîne de caractères et la scinde en plisiuers lignes
        selon sa longueur, puis retourne la chaine mise en forme."""
        cassure = chaine.split(" ")
        chaine = ""
        i = 0
        while i < len(cassure):
            mot = " ".join(cassure[i:i + 5])
            i += 5

            chaine += mot
            if len(cassure) > 5 and i < len(cassure):
                chaine += "\n"
        return chaine

    # Called by another function (ask_connection)
    def get_conversation(self, *event):
        """Read the _sach files and show conversation bubbles."""

        fichier = "ressources/" + \
                  self.cadre_discussions.cget("text").lower() + "_sach"

        try:
            self.toile.pack_forget()
            self.scroll.pack_forget()

        except: # If toile was not created
            pass

        finally:
            self.chat_canvas()
            try:
                chat = open(fichier, 'r')
            except FileNotFoundError:
                pass
            else:
                while 1:
                    line = chat.readline()
                    temps = chat.readline()
                    if temps == "":  # If file is all read
                        break

                    elif line[0] == "R":  # If message was 'R' eceived
                        self.last_row = self.increment_row()
                        self.create_left_bubble()
                        self.left_bubble.config(text=self.layout_msg(line[2:-1]))
                        self.left_time.config(text=temps)

                    elif line[0] == "S":    # If message was 'S' ent
                        self.derniere_ligne = self.increment_row()
                        self.create_right_bubble()
                        self.right_bubble.config(text=self.layout_msg(line[2:-1]))
                        self.right_time.config(text=temps)

                chat.close()

# ========================================== SEND MESSAGE FUNCTIONS ====================================================

    def send_msg_bubble(self, *event):
        """ Fonction qui crée la bulle de message envoyé et la place à la dernère position
        dans la liste de messages envoyés et reçus. """

        if self.cadre_discussions.cget("text") == "":
            # Show warning
            messagebox.showerror("Destinataire non défini",
                                 "Veuillez spécifiez d'abord votre destinataire!")

        else:
            self.temps = self.get_time()  # To get the time message was sent
            self.derniere_ligne = self.increment_row()  # To get the last row where we'll grid the bubble
            message = self.message_saisi.get()

            # Putt messages into bubble
            self.create_right_bubble()
            self.right_bubble.config(text=self.layout_msg(message))
            self.right_time.config(text=self.temps)

            # Send message
            self.client.send_message(message)

            # Empty the entry field once the message is sent
            self.message_saisi.set("")

            # Save message in a text file
            self.save_msg("S:", message, self.temps)

    def receive_msg_bubble(self):
        """ Ajoute un message reçu dans le canvas de l'expeditaire."""

        self.time = self.get_time()  # To get the time message was sent
        self.last_row = self.increment_row()  # To get the last row where we'll grid the bubble

        # Create bubble
        self.create_left_bubble()
        self.left_bubble.config(text=self.layout_msg(self.msg_recu[1:]))
        self.left_time.config(text=self.time)

        # Save message in a text file
        self.save_msg("R:", self.msg_recu[1:], self.time)

    def save_msg(self, prefixe, message, time):
        """Enregistre le message dans un fichier texte."""
        fichier = "ressources/" +\
                  self.cadre_discussions.cget("text").lower() + "_sach"

        chat = open(fichier, "a")
        chat.write(prefixe + message + "\n" + time + "\n")
        chat.close()

# ----------------------------------------------------------------------------------------------------------------------
    def get_time(self):
        """Retoourne le temps où le message a été envoyé pu reçu."""
        temps = time.strftime("%H:%M  %d-%m-%Y")
        return temps

    def increment_row(self):
        """Retourne la dernière ligne du canvas de conversation pour y placer la bulle d'un message envoyé ou reçu."""
        Callbacks.last_row += 1
        return Callbacks.last_row

# =================================================== SERVER ===========================================================

# Create server and let it listen for connections - command function
# called by another function "connect_myself" in the log in window

    def create_server(self):
        """Créer une instance de la classe Server, lui donne le nom de code,
        et lui établi le port de connexion correspondant."""

        global serveur

        codeUtilisateur = self.client_id["code"]

        self.set_usercode(codeUtilisateur)
        self.set_port()

# =============================================== CLIENT ===============================================================
    def msg_counter(self, sender):
        # Show notification
        for i, element in enumerate(self.liste):
            if sender == element:
                if i == 0:
                    nombre_msg = self.canevas_msgcounter.itemcget(self.msg_ct, "text")
                    nombre_msg = int(nombre_msg)

                    self.canevas_msgcounter.itemconfig(self.msg_cc, fill="#E88522", outline="#E88522")
                    self.canevas_msgcounter.itemconfig(self.msg_ct, text=nombre_msg + 1)

                elif i == 1:
                    nombre_msg = self.canevas_msgcounter1.itemcget(self.msg_ct1, "text")
                    nombre_msg = int(nombre_msg)

                    self.canevas_msgcounter1.itemconfig(self.msg_cc1, fill="#E88522", outline="#E88522")
                    self.canevas_msgcounter1.itemconfig(self.msg_ct1, text=nombre_msg + 1)

                elif i == 2:
                    nombre_msg = self.canevas_msgcounter2.itemcget(self.msg_ct2, "text")
                    nombre_msg = int(nombre_msg)

                    self.canevas_msgcounter2.itemconfig(self.msg_cc2, fill="#E88522", outline="#E88522")
                    self.canevas_msgcounter2.itemconfig(self.msg_ct2, text=nombre_msg + 1)

                elif i == 3:
                    nombre_msg = self.canevas_msgcounter3.itemcget(self.msg_ct3, "text")
                    nombre_msg = int(nombre_msg)

                    self.canevas_msgcounter3.itemconfig(self.msg_cc3, fill="#E88522", outline="#E88522")
                    self.canevas_msgcounter3.itemconfig(self.msg_ct3, text=nombre_msg + 1)

                elif i == 4:
                    nombre_msg = self.canevas_msgcounter4.itemcget(self.msg_ct4, "text")
                    nombre_msg = int(nombre_msg)

                    self.canevas_msgcounter4.itemconfig(self.msg_cc4, fill="#E88522", outline="#E88522")
                    self.canevas_msgcounter4.itemconfig(self.msg_ct4, text=nombre_msg + 1)

    def put_inbox(self):
        """ Qand l'utilisateur reçoit un message provenant d'un client avec qui il n'est pas en communication,
        le message est enregistré et une notification lui est montrée."""

        if self.msg_recu[0] == "A":
            # Save message
            ffichier = "ressources/" + "alpha_sach"

            # Show orange notification
            self.msg_counter("Alpha")

            # show popup
            popup("Alpha")

        elif self.msg_recu[0] == "B" :
            ffichier = "ressources/" + "bravo_sach"

            # Show orange notification
            self.msg_counter("Bravo")

            # show popup
            popup("Bravo")

        elif self.msg_recu[0] == "D":
            ffichier = "ressources/" + "delta_sach"

            # Show orange notification
            self.msg_counter("Delta")

            # show popup
            popup("Delta")

        elif self.msg_recu[0] == "E":
            ffichier = "ressources/" + "echo_sach"

            # Show orange notification
            self.msg_counter("Echo")

            # show popup
            popup("Echo")

        elif self.msg_recu[0] == "T":
            ffichier = "ressources/" + "tango_sach"

            # Show orange notification
            self.msg_counter("Tango")

            # show popup
            popup("Tango")

        # Save message in the correct file
        tmps = self.get_time() # Get time

        chat_file = open(ffichier, "a")
        chat_file.write("R:" + self.msg_recu[1:] + "\n" + tmps + "\n")
        chat_file.close()

    def supprimer_msg(self, event):
        current_text = self.cadre_discussions.cget("text")
        if current_text != "":
            fichier = "ressources/" + current_text.lower() + "_sach"
            if messagebox.askyesno("Effacement des discussions",
                                    f"Êtes-vous sûr de vouloir effacer vos conversations avec {current_text} ?"):

                lecture = open(fichier, 'w')
                lecture.close()


# ============================================== SEE COMMAND RESULT ====================================================
# Run the app   -------  Just for trying

if __name__ == "__main__":
    app = Callbacks()

# ===================================================== END ============================================================