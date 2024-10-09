import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from controleur.boissonControler import *
from .erreur.erreur import erreur
from PIL import Image
import io
import re

class choixBoisson(ctk.CTkToplevel):

    boissonAttribue = ("nom", "prix", "categorie", "stock")
    patternQuantite = r"[0-9]+"
    rechecheImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/recherche.png"
    boissonCourant = None

    def __init__(self, parent, callback, listBoisson):
        super().__init__(parent)
        self.callback = callback
        self.listBoisson = listBoisson
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.contenu = ctk.CTkFrame(self)
        self.contenu.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.initBody()
        self.chargerBoissons()

        self.wait_visibility()
        self.grab_set()

    def initBody(self):
        self.contenu.grid_rowconfigure(0, minsize=50)
        self.contenu.grid_rowconfigure(1, weight=1)
        self.contenu.grid_columnconfigure(0, weight=1)
        topFrame = ctk.CTkFrame(self.contenu, height=50)
        topFrame.grid_propagate(False)
        topFrame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        ctk.CTkButton(topFrame, text="annuler").pack(side="left", padx=5, pady=5)
        ctk.CTkButton(topFrame, text="valider", command=self.valider).pack(side="right", padx=5, pady=5)

        bottomFrame = ctk.CTkFrame(self.contenu)
        bottomFrame.grid_columnconfigure(0, weight=1)
        bottomFrame.grid_columnconfigure(1, minsize=155)
        bottomFrame.grid_rowconfigure(0, weight=1)

        bottomFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        style = tk.ttk.Style()
        style.configure("mystyle.Treeview", font=("Arial", 14))  # Augmenter la taille de la police
        style.configure("mystyle.Treeview.Heading", font=("Arial", 16, "bold"))  # Augmenter la taille de la police des titres
        style.configure("mystyle.Treeview", rowheight=30)  # Augmenter la hauteur des lignes
        self.boissonTab = tk.ttk.Treeview(bottomFrame, style="mystyle.Treeview", columns=self.boissonAttribue, show="headings")
        for attribue in self.boissonAttribue:
            self.boissonTab.heading(attribue, text=attribue)

        self.boissonTab.grid(row=0, column=0, sticky="nsew")
        self.boissonTab.bind("<<TreeviewSelect>>", self.surSelection)

        choixFrame = ctk.CTkFrame(bottomFrame)
        choixFrame.pack_propagate(False)
        choixFrame.grid(row=0, column=1, sticky="ns", padx=5, pady=5)

        self.photoLabel = ctk.CTkLabel(choixFrame, height=150, width=150, text="")
        self.photoLabel.pack(side="top", pady=5, padx=3)

        self.nomLabel = ctk.CTkLabel(choixFrame,width=100, text="nom")
        self.nomLabel.pack(side="top", pady=5, padx=3)
        self.prixLabel = ctk.CTkLabel(choixFrame,width=100, text="prix")
        self.prixLabel.pack(side="top", pady=5, padx=3)
        self.quantiteEntree = ctk.CTkEntry(choixFrame, placeholder_text="quantite")
        self.quantiteEntree.pack(side="top", pady=5, padx=3)

    def chargerBoissons(self):
        boissons = obtenirBoissonParAttribue(tous=True)
        for boisson in boissons:
            self.boissonTab.insert("", tk.END, iid=boisson.id, values=(boisson.nom, boisson.prix, boisson.categorie.nom, boisson.stock.quantite))

    def bitVersImage(self, imageBinaire):
        if imageBinaire:
            fluxImage = io.BytesIO(imageBinaire)
            image = Image.open(fluxImage)
            ctkImgae = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)
            return ctkImgae
        
    def surSelection(self, event):
        selection = self.boissonTab.selection()
        if selection:
            id = selection[0]
            self.boissonCourant=obtenirBoissonParAttribue(tous=False, boissonId=id)[0]
            self.photoLabel.configure(image=self.bitVersImage(self.boissonCourant.image))
            self.nomLabel.configure(text=self.boissonCourant.nom)
            self.prixLabel.configure(text=str(self.boissonCourant.prix))
            #self.labelVisuel.image=self.bitVersImage(boisson.image)

    def rougir(self, widget):
        widget.configure(fg_color = "red")
        self.after(1500, lambda:self.blanchir(widget))

    def blanchir(self, widget):
        widget.configure(fg_color="white")

    def valider(self):
        if self.boissonCourant:
            quantite = self.quantiteEntree.get()
            if not re.match(self.patternQuantite, quantite):
                self.rougir(self.quantiteEntree)
            elif self.boissonCourant.nom in self.listBoisson:
                self.wait_window(erreur(self ,f"{self.boissonCourant.nom} a déjà été selectionné"))
            elif self.boissonCourant.stock.quantite < int(quantite):
                self.wait_window(erreur(self ,f"quantite de {self.boissonCourant.nom} est inssufisant"))
            else:
                self.callback(self.boissonCourant, int(quantite))
                self.destroy()




        