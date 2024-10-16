import time
import customtkinter as ctk
import tkinter as tk
from .erreur.erreur import erreur
import re
from controleur.chefControler import creerChef


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class PremiereConnexion(ctk.CTkToplevel):
    emailPattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    numeroPattern = r"[0-9]{8}"
    nomPattern = r"[a-zA-Z]"

    def __init__(self, parent, callback):
        super().__init__(parent)
        self.geometry("500x400")
        self.protocol("WM_DELETE_WINDOW", self.fermetureAnormale)
        self.callback = callback
 
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.titre = ctk.CTkLabel(self, text="mode", font=ctk.CTkFont(family="Arial", size=25, weight="bold"))
        self.titre.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.contenu = ctk.CTkFrame(self)
        #for i in range(4):
        #    self.contenu.grid_rowconfigure(i, weight=1)
        self.contenu.grid_columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky="nsew", padx=15, pady=5)

        self.entreeNom = ctk.CTkEntry(self.contenu, placeholder_text="nom", width=200)
        self.entreePrenom = ctk.CTkEntry(self.contenu, placeholder_text="prenom", width=200)
        self.entreeTelephone = ctk.CTkEntry(self.contenu, placeholder_text="telephone", width=200)
        self.entreeAddresse = ctk.CTkEntry(self.contenu, placeholder_text="addresse", width=200)

        self.entreeNom.grid(row=0, column=0, pady=(30, 5))
        self.entreePrenom.grid(row=1, column=0, pady=(5, 5))
        self.entreeTelephone.grid(row=2, column=0, pady=(5, 5))
        self.entreeAddresse.grid(row=3, column=0, pady=(5, 30))

        self.confirmationFrame = ctk.CTkFrame(self, height=50)
        self.confirmationFrame.grid(row=2, column=0, sticky="ew", pady=15)

        self.valider = ctk.CTkButton(self.confirmationFrame, text="valider", fg_color="green")
        self.annuler = ctk.CTkButton(self.confirmationFrame, text="annuler", fg_color="red")
        self.valider.pack(side="right", padx=(30, 50), pady=10)
        self.annuler.pack(side="left", padx=(50, 30), pady=10)

        self.wait_visibility()
        self.grab_set()
        #self.grab_set_global()
        #self.mainloop()

    def fermetureAnormale(self):
        self.destroy()
