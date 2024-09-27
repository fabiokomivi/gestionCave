import customtkinter as ctk
from controleur.chefControler import *
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class ConnexionPage(ctk.CTkFrame):
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
        self.userEntree.grid(row=1, column=0, padx=40, pady=(50, 0))

        self.mpdEntree = ctk.CTkEntry(self.connexionFrame, placeholder_text="mot de passe", height=50, width=300)
        self.mpdEntree.grid(row=2, column=0, padx=40, pady=(0, 50))


        self.bouttonCommit = ctk.CTkButton(self.connexionFrame,width=150, height=20, text="valider", fg_color="green", text_color="white",command=self.verification)
        self.bouttonCommit.grid(row=3, column=0, pady=(0, 20))

    def verification(self):
        chefs = obtenirChefs()
        print(chefs)
        password = self.mpdEntree.get()
        username = self.userEntree.get()
        self.controller.changePage("contenu")

        