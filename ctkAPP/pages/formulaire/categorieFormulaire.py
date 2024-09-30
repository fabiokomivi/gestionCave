import customtkinter as ctk
import tkinter as tk
from .erreur.erreur import erreur
import re
from controleur.categorieControler import *

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class categorieForm(ctk.CTkToplevel):

    nomPattern = r"[a-zA-Z]"

    def __init__(self,controller, callback, dico, mode):
        super().__init__(controller)
        self.geometry("500x400")
        self.callback = callback
        self.mode = mode
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.titre = ctk.CTkLabel(self, text=mode, font=ctk.CTkFont(family="Arial", size=25, weight="bold"))
        self.titre.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.contenu = ctk.CTkFrame(self)
        #for i in range(4):
        #    self.contenu.grid_rowconfigure(i, weight=1)
        self.contenu.grid_columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky="nsew", padx=15, pady=5)

        self.entreeNom = ctk.CTkEntry(self.contenu, placeholder_text="nom", width=200)
        self.entreeDescription = ctk.CTkEntry(self.contenu, placeholder_text="description", width=200, height=100)


        if dico:
            self.entreeNom.insert(0, dico["nom"])
            self.entreeDescription.insert(0, dico["description"])

        self.entreeNom.grid(row=0, column=0, pady=(30, 5))
        self.entreeDescription.grid(row=1, column=0, pady=(5, 5))


        self.confirmationFrame = ctk.CTkFrame(self, height=50)
        self.confirmationFrame.grid(row=2, column=0, sticky="ew", pady=15)

        self.valider = ctk.CTkButton(self.confirmationFrame, text="valider", fg_color="green", command=self.verification)
        self.annuler = ctk.CTkButton(self.confirmationFrame, text="annuler", fg_color="red", command=self.quitter)
        self.valider.pack(side="right", padx=(30, 50), pady=10)
        self.annuler.pack(side="left", padx=(50, 30), pady=10)

        self.wait_visibility()
        self.grab_set()
        #self.grab_set_global()
        #self.mainloop()

    def verification(self):
        nom = self.entreeNom.get()
        description = self.entreeDescription.get()
        telephone = self.entreeTelephone.get()
        addresse = self.entreeAddresse.get()

        if not re.match(self.nomPattern, nom):
            self.rougir(self.entreeNom)
        elif not re.match(self.nomPattern, description):
            self.rougir(self.entreeDescription)
        else:
            if self.mode=="ajout":
                if obtenirCategorieParAttribue(nom=telephone): 
                    self.wait_window(erreur(self, "un client possede deja ce numero"))
                elif obtenirCategorieParAttribue(description==addresse):
                    self.wait_window(erreur(self, "un client possede deja cet addresse"))
                else:
                    self.callback({"nom": nom, "description": description})
                    self.destroy()
            else:
                self.callback({"nom": nom, "description": description})
                self.destroy()

    def rougir(self, widget):
        widget.configure(fg_color = "red")
        self.after(1500, lambda:self.blanchir(widget))

    def blanchir(self, widget):
        widget.configure(fg_color="white")

    def quitter(self):
        #self.controller.controller.deiconify()
        self.destroy()


