import time
import customtkinter as ctk
import tkinter as tk
from .erreur.erreur import erreur
import re
from controleur.clientControler import obtenirClientparAttribue


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class ClientForm(ctk.CTkToplevel):
    emailPattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    numeroPattern = r"[0-9]{8}"
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
        self.entreePrenom = ctk.CTkEntry(self.contenu, placeholder_text="prenom", width=200)
        self.entreeTelephone = ctk.CTkEntry(self.contenu, placeholder_text="telephone", width=200)
        self.entreeAddresse = ctk.CTkEntry(self.contenu, placeholder_text="addresse", width=200)

        if dico:
            self.entreeNom.insert(0, dico["nom"])
            self.entreePrenom.insert(0, dico["prenom"])
            self.entreeTelephone.insert(0, dico["telephone"])
            self.entreeAddresse.insert(0, dico["addresse"])

        self.entreeNom.grid(row=0, column=0, pady=(30, 5))
        self.entreePrenom.grid(row=1, column=0, pady=(5, 5))
        self.entreeTelephone.grid(row=2, column=0, pady=(5, 5))
        self.entreeAddresse.grid(row=3, column=0, pady=(5, 30))

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
        prenom = self.entreePrenom.get()
        telephone = self.entreeTelephone.get()
        addresse = self.entreeAddresse.get()

        if not re.match(self.nomPattern, nom):
            self.rougir(self.entreeNom)
        elif not re.match(self.nomPattern, prenom):
            self.rougir(self.entreePrenom)
        elif not re.match(self.numeroPattern, telephone):
            self.rougir(self.entreeTelephone)
        elif not re.match(self.emailPattern, addresse):
            self.rougir(self.entreeAddresse)
        else:
            if self.mode=="ajout":
                if obtenirClientparAttribue(telephone=telephone): 
                    self.wait_window(erreur(self, "un client possede deja ce numero"))
                elif obtenirClientparAttribue(addresse=addresse):
                    self.wait_window(erreur(self, "un client possede deja cet addresse"))
                else:
                    self.callback({"nom": nom, "prenom": prenom, "telephone": telephone, "addresse": addresse})
                    self.destroy()
            else:
                self.callback({"nom": nom, "prenom": prenom, "telephone": telephone, "addresse": addresse})
                self.destroy()

    def rougir(self, widget):
        widget.configure(fg_color = "red")
        self.after(1500, lambda:self.blanchir(widget))

    def blanchir(self, widget):
        widget.configure(fg_color="white")

    def quitter(self):
        #self.controller.controller.deiconify()
        self.destroy()


        

#ClientForm(None, {"nom": "fabio", "prenom": "fabio", "telephone": "fabio", "addresse": "addresse"})