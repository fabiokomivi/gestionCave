import datetime
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from .formulaire.commandeFormulaire import commandeForm
from controleur.commandeControler import *
from controleur.clientControler import *
from controleur.ligneCommandeControler import *
from .formulaire.erreur.erreur import erreur
from weasyprint import CSS, HTML
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class CommandePage(ctk.CTkFrame):

    commandeAttribue = ("nom", "prenom", "telephone", "date", "montant")
    rechecheImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/recherche.png"
    reponse = {}


    def __init__(self, parent, controller):
        super().__init__(parent)
        ctk.CTkLabel(self, text="commande").grid(row=0, column=0)

        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(2, weight=1)


        self.titre = ctk.CTkLabel(self, text="commandes", font=ctk.CTkFont(family="Arial", size=25, weight="bold"), height=30)
        self.menu = ctk.CTkFrame(self, height=150)
        self.tabFrame = ctk.CTkFrame(self)
        
        self.titre.grid(row=0, column=0)
        self.menu.grid(row=1, column=0, sticky="ew", padx=5, pady=(5, 5))
        self.tabFrame.grid(row=2, column=0, sticky="nsew", padx=5, pady=(5, 5))

        self.frameGauche = ctk.CTkFrame(self.menu, height=50)
        self.frameGauche.pack(side="left", padx=3, pady=3)

        self.nouveauBoutton = ctk.CTkButton(self.frameGauche, text="nouveau", height=35, width=50, command=self.ajouterCommande)
        self.nouveauBoutton.pack(side="left", padx=3, pady=3)

        self.factureBoutton = ctk.CTkButton(self.frameGauche, text="facture", height=35, width=50, command=self.creerFacture)
        self.factureBoutton.pack(side="right", padx=3, pady=3)

        self.supprimerBoutton = ctk.CTkButton(self.menu, text="supprimer", height=35, width=50)
        self.supprimerBoutton.pack(side="right", padx=3, pady=3)

        self.tabFrame.grid_columnconfigure(0, weight=1)
        self.tabFrame.grid_rowconfigure(1, weight=1)
        self.tabFrame.grid_rowconfigure(0, weight=0)

        style = tk.ttk.Style()
        style.configure("mystyle.Treeview", font=("Arial", 14))  # Augmenter la taille de la police
        style.configure("mystyle.Treeview.Heading", font=("Arial", 16, "bold"))  # Augmenter la taille de la police des titres
        style.configure("mystyle.Treeview", rowheight=30)  # Augmenter la hauteur des lignes

        self.barreRecherche = ctk.CTkFrame(self.tabFrame, height=50)
        self.commandeTab = tk.ttk.Treeview(self.tabFrame, style="mystyle.Treeview", columns=self.commandeAttribue, show="headings")
        

        for attribue in self.commandeAttribue:
            self.commandeTab.heading(attribue, text=attribue)

        self.barreRecherche.grid(row=0, column=0, padx=3, pady=3, sticky="ew")
        self.commandeTab.grid(row=1, column=0, sticky="nsew")
        self.barreRecherche.grid_columnconfigure(0, weight=1)
        self.boxRecherche = ctk.CTkFrame(self.barreRecherche, width=300, height=50)
        self.boxRecherche.grid(row=0, column=0, pady=2)

        self.selecteur = ctk.CTkComboBox(self.boxRecherche, values=("nom", "prenom", "telephone"))
        self.selecteur.set(self.commandeAttribue[0])

        ctk.CTkLabel(self.boxRecherche, text="", image=ctk.CTkImage(Image.open(self.rechecheImagePath))).pack(padx=2, pady=2, side="right")

        self.rechercheEntree = ctk.CTkEntry(self.boxRecherche, width=200)
        self.rechercheEntree.pack(padx=2, pady=2, side="right")
        self.rechercheEntree.bind("<KeyRelease>", self.recherche)

        self.selecteur.pack(side="left", padx=2, pady=2)
        self.miseAjour()

    def ajouterCommande(self):
        self.wait_window(commandeForm(self, self.avoirCommande, self.controller))
        

    def avoirCommande(self, commande):
        client = obtenirClientparAttribue(clientId=commande.clientId)[0]
        lignesCommandes = obtenirLigneDeCommandes(commandeId=commande.id)
        montant = 0
        for ligneCommande in lignesCommandes:
            montant += ligneCommande.prix*ligneCommande.quantite
        self.commandeTab.insert("", tk.END, iid=commande.id, values=(client.nom, client.prenom, client.telephone, commande.dateCommande.strftime('%H:%M %d/%m/%Y'), montant)) 
        
    def miseAjour(self):
        commandes = obtenirCommandePar(tous=True)
        for commande in commandes:
            client = commande.client
            montant = 0
            for lignecommande in commande.lignesCommande:
                montant += lignecommande.quantite*lignecommande.boisson.prix
            self.commandeTab.insert("", tk.END, iid=commande.id, values=(client.nom, client.prenom, client.telephone, commande.dateCommande.strftime('%H:%M %d/%m/%Y'), montant))

    def recherche(self, event=None):
        critere = self.selecteur.get()
        texteRechere = self.rechercheEntree.get()
        self.commandeTab.delete(*self.commandeTab.get_children())
        match critere:
            case "id":
                clients = obtenirClientparAttribue(employeId=eval(texteRechere.strip()))
            case "nom":
                clients = obtenirClientparAttribue(nom=texteRechere)
            case "prenom":
                clients = obtenirClientparAttribue(prenom=texteRechere)
            case "telephone":
                clients = obtenirClientparAttribue(telephone=texteRechere)
            case "":
                clients = obtenirClientparAttribue(tous=True)
        for client in clients:  
            commandes = obtenirCommandePar(clientId=client.id)   
            for commande in commandes:
                if commande:
                    montant = 0
                    for detail in commande.lignesCommande:
                        montant += detail.quantite*detail.prix
                    self.commandeTab.insert("", tk.END, iid=commande.id, values=(client.nom, client.prenom, client.telephone, commande.dateCommande.strftime('%H:%M %d/%m/%Y'), montant))

    def creerFacture(self):
        selection = self.commandeTab.selection()
        if selection:
            commande = obtenirCommandePar(commandeId=selection[0])
            client = commande.client
            details = commande.lignesCommande

            factureHtml = f"""
            <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            margin: 0;
                            padding: 0;
                        }}
                        .container {{
                            width: 95%;
                            margin: 0 auto;
                            padding: 5px;
                        }}
                        .header {{
                            text-align: center;
                            font-size: 24px;
                            font-weight: bold;
                            margin-bottom: 40px;
                        }}
                        .client-date {{
                            display: flex;
                            justify-content: space-between;
                            margin-bottom: 20px;
                        }}
                        .client-info {{
                            float: left;
                        }}
                        .date-info {{
                            text-align: right;
                        }}
                        .clearfix {{
                            clear: both;
                        }}
                        table {{
                            width: 100%;
                            border-collapse: collapse;
                            margin-top: 20px;
                        }}
                        table, th, td {{
                            border: 1px solid black;
                        }}
                        th, td {{
                            padding: 10px;
                            text-align: center;
                        }}
                        th {{
                            background-color: #f2f2f2;
                        }}
                        tfoot td {{
                            font-weight: bold;
                        }}
                        .total {{
                            margin-top: 20px;
                            text-align: right;
                            font-size: 18px;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            FACTURE N°{commande.id}
                        </div>
                        <div class="client-date">
                            <div class="client-info">
                                <p>Nom: {client.nom}</p>
                                <p>Prénom: {client.prenom}</p>
                                <p>Téléphone: {client.telephone}</p>
                                <p>Adresse: {client.addresse}</p>
                            </div>
                            <div class="date-info">
                                <p>Date: {commande.dateCommande.strftime('%d/%m/%Y')}</p>
                            </div>
                        </div>

                        <table>
                            <thead>
                                <tr>
                                    <th>Produit</th>
                                    <th>Quantité</th>
                                    <th>Prix Unitaire (FCFA)</th>
                                    <th>Total (FCFA)</th>
                                </tr>
                            </thead>
                            <tbody>
            """
            for detail in details:
                nom = detail.boisson.nom
                quantite = detail.quantite
                prix = detail.boisson.prix
                prixTotal = detail.prixTotal
                factureHtml += f"""
                                <tr>
                                    <td>{nom}</td>
                                    <td>{quantite}</td>
                                    <td>{prix}</td>
                                    <td>{prixTotal}</td>
                                </tr>
                """
            total_general = sum(detail.quantite * detail.boisson.prix for detail in details)
            factureHtml += f"""
                            </tbody>
                            <tfoot>
                                <tr>
                                    <td colspan="3">Total Général</td>
                                    <td>{total_general} FCFA</td>
                                </tr>
                            </tfoot>
                        </table>
                    </div>
                </body>
            </html>
            """
            html = HTML(string=factureHtml)
            html.write_pdf(f"ctkAPP/factures/facture_{commande.id}.pdf", stylesheets=[CSS(string='@page { size: A5; }')])
            self.wait_window(erreur(self, "facture generee avec succes"))


