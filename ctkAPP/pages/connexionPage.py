import time
import customtkinter as ctk
from controleur.employeControler import *
from controleur.chefControler import *
import re
from .formulaire.erreur.erreur import erreur
ctk.set_default_color_theme("ctkAPP/themes/myBlue.json")  # Thème bleue

class ConnexionPage(ctk.CTkFrame):
    
    patern = r"[a-zA-Z0-9#*@_]+"
    def __init__(self, parent, controller):
        super().__init__(parent)
        controller.title("connexion")
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

        self.userEntree.insert(0, "admin")

        self.mpdEntree = ctk.CTkEntry(self.connexionFrame, placeholder_text="mot de passe", show="*", height=50, width=300)
        self.mpdEntree.grid(row=2, column=0, padx=40, pady=(10, 50))

        self.mpdEntree.insert(0, "1234")


        self.bouttonCommit = ctk.CTkButton(self.connexionFrame,width=150, height=20, text="valider", fg_color="green", text_color="white",command=self.verification)
        self.bouttonCommit.grid(row=3, column=0, pady=(0, 20))



    def verification(self):
        motDePasse = self.mpdEntree.get()
        nom = self.userEntree.get()
        if not re.match(self.patern, nom):
            self.rougir(self.userEntree)

        elif not re.match(self.patern, motDePasse):
            self.rougir(self.mpdEntree)
        else:
            utilisateur = obtenirChefPar(nom, motDePasse)
            
            if utilisateur:
                self.controller.utilisateurCourant=utilisateur
                self.controller.wait_window(erreur(self.controller, "connexion reussie"))
                self.controller.title("dashboard")
                self.controller.pagesChef["dashboard"].miseAjour()
                self.controller.pagesChef["dashboard"].tkraise()
                self.controller.pagesSecondaire["gestions"].tkraise()
                self.controller.pagesPrimaire["contenu"].tkraise()
            else:
                utilisateur = obtenirEmployePar(nom=nom, mdp=motDePasse, connexion=True)
                if utilisateur:
                    self.controller.utilisateurCourant=utilisateur[0]
                    self.controller.wait_window(erreur(self.controller, "connexion reussie"))
                    self.controller.pagesEmploye["clients"].miseAjour()
                    self.controller.pagesEmploye["clients"].tkraise()
                    self.controller.pagesSecondaire["pageEmploye"].tkraise()
                    self.controller.pagesPrimaire["contenu"].tkraise()
                    self.controller.title("client")
                    self.controller.pagesSecondaire["pageEmploye"].tkraise()
                else:
                    self.controller.wait_window(erreur(self.controller, "connexion echouée"))
    
    def rougir(self, widget):
        widget.configure(fg_color = "red")
        self.after(1500, lambda:self.blanchir(widget))

    def blanchir(self, widget):
        widget.configure(fg_color="white")

    def miseAjour(self):
        if self.grid_info():
            self.controller.title("connexion")

    

    

        