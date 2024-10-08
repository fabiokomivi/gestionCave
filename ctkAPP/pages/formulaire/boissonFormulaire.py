import customtkinter as ctk
from tkinter import filedialog
from controleur.boissonControler import *
from .erreur.erreur import erreur
from PIL import Image
import re

class boissonForm(ctk.CTkToplevel):

    patternNom = r"[a-zA-Z]+"
    patternPrix = r"[0-9]+"
    imageBinaire = ""

    def __init__(self, parent, callback, mode, categories,information):
        super().__init__(parent)

        self.callback=callback
        self.mode = mode
        self.information=information

        self.title(mode)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        topFrame = ctk.CTkFrame(self)
        for i in range(5):
            if i == 0:
                topFrame.grid_rowconfigure(i, weight=0)
            else:
                topFrame.grid_rowconfigure(i, weight=1)
                
        topFrame.grid_columnconfigure(0, weight=0)
        topFrame.grid_columnconfigure(1, weight=1)
        
        topFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.photoLabel = ctk.CTkLabel(topFrame, text="",width=150, height=150)
        self.entreeNom = ctk.CTkEntry(topFrame, width=150, placeholder_text="nom")
        self.entreePrix = ctk.CTkEntry(topFrame, width=150, placeholder_text="prix")
        self.selecteur = ctk.CTkComboBox(topFrame, values=categories, width=150)

        boutonValider = ctk.CTkButton(topFrame, text="selectionner", command=self.choisirImage)
        self.photoLabel.grid(column=0, row=0, rowspan=3, pady=10)
        self.entreeNom.grid(row=0, column=1, pady=10)
        self.entreePrix.grid(row=1, column=1)
        self.selecteur.grid(row=2, column=1, pady=10)
        boutonValider.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        confirmationFrame= ctk.CTkFrame(topFrame)
        confirmationFrame.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        ctk.CTkButton(confirmationFrame, text="annuler", fg_color="red", command=self.destroy).pack(side="left", padx=10, pady=5)
        ctk.CTkButton(confirmationFrame, text="valider", fg_color="green", command=self.verification).pack(side="right", padx=10, pady=5)

        if information:
            self.entreeNom.insert(0, information["nom"])
            self.entreePrix.insert(0, information["prix"])
            self.photoLabel.configure(image=information["image"])
            if information["categorie"] in self.selecteur._values:
                self.selecteur.set(information["categorie"])
        
        self.wait_visibility()
        self.grab_set()


    def verification(self):
        nom = self.entreeNom.get()
        prix = self.entreePrix.get()
        categorie = self.selecteur.get()

        if not re.match(self.patternNom, nom):
            self.rougir(self.entreeNom)
        elif not re.match(self.patternPrix, prix):
            self.rougir(self.entreePrix)
        else:
            if self.mode == "modification":
                boissons = obtenirBoissonParAttribue(tous=True)
                for boisson in boissons:
                    if boisson.id!=self.information["id"] and boisson.nom==nom:
                        self.wait_window(erreur(self, "ce nom de boisson existe dejà"))
                        return
                
                reponse = {"nom": nom, "prix": prix, "categorie": categorie, "image": self.imageBinaire}
                self.callback(reponse)
                self.destroy()
            elif self.mode == "ajout":
                boissons = obtenirBoissonParAttribue(tous=True)
                for boisson in boissons:
                    if boisson.nom==nom:
                        self.wait_window(erreur(self, "ce nom de boisson existe dejà"))
                        return
                reponse = {"nom": nom, "prix": prix, "categorie": categorie, "image": self.imageBinaire}
                self.callback(reponse)
                self.destroy()

                

    def choisirImage(self):
        fichierImage = filedialog.askopenfilename(
            filetypes=[("Fichiers image", "*.png")]
        )
        if fichierImage:
            image = Image.open(fichierImage)
            ctkImage = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)
            self.photoLabel.configure(image=ctkImage)
            with open(fichierImage, 'rb') as fichier:
                self.imageBinaire = fichier.read()

    def rougir(self, widget):
        widget.configure(fg_color = "red")
        self.after(1500, lambda:self.blanchir(widget))

    def blanchir(self, widget):
        widget.configure(fg_color="white")
   


"""boissonForm(ctk.CTk(), None, None, {"nom": "coca cola", "prix": 500})"""