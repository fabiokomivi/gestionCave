import customtkinter as ctk
import tkinter as tk
from datetime import datetime
from controleur.commandeControler import *
from controleur.employeControler import *
from controleur.boissonControler import *
from .formulaire.visuelDiagramme import DiagramViewer
import calendar
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from PIL import Image



class DashboardPage(ctk.CTkFrame):

    annee = {1:"jan", 2:"fev", 3:"mar", 4:"avr", 5:"mai", 6:"jun", 7:"jui", 8:"aou", 9:"sep", 10:"oct", 11:"nov", 12:"dec"}
    progresbars = {}
    venteTabTitle = ("nom", "prenom", "total")

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller
        self.initBody()

    
    def initBody(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, minsize=150)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, minsize=300)

        topLeftFrame = ctk.CTkFrame(self)
        self.initsales(topLeftFrame)
        topRightFrame = ctk.CTkFrame(self)
        bottomFrame = ctk.CTkFrame(self)

        topLeftFrame.grid(row=0, column=0, padx=(5, 2), pady=3, sticky="nsew")
        topRightFrame.grid(row=0, column=1, rowspan=2, padx=(2, 5), pady=3, sticky="nsew")
        bottomFrame.grid(row=1, column=0, padx=5, pady=3, sticky="nsew")
        bottomFrame.grid_rowconfigure(0, minsize=125)
        bottomFrame.grid_rowconfigure(1, minsize=25)

        for i in range(len(self.annee)):
            bottomFrame.grid_columnconfigure(i, weight=1)

        for mois in self.annee.values():
            self.progresbars[mois] = ctk.CTkProgressBar(bottomFrame,orientation="vertical", width=25, corner_radius=6)

        for i in range(1, len(self.annee)+1):
            ctk.CTkLabel(bottomFrame, text=self.annee[i]).grid(row=1, column=i-1, padx=2, pady=1)
            self.progresbars[self.annee[i]].grid(row=0, column=i-1, padx=2, pady=(5, 1))

        for i in range(4):
            if i<2:
                topRightFrame.grid_columnconfigure(i, minsize=150)
                topRightFrame.grid_rowconfigure(i, minsize=150)
            else:
                topRightFrame.grid_rowconfigure(i, minsize=150)
            
        ctk.CTkButton(topRightFrame, text="quantites\nde boissons", command=self.diagrammeBareBoissons).grid(row=0, column=0, sticky="nsew", padx=5,pady=5)
        ctk.CTkButton(topRightFrame, text="quantite de\nboissonn par\ncategories", command=self.diagrammeBoissonCategorie).grid(row=1, column=0, sticky="nsew", padx=5,pady=5)
        ctk.CTkButton(topRightFrame, text="vente par\n prix de\nboissons", command=self.diagrammeVenteParBoisson).grid(row=0, column=1, sticky="nsew", padx=5,pady=5)
        ctk.CTkButton(topRightFrame, text="vente par\ncategories\nde boissons", command=self.diagrammeVenteParCategorie).grid(row=1, column=1, sticky="nsew", padx=5,pady=5)
        ctk.CTkButton(topRightFrame, text="vente par\nemployes", command=self.diagrammeVenteParEmploye).grid(row=2, column=0, sticky="nsew", padx=5,pady=5)
        ctk.CTkButton(topRightFrame, text="autres", command=self.diagrammeVenteParCategorie).grid(row=2, column=1, sticky="nsew", padx=5,pady=5)


        self.miseAjourVente()
        self.miseAjour()

    def initsales(self, frame):
        frame.grid_rowconfigure(0, minsize=50)
        frame.grid_rowconfigure(1, minsize=50)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(frame, text="ventes", font=("Arial", 30)).grid(row=0, column=0, padx=5, pady=(5,3))

        checkFrame = ctk.CTkFrame(frame, height=50)

        checkFrame.grid_columnconfigure(0, weight=1)

        #ctk.CTkButton(checkFrame, command=self.ouvreCalendrier).grid(row=0, column=0, padx=3, pady=5)
        self.calendrier = DateEntry(checkFrame, width=15, background='black', foreground='white', borderwidth=2, 
                     year=datetime.now().year, font=("Helvetica", 12), selectbackground='darkblue', selectforeground='white',
                     day=datetime.now().day, month=datetime.now().month, showweeknumbers=False)
        self.calendrier.grid(row=0, column=0, padx=3, pady=5)
        self.calendrier.bind("<<DateEntrySelected>>", self.miseAjourVente)



        checkFrame.grid(row=1, column=0, padx=5, pady=(3,3), sticky="ew")

        style = tk.ttk.Style()
        style.configure("mystyle.Treeview", font=("Arial", 14))  # Augmenter la taille de la police
        style.configure("mystyle.Treeview.Heading", font=("Arial", 16, "bold"))  # Augmenter la taille de la police des titres
        style.configure("mystyle.Treeview", rowheight=30)  # Augmenter la hauteur des lignes


        self.venteTab = tk.ttk.Treeview(frame, style="mystyle.Treeview",columns=self.venteTabTitle, show="headings")
        for attribue in self.venteTabTitle:
            self.venteTab.heading(attribue, text=attribue)
        self.venteTab.grid(row=2, column=0, sticky="nsew", padx=5, pady=(3,3))


    def miseAjour(self):
        ventes = {"jan": 0, "fev": 0, "mar": 0, "avr": 0, "mai": 0, "jun": 0, "jui": 0, "aou": 0, "sep": 0, "oct": 0, "nov": 0, "dec": 0}
        venteTotal = 0
        anneeCourrant = datetime.now().year
        commandes = obtenirCommandePar(tous=True)
        for commande in commandes:
            jour, mois, annee = commande.avoirJourMoisAnnee()
            if anneeCourrant==annee:
                ventes[self.annee[mois]]+=commande.prixTotal()
                venteTotal += commande.prixTotal()
        if venteTotal>0:
            for mois in self.annee.values():
                self.progresbars[mois].set(ventes[mois] / venteTotal)
                self.progresbars[mois].update_idletasks()
        #self.chargerDiagrammeBarres()


    def miseAjourVente(self, event=None):
        date = self.calendrier.get_date()  # pas besoin de strptime
        anneeSel, moisSel, jourSel = date.year, date.month, date.day
        employes = obtenirEmploye()
        self.venteTab.delete(*self.venteTab.get_children())
        
        for employe in employes:
            montant = 0
            for commande in employe.commandes:
                jour, mois, annee = commande.avoirJourMoisAnnee()
                if mois == moisSel and jour == jourSel and annee == anneeSel:
                    montant += commande.prixTotal()
                    
            self.venteTab.insert("", tk.END, iid=employe.id, values=(employe.nom, employe.prenom, montant))


    def diagrammeBoissonCategorie(self):
        categories, quantites = obtenirBoissonsParCategorie()

        plt.figure(figsize=(6,6))
        plt.pie(quantites, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

        plt.title('Répartition des types de boissons par catégorie')
        plt.axis('equal')  # Pour garder le cercle
        plt.legend(loc='lower left', ncol=3, bbox_to_anchor=(0.1, -0.15))  # Légende en bas au milieu

        # Enregistrer le diagramme en tant qu'image PNG
        'ctkAPP/pages/diagrammes/diagrammesTypesBoissons.png'
        plt.savefig('ctkAPP/pages/diagrammes/diagrammesTypesBoissons.png')
        plt.close()
        self.wait_window(DiagramViewer(self.controller, 'ctkAPP/pages/diagrammes/diagrammesTypesBoissons.png'))

    
    def diagrammeBareBoissons(self):
        noms, quantites = obtenirQuantitesBoissons()

        plt.figure(figsize=(10, 6))
        plt.bar(noms, quantites, color=plt.cm.Paired.colors)
        
        plt.title('Quantité de Chaque Boisson')
        plt.xlabel('Boissons')
        plt.ylabel('Quantité')
        plt.xticks(rotation=45, ha='right')  # Rotation des labels pour une meilleure lisibilité
        plt.tight_layout()  # Ajuste les marges pour éviter le chevauchement
        plt.savefig('ctkAPP/pages/diagrammes/diagrammesBoissonsBarres.png')
        plt.close()
        self.wait_window(DiagramViewer(self.controller, 'ctkAPP/pages/diagrammes/diagrammesBoissonsBarres.png'))

    def diagrammeVenteParCategorie(self):
        categories, ventes = obtenirVentesParCategorie()
    
        # Génération du diagramme en barres
        plt.figure(figsize=(8, 6))
        plt.bar(categories, ventes, color=plt.cm.Paired.colors)
        plt.xlabel('Catégories de Boissons')
        plt.ylabel('Ventes (quantité)')
        plt.title('Ventes par Catégorie de Boissons')
        
        # Sauvegarde du diagramme
        plt.savefig('ctkAPP/pages/diagrammes/ventesCategorie.png')
        plt.close()
        self.wait_window(DiagramViewer(self.controller, 'ctkAPP/pages/diagrammes/ventesCategorie.png'))

    def diagrammeVenteParBoisson(self):
        boissons, ventes = obtenirVentesParBoisson()
        
        plt.figure(figsize=(10, 6))
        plt.bar(boissons, ventes, color=plt.cm.Paired.colors)
        plt.xlabel('Boissons')
        plt.ylabel('Ventes')
        plt.title('Ventes par Boisson')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig('ctkAPP/pages/diagrammes/ventesBoisson.png')
        plt.close()
        self.wait_window(DiagramViewer(self.controller, 'ctkAPP/pages/diagrammes/ventesBoisson.png'))

    def diagrammeVenteParEmploye(self):
        employes, ventes = obtenirVenteParEmployes()
        
        plt.figure(figsize=(10, 6))
        plt.bar(employes, ventes, color=plt.cm.Paired.colors)
        plt.xlabel('employes')
        plt.ylabel('Ventes')
        plt.title('Ventes par employes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig('ctkAPP/pages/diagrammes/ventesEmployes.png')
        plt.close()
        self.wait_window(DiagramViewer(self.controller, 'ctkAPP/pages/diagrammes/ventesEmployes.png'))




