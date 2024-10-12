import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from controleur.boissonControler import *
from controleur.commandeControler import *
from controleur.ligneCommandeControler import * 
from .erreur.erreur import erreur
from PIL import Image
import re
from .choisirClient import choixClient
from .choisirBoisson import choixBoisson
from .erreur.erreur import erreur

class commandeForm(ctk.CTkToplevel):

    commandeAttribue = ("nom", "prix unitaire", "quantite", "prix total")
    clientCourant = None
    boissonsList = {}

    def __init__(self, parent, callback,controller):
        super().__init__(parent)
        self.controller = controller
        self.callback = callback
        self.geometry("800x500")
        self.title("commandes")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.contenu = ctk.CTkFrame(self)
        self.contenu.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.initBody()



        self.wait_visibility()
        self.grab_set()


    def initBody(self):
        self.contenu.grid_rowconfigure(0, minsize=75)
        self.contenu.grid_rowconfigure(1, weight=1)
        self.contenu.grid_columnconfigure(0, weight=1)

        clientFrame = ctk.CTkFrame(self.contenu, height=60)
        clientFrame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        clientFrame.grid_propagate(False)
        for i in range(4):
            if i == 0:
                clientFrame.grid_columnconfigure(i, minsize=100)
            else:
                clientFrame.grid_columnconfigure(i, weight=1)
        clientFrame.grid_rowconfigure(0, weight=1)

        ctk.CTkButton(clientFrame, text="choisir un client", command=self.choisirClient).grid(row=0, column=0, padx=(10, 5), pady=3)
        self.labelNom = ctk.CTkLabel(clientFrame, text="nom")
        self.labelPrenom = ctk.CTkLabel(clientFrame, text="prenom")
        self.labelTelephone = ctk.CTkLabel(clientFrame, text="telephone")

        self.labelNom.grid(row=0, column=1, padx=3, pady=3)
        self.labelPrenom.grid(row=0, column=2, padx=3, pady=3)
        self.labelTelephone.grid(row=0, column=3, padx=3, pady=3)

        commandeFrame = ctk.CTkFrame(self.contenu)
        commandeFrame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        controlFrame = ctk.CTkFrame(commandeFrame, height=75)
        controlFrame.pack(side="top", padx=5, pady=5, fill="x")
        ctk.CTkButton  (controlFrame, text="ajouter", command=self.choisirBoisson).pack(side="left", padx=5, pady=5)
        ctk.CTkButton  (controlFrame, text="supprimer").pack(side="left", padx=5, pady=5)
        ctk.CTkButton  (controlFrame, text="valider", command=self.valider).pack(side="right", padx=5, pady=5)

        style = tk.ttk.Style()
        style.configure("mystyle.Treeview", font=("Arial", 14))  # Augmenter la taille de la police
        style.configure("mystyle.Treeview.Heading", font=("Arial", 16, "bold"))  # Augmenter la taille de la police des titres
        style.configure("mystyle.Treeview", rowheight=30)  # Augmenter la hauteur des lignes

        self.ligneCommandeTab = tk.ttk.Treeview(commandeFrame,style="mystyle.Treeview", columns=self.commandeAttribue, show="headings")
        for attribue in self.commandeAttribue:
            self.ligneCommandeTab.heading(attribue, text=attribue)
        self.ligneCommandeTab.pack(side="bottom", expand=True, fill="both")

    def choisirClient(self):
        self.wait_window(choixClient(self, self.avoirClient))

    def choisirBoisson(self):
        self.wait_window(choixBoisson(self, self.avoirBoisson, self.boissonsList.keys()))

    def avoirClient(self, client):
        self.clientCourant = client
        self.labelNom.configure(text=client.nom)
        self.labelPrenom.configure(text=client.prenom)
        self.labelTelephone.configure(text=client.telephone)

    def avoirBoisson(self, boisson, quantite):
        self.boissonsList[boisson.nom]=(boisson, quantite)
        self.ligneCommandeTab.insert("", tk.END, iid=boisson.id, values=(boisson.nom, boisson.prix, quantite, boisson.prix*quantite))


    def valider(self):
        if not self.clientCourant:
            self.wait_window(erreur(self, "veuillez choisir un client"))
        elif len(self.ligneCommandeTab.get_children())==0:
            self.wait_window(erreur(self, "veuillez choisir une boisson"))
        else:
            commande = creerCommande(employeId=self.controller.utilisateurCourant.id, clientId=self.clientCourant.id)
            for boissonNom in self.boissonsList.keys():
                boissons = self.boissonsList[boissonNom]
                AjouterLigneCommande(commande.id, boissons[0].id, boissons[1], prix=boissons[0].prix, prixTotal=boissons[0].prix*boissons[1])
                mettreAjourBoisson(boissons[0].id, boissons[1])
            self.callback(commande)
            self.destroy()


