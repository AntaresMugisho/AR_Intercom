# -*- This python file uses the following encoding : coding:utf-8 -*-

# =========================================== GRAPHIC USER DESIGNED WITH TKINTER =======================================

# Importing tkinter and tix modules

from tkinter import *
from tkinter import tix
import os

# ---------------------------------------------------- MAIN CLASS ------------------------------------------------------

class UserInteface :
    """
    Interface graphique du logiciel. La fenêtre est verticalement scindée en deux parties principales:
    - La partie gauche affiche la liste des contacts, celle de droite affiche les discussions avec le contact cliqué
    dans la partie gauche.
    """

    def __init__(self):

        self.window = tix.Tk()
        self.window.iconbitmap("ressources/ARsoftlogo.ico")
        self.window.title("AR Intercom")
        self.window.geometry("480x300+480+240")
        self.window.minsize(480, 300)
        self.window.resizable(False, True)
        self.window.config(background="#fff")

        # An empty dictionnary / will contain the client info
        self.client_id = {}

        # A dictionnary containing ports of servers. and  creating chatlist
        self.dictionnary = {"Alpha": 12100, "Bravo": 12200, "Delta": 12400, "Echo": 12500, "Tango": 12210}
        self.liste = ["Alpha", "Bravo", "Delta", "Echo", "Tango"]

        # Initializing
        self.create_menubar()
        self.login_window()
        self.window.mainloop()

# 0 ============================================ GRAPHIC USER - MUNU BAR ===============================================
    def create_menubar(self):
        """Créer un menu dans la fenêtre."""
        barre_menu = Menu(self.window, tearoff=0)

        # Create menu 'Menu'
        menu_menu = Menu(barre_menu, background='#FFF', activebackground="#2b85c7")
        # Add submenus
        menu_menu.add_command(label="Aide", command=lambda: os.startfile("ressources\Help.pdf"))
        menu_menu.add_separator()
        menu_menu.add_command(label="Quitter", command=self.quitter)

        barre_menu.add_cascade(label="Menu", menu=menu_menu)
        self.window.config(menu=barre_menu)

# 1 =========================================== GRAPHIC USER - CHAT WINDOW =============================================

    def container(self):
        """
        Ceci est la fonction principale qui sera appelée à chaque fois que l'utilisateur aura besoin d'afficher
        la liste de ses contacts, ainsi que leurs conversations respectives.
        """
        global conteneur, left_side, right_side

        conteneur = PanedWindow(self.window, handlesize=4, handlepad=10, showhandle=True, sashrelief="sunken")

        left_side = Frame(conteneur)
        right_side = Frame(conteneur)

        conteneur.add(left_side)
        conteneur.add(right_side)
        conteneur.pack(fill=BOTH, expand=TRUE)

# _______________________________________________ LEFT SIDE ____________________________________________________________

    def frame_with_quick_menu(self):
        """ Défini le titre 'Chat canvas' dans un cadre."""
        cadre_menus = Frame(left_side, relief="sunken", bg="#fff")
        cadre_menus.pack(pady=10)

        # Creating quick menus
        titre = Label(cadre_menus, text="Chat list", font=("Verdana", 11), fg="#FFF", bg="#2b85c7")
        titre.pack(ipadx=12)

    def frame_with_chat_list(self):
        """Etabli la liste de clients à partir de 'liste', un attribut d'objet de 'UserInterface'.
        Pour ce faire la fonction 'create_list est appelée."""
        global liste_contacts
        liste_contacts = Canvas(left_side) # Writing list into a canvas to enable scroll one day
        liste_contacts.pack()

        if self.client_id["code"] in self.liste:
            self.liste.remove(self.client_id["code"])

        for self.index, nom in enumerate(self.liste):
            self.create_list(nom)

# ----------------------------------------------------------------------------------------------------------------------

    def create_list(self, parametre):
        """Fonction créant la liste des clients. parametre étant le paramètre nom du client."""
        # Frame which contains all information about contacts
        cadre_infos = Frame(liste_contacts, bg="#FFF", bd=1, relief="solid")
        cadre_infos.pack(pady=2, fill=X)

        if self.index == 0:
            # 1. Profile picture
            profile_client = PhotoImage(file="ressources/1.png").zoom(10).subsample(8)
            canevas_photo_client = Canvas(cadre_infos, width=30, height=30, cursor="hand2")
            canevas_photo_client.create_image(15, 15, image=profile_client)
            canevas_photo_client.pack(side=LEFT)

            # 2. Online toast
            self.canevas_onlinetoast = Canvas(cadre_infos, bg="#FFF", width=8, height=8)
            self.canevas_onlinetoast.pack(side=LEFT, anchor=NE)

            # 3. Contact user_code
            self.nom_contact = Label(cadre_infos, bg="#FFF", text=parametre, font=("Calibri", 12))
            self.nom_contact.pack(side=LEFT)
            self.nom_contact.bind("<ButtonPress-1>", self.ask_connection)
            self.nom_contact.bind("<ButtonRelease-1>", self.get_conversation)

            # 4. Unread message counter
            self.canevas_msgcounter = Canvas(cadre_infos, bg="#FFF", width=30, height=30)
            self.canevas_msgcounter.pack(anchor=E)
            self.msg_cc = self.canevas_msgcounter.create_oval(8, 25, 25, 8, fill="#FFF", outline="#FFF")
            self.msg_ct = self.canevas_msgcounter.create_text((16, 16), text=0, fill="#FFF", font=("Calibri", 10))


        elif self.index == 1:
            # 1. Profile picture
            profile_client = PhotoImage(file="ressources/1.png").zoom(10).subsample(8)
            canevas_photo_client = Canvas(cadre_infos, width=30, height=30)
            canevas_photo_client.create_image(15, 15, image=profile_client)
            canevas_photo_client.pack(side=LEFT)

            # 2. Online toast
            self.canevas_onlinetoast1 = Canvas(cadre_infos, bg="#FFF", width=8, height=8)
            self.canevas_onlinetoast1.pack(side=LEFT, anchor=NE)

            # 3. Contact user_code
            self.nom_contact1 = Label(cadre_infos, bg="#FFF", text=parametre, font=("Calibri", 12))
            self.nom_contact1.pack(side=LEFT)
            self.nom_contact1.bind("<ButtonPress-1>", self.ask_connection1)
            self.nom_contact1.bind("<ButtonRelease-1>", self.get_conversation)

            # 4. Unread message counter
            self.canevas_msgcounter1 = Canvas(cadre_infos, bg="#fff", width=30, height=30)
            self.canevas_msgcounter1.pack(anchor=E)
            self.msg_cc1 = self.canevas_msgcounter1.create_oval(8, 25, 25, 8, fill="#FFF", outline="#FFF")
            self.msg_ct1 = self.canevas_msgcounter1.create_text((16, 16), text=0, fill="#FFF", font=("Calibri", 10))


        elif self.index == 2 :
            # 1. Profile picture
            profile_client = PhotoImage(file="ressources/1.png").zoom(10).subsample(8)
            canevas_photo_client = Canvas(cadre_infos, width=30, height=30)
            canevas_photo_client.create_image(15, 15, image=profile_client)
            canevas_photo_client.pack(side=LEFT)

            # 2. Online toast
            self.canevas_onlinetoast2 = Canvas(cadre_infos, bg="#FFF", width=8, height=8)
            self.canevas_onlinetoast2.pack(side=LEFT, anchor=NE)

            # 3. Contact user_code
            self.nom_contact2 = Label(cadre_infos, bg="#FFF", text=parametre, font=("Calibri", 12))
            self.nom_contact2.pack(side=LEFT)
            self.nom_contact2.bind("<ButtonPress-1>", self.ask_connection2)
            self.nom_contact2.bind("<ButtonRelease-1>", self.get_conversation)

            # 4. Unread message counter
            self.canevas_msgcounter2 = Canvas(cadre_infos, bg="#fff", width=30, height=30)
            self.canevas_msgcounter2.pack(anchor=E)
            self.msg_cc2 = self.canevas_msgcounter2.create_oval(8, 25, 25, 8, fill="#FFF", outline="#FFF")
            self.msg_ct2 = self.canevas_msgcounter2.create_text((16, 16), text=0, fill="#FFF", font=("Calibri", 10))


        elif self.index == 3 :

            # 1. Profile picture
            profile_client = PhotoImage(file="ressources/1.png").zoom(10).subsample(8)
            canevas_photo_client = Canvas(cadre_infos, width=30, height=30)
            canevas_photo_client.create_image(15, 15, image=profile_client)
            canevas_photo_client.pack(side=LEFT)

            # 2. Online toast
            self.canevas_onlinetoast3 = Canvas(cadre_infos, bg="#FFF", width=8, height=8)
            self.canevas_onlinetoast3.pack(side=LEFT, anchor=NE)

            # 3. Contact user_code
            self.nom_contact3 = Label(cadre_infos, bg="#FFF", text=parametre, font=("Calibri", 12))
            self.nom_contact3.pack(side=LEFT)
            self.nom_contact3.bind("<ButtonPress-1>", self.ask_connection3)
            self.nom_contact3.bind("<ButtonRelease-1>", self.get_conversation)

            # 4. Unread message counter
            self.canevas_msgcounter3 = Canvas(cadre_infos, bg="#fff", width=30, height=30)
            self.canevas_msgcounter3.pack(anchor=E)
            self.msg_cc3 = self.canevas_msgcounter3.create_oval(8, 25, 25, 8, fill="#FFF", outline="#FFF")
            self.msg_ct3 = self.canevas_msgcounter3.create_text((16, 16), text=0, fill="#FFF", font=("Calibri", 10))


        elif self.index == 4 :
            # 1. Profile picture
            profile_client = PhotoImage(file="ressources/1.png").zoom(10).subsample(8)
            canevas_photo_client = Canvas(cadre_infos, width=30, height=30)
            canevas_photo_client.create_image(15, 15, image=profile_client)
            canevas_photo_client.pack(side=LEFT)

            # 2. Online toast
            self.canevas_onlinetoast4 = Canvas(cadre_infos, bg="#FFF", width=8, height=8)
            self.canevas_onlinetoast4.pack(side=LEFT, anchor=NE)

            # 3. Contact user_code
            self.nom_contact4 = Label(cadre_infos, bg="#FFF", text=parametre, font=("Calibri", 12))
            self.nom_contact4.pack(side=LEFT)
            self.nom_contact4.bind("<ButtonPress-1>", self.ask_connection4)
            self.nom_contact4.bind("<ButtonRelease-1>", self.get_conversation)

            # 4. Unread message counter
            self.canevas_msgcounter4 = Canvas(cadre_infos, bg="#fff", width=30, height=30)
            self.canevas_msgcounter4.pack(anchor=E)
            self.msg_cc4 = self.canevas_msgcounter4.create_oval(8, 25, 25, 8, fill="#FFF", outline="#FFF")
            self.msg_ct4 = self.canevas_msgcounter4.create_text((16, 16), text=0, fill="#FFF", font=("Calibri", 10))

# _______________________________________________ RIGHT SIDE ___________________________________________________________

    def frame_with_chat(self):
        """Créer un labelframe au côté droit et fait appel à la fonction 'chat_canvas'."""
        self.cadre_discussions = LabelFrame(right_side, bg="#FFF", text="", width=50, height=50)
        self.cadre_discussions.pack(fill=BOTH, expand=YES)
        self.cadre_discussions.bind("<Alt-ButtonPress-1>", self.supprimer_msg)

    def chat_canvas(self):
        """Crée le canvas (avec une scrollbar) qui contiendra les discussions."""
        # Create canvas
        self.toile = Canvas(self.cadre_discussions, bg="#FFF", width=50, height=50)
        self.toile.pack(expand=YES,  side=LEFT, fill=BOTH)

        # Create and add a frame to canvas as window
        self.frame_toile = Frame(self.toile, bg="#FFF")
        self.toile.create_window((0, 0), window=self.frame_toile, anchor=NW)

        # White space
        self.date_msg = Label(self.frame_toile, bg="#FFF", width=46, height=0)
        self.date_msg.grid(row=0, columnspan=2, sticky=EW)

        # Create scrollbar
        self.create_scroll()

    def create_scroll(self):
        """Crée la barre de défilement dans la liste la toile."""
        self.scroll = Scrollbar(self.cadre_discussions, orient=VERTICAL, command=self.toile.yview)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.toile.config(yscrollcommand=self.scroll.set)
        self.toile.bind('<Configure>', lambda event: self.toile.configure(scrollregion=self.toile.bbox(ALL)))

    def frame_entry_zone(self):
        """Affiche la zone de saisie d'un nouveau message et le bouton d'envoie."""
        # Frame with the entry widget and send button
        zone_texte = Frame(right_side, bg="#EBEBEB", relief=SOLID)
        zone_texte.pack(side=BOTTOM, fill=X)

        self.message_saisi = StringVar()  # In the chat window
        ligne_texte = Entry(zone_texte, textvariable=self.message_saisi, width=30, relief=RAISED)
        ligne_texte.grid(column=0, ipady=3, pady=6, padx=6)

        # Bouton d'envoie
        send_button = Button(zone_texte, text="Envoyer", font=("Calibri", 11), fg="#FFF", bg="#2b85c7",
            command=self.send_msg_bubble)
        send_button.grid(column=1, row=0, sticky=E, padx=40)
        send_button.bind("<Return>", self.send_msg_bubble)

    def create_right_bubble(self):
        """Créer la bulle d'un message envoyé et l'empacte."""
        # Creating a frame that will pack two labels: one with the sent message, the other with the hour
        frame_msg_droit = Frame(self.frame_toile, bg="white")
        frame_msg_droit.grid(row=self.derniere_ligne, pady=2, sticky=E)

        # Two labels : sent message and time
        self.right_bubble = Label(frame_msg_droit, bg="#3399cc", font=("Verdana", 10), fg="white")
        self.right_bubble.pack(ipadx=3)

        self.right_time = Label(frame_msg_droit, bg="white", text="", font=("Verdana", 6))
        self.right_time.pack(expand=YES)

    def create_left_bubble(self):
        """Créer la bulle d'un message reçu et l'empacte."""
        # Creating a frame that will pack two labels: one with the sent message, the other with the hour
        frame_msg_gauche = Frame(self.frame_toile, bg="white")
        frame_msg_gauche.grid(row=self.last_row,pady=2, sticky=W)

        # Two labels : received message and time
        self.left_bubble = Label(frame_msg_gauche, bg="#e88522", fg="#FFF", font=("Verdana", 10))
        self.left_bubble.pack(ipadx=3)

        self.left_time = Label(frame_msg_gauche, bg="white", text="", font=("Verdana", 6), fg="#333333")
        self.left_time.pack(expand=YES)

# 2 ----------------------------------------- GRAPHIC USER - LOG IN WINDOW ---------------------------------------------

    def login_window(self):
        """Conçois l'interface de connexion (Login window)."""
        # Parent frame
        self.central_login = Frame(self.window)
        self.central_login.pack(expand=YES, fill=BOTH)

        # Label frame containning title of window
        cadre_login = LabelFrame(self.central_login, text="Log in")
        cadre_login.pack(expand=YES, pady=15, padx=15, ipady=10, ipadx=10)

        nom_utilisateur = Label(cadre_login, text="Nom d'utilisateur").grid(row=0, column=0, sticky=E)
        self.var_log_nom = StringVar()
        self.log_username = Entry(cadre_login, textvariable=self.var_log_nom, bg="#fff", bd=2, relief=GROOVE)
        self.log_username.grid(row=0, column=1, sticky=W, pady=5, padx=5)
        self.log_username.focus()
        self.log_username.bind("<KeyPress>", self.reset_usrn_entry)

        mot_de_passe = Label(cadre_login, text="Mot de passe : ").grid(row=1, column=0, sticky=E)
        self.var_log_mdp = StringVar()
        self.log_password = Entry(cadre_login, textvariable=self.var_log_mdp, bg="#fff", bd=2, relief=GROOVE, show="●")
        self.log_password.grid(row=1, column=1, sticky=W, pady=5, padx=5)
        self.log_password.bind("<KeyPress>", self.reset_psw_entry)

        toogle = Button(cadre_login, height=0, relief=SOLID, borderwidth=0, bg="#FFF", activebackground="#276EBA",
            command=lambda: self.log_password.config(show="●"))
        toogle.grid(row=1, column=2)
        toogle.bind("<ButtonPress-1>", lambda *event: self.log_password.config(show=""))


        bouton_connexion = Button(self.central_login, text="Connexion", font=("arial", 12), bg="#276EBA", fg="#FFF",
            command=self.connect_myself)
        bouton_connexion.pack(expand=YES, pady=12)
        bouton_connexion.bind("<Return>", self.connect_myself)

        # Create account field
        cadre_bas = Frame(self.central_login, bg="#F4A682", height=1)
        creer_compte = Label(cadre_bas, text="Créer un compte.", font=("calibri", 9, UNDERLINE), bg="#F4A682",
                         fg="blue", cursor="hand2", activebackground="#F4A682", activeforeground="#FFF", relief="flat")
        creer_compte.pack(side=RIGHT)
        creer_compte.bind("<ButtonPress-1>", self.signin)

        label_inscription = Label(cadre_bas, bg="#F4A682", text="Pas encore inscrit ?", font=("calibri", 9), width=20)
        label_inscription.pack(side=RIGHT)

        cadre_bas.pack(pady=12, fill=BOTH)


# 2 ----------------------------------------- GRAPHIC USER - LOG IN WINDOW ---------------------------------------------

    def signin_window(self):
        """Conçois l'interface d'enregistrement."""
        self.central_signin = Frame(self.window, bg="#FFF")
        self.central_signin.pack(expand=YES, fill=BOTH)

        # Creating  back button (to go back on the login window)
        bouton_retour = Canvas(self.central_signin, width=25, height=20, bg="#FFF", bd=0)
        bouton_retour.create_line(0, 12, 20, 12, arrow="first", fill="#276EBA")
        bouton_retour.pack(anchor=NW, pady=10, padx=10)
        bouton_retour.bind("<ButtonPress-1>", self.hide_signin_window)

        # Creating sign in formulary
        cadre_signin = LabelFrame(self.central_signin, bg="#FFF", text="Sign in", font=("Calibri", 12))
        cadre_signin.pack(pady=12)

        nom_utilisateur = Label(cadre_signin, bg="#FFF", text="Nom d'utilisateur :").grid(row=0, column=0, sticky=E)
        self.var_nom = StringVar()
        username = Entry(cadre_signin, width=25, textvariable=self.var_nom, relief=RAISED)
        username.grid(row=0, column=1, sticky=W, pady=5, padx=5)
        username.focus()

        nom_de_code = Label(cadre_signin, bg="#FFF", text="Nom de code : ").grid(row=1, column=0, sticky=E)
        self.var_codename = StringVar()
        code_name = tix.ComboBox(cadre_signin, bg="white", variable=self.var_codename, relief="flat",
        options='listbox.height 6 background white relief flat')

        for element in self.dictionnary.keys():
            code_name.insert(END, element)
        code_name.grid(row=1, column=1, sticky=W, pady=5, padx=5)

        mot_de_passe = Label(cadre_signin, bg="#FFF", text="Mot de passe : ").grid(row=2, column=0, sticky=E)
        self.var_mdp = StringVar()
        password = Entry(cadre_signin, width=25, textvariable=self.var_mdp, relief=RAISED)
        password.grid(row=2, column=1, sticky=W, pady=5, padx=5)

        confirmation_mdp = Label(cadre_signin, bg="#FFF", text="Confirmer mot de passe : ").grid(row=3, column=0, sticky=E)
        self.var_conf_mdp = StringVar()
        confirm_password = Entry(cadre_signin, width=25, textvariable=self.var_conf_mdp, relief=RAISED)
        confirm_password.grid(row=3, column=1, sticky=W, pady=5, padx=5)

        # This is not important now but it can be a feature of next version.
        #numuro_telephone = Label(cadre_signin, text="Numéro de téléphone : ").grid(row=4, column=0, sticky=E)
        #self.var_number = StringVar()
        #phone_number = Entry(cadre_signin, width=25, textvariable=self.var_number)
        #phone_number.grid(row=4, column=1, sticky=W, pady=5, padx=5)

        rappel_cgu = Label(self.central_signin, bg="#FFF", text="En cliquant sur \"Valider\", vous acceptez",font=("Calibri", 9))
        lien_cgu = Label(self.central_signin, bg="#FFF", fg="blue", cursor="hand2",
            text="les conditions générales d'utilisation de AR Intercom.", font=("Calibri", 9, UNDERLINE))
        rappel_cgu.pack()
        lien_cgu.pack()
        lien_cgu.bind("<ButtonPress-1>", lambda event: os.startfile("ressources\CGU_ARIntercom.pdf"))

        bouton_valider = Button(self.central_signin, text="Valider", bg="green", fg="#FFF", width=8, height=1,
                                                     font=("Calibri", 12), command=self.registrer)
        bouton_valider.pack(expand=YES, pady=6)

# ================================================= COMMAND FUNCTIONS ==================================================
# To prevent errors if this module is run by here

    def signin(self, *event):
        # Called on clicked "Créer un compte" in the login window
        pass

    def hide_signin_window(self, *event):
        # Called on clicked button "Créer un compte" in the log in window
        # Also called as event funtion on clicked "Left arrow" in the sign in window
        pass

    def registrer(self):
        # Called on clicked button "Valider" in the sign in window
        pass

    def create_data_base(self) :
        # (This is called by another function "registrer")
        pass

    def connect_myself(self, *event):
        # Called on clicked button "Connexion" in the log in window
        pass

    def reset_psw_entry(self, event):
        # Called on KeyPressed-any in an entry field of log in window after an occured error
        pass

    def reset_usrn_entry(self, event):
        # Called on KeyPressed-any in an entry field of log in window after an occured error
        pass

    def show_left_side(self):
        # Called by another function, "connect_myself".
        pass

    def show_right_side(self):
        # Called by another function, "connect_myself".
        pass

    def get_conversation(self, *event):
        pass

    def receive_msg_bubble(self):
        pass

    def quitter(self):
        pass
# ============================================== SEE DESIGN RESULT =====================================================
# Run the app   -------  Just for trying
if __name__ == "__main__":
    app = UserInteface()

# ===================================================== END ============================================================