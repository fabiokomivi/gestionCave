import customtkinter as ctk
import tkinter as tk
from PIL import Image
from .formulaire.commandeFormulaire import commandeForm
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class CommandePage(ctk.CTkFrame):

    commandeAttribue = ("nom", "prenom", "telepnone", "date", "montant")
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

        self.modifierBoutton = ctk.CTkButton(self.frameGauche, text="voir details", height=35, width=50)
        self.modifierBoutton.pack(side="right", padx=3, pady=3)

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

        self.selecteur = ctk.CTkComboBox(self.boxRecherche, values=self.commandeAttribue)
        self.selecteur.set(self.commandeAttribue[0])

        ctk.CTkLabel(self.boxRecherche, text="", image=ctk.CTkImage(Image.open(self.rechecheImagePath))).pack(padx=2, pady=2, side="right")

        self.rechercheEntree = ctk.CTkEntry(self.boxRecherche, width=200)
        self.rechercheEntree.pack(padx=2, pady=2, side="right")
        #self.rechercheEntree.bind("<KeyRelease>", self.recherche)

        self.selecteur.pack(side="left", padx=2, pady=2)

    def ajouterCommande(self):
        self.wait_window(commandeForm(self))
        #self.wait_window(commandeForm())