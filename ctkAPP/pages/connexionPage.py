import time
import customtkinter as ctk
from controleur.chefControler import *
from controleur.employeControler import *
import re
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class ConnexionPage(ctk.CTkFrame):
    patern = r"[a-zA-Z0-9#*@_]+"
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.connexionFrame = ctk.CTkFrame(self, height=500, width=500)
        self.connexionFrame.grid_propagate(False)
        self.connexionFrame.grid(row=0, column=0, pady=100)

        for i in range(3):
            self.connexionFrame.grid_rowconfigure(i, weight=1)
        self.connexionFrame.grid_columnconfigure(0, weight=1)
        

        ctk.CTkLabel(self.connexionFrame, text="connexion", height=100, width=150, font=ctk.CTkFont(family="Arial", size=35, weight="bold")).grid(row=0, column=0, padx=20, sticky="ew")
        

        self.userEntree = ctk.CTkEntry(self.connexionFrame, placeholder_text="utilisateur", height=50, width=300)
        self.userEntree.grid(row=1, column=0, padx=40, pady=(50, 10))

        self.userEntree.insert(0, "amouzou")

        self.mpdEntree = ctk.CTkEntry(self.connexionFrame, placeholder_text="mot de passe", show="*", height=50, width=300)
        self.mpdEntree.grid(row=2, column=0, padx=40, pady=(10, 50))

        self.mpdEntree.insert(0, "fabio2002")


        self.bouttonCommit = ctk.CTkButton(self.connexionFrame,width=150, height=20, text="valider", fg_color="green", text_color="white",command=self.verification)
        self.bouttonCommit.grid(row=3, column=0, pady=(0, 20))

        self.labelInfo = ctk.CTkLabel(self.connexionFrame, text="", height=100, width=30, font=ctk.CTkFont(family="Arial", size=15, weight="bold"))
        self.labelInfo.grid(row=4, column=0, padx=20, sticky="ew")

    def verification(self):
        motDePasse = self.mpdEntree.get()
        nom = self.userEntree.get()
        if not re.match(self.patern, nom):
            self.labelInfo.configure(text="!! le nom ne doit pas etre vide !!")
            self.rougir(self.userEntree)

        elif not re.match(self.patern, motDePasse):
            self.labelInfo.configure(text="!! le mot de passe ne doit pas etre vide !!")
            self.rougir(self.mpdEntree)
        else:
            utilisateur = obtenirChefPar(nom, motDePasse)
            self.controller.utilisateurCourant=utilisateur
            self.controller.pagesSecondaire["gestions"].tkraise()
            if not utilisateur:
                utilisateur = obtenirEmployePar(nom=nom, mdp=motDePasse)
                self.controller.utilisateurCourant=utilisateur
                self.controller.pagesSecondaire["pageEmploye"].tkraise()
            if utilisateur:
                self.labelInfo.configure(text="!! connexion reussie !!")
                self.controller.chargerBoutonMenu()
                time.sleep(1)
                self.controller.utilisateurCourant = utilisateur
                self.controller.changePage("contenu")
            else:
                self.labelInfo.configure(text="!! utilisateur n'existe pas !!")

    def rougir(self, widget):
        widget.configure(fg_color = "red")
        self.after(1500, lambda:self.blanchir(widget))

    def blanchir(self, widget):
        widget.configure(fg_color="white")

        