import customtkinter as ctk
import tkinter as tk
from PIL import Image
from .formulaire.categorieFormulaire import categorieForm
from controleur.categorieControler import *

ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class CategoriePage(ctk.CTkFrame):

    categorieAttribue = ("nom", "description")
    rechecheImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/recherche.png"
    reponse = {}
    mode = ""
    listeCategorie = []

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(2, weight=1)


        self.titre = ctk.CTkLabel(self, text="categories", font=ctk.CTkFont(family="Arial", size=25, weight="bold"), height=30)
        self.menu = ctk.CTkFrame(self, height=150)
        self.tabFrame = ctk.CTkFrame(self)
        
        self.titre.grid(row=0, column=0)
        self.menu.grid(row=1, column=0, sticky="ew", padx=5, pady=(5, 5))
        self.tabFrame.grid(row=2, column=0, sticky="nsew", padx=5, pady=(5, 5))

        self.frameGauche = ctk.CTkFrame(self.menu, height=50)
        self.frameGauche.pack(side="left", padx=3, pady=3)

        self.nouveauBoutton = ctk.CTkButton(self.frameGauche, text="nouveau", height=35, width=50, command=self.ajouter)
        self.nouveauBoutton.pack(side="left", padx=3, pady=3)

        self.modifierBoutton = ctk.CTkButton(self.frameGauche, text="modifier", height=35, width=50, command=self.modifier)
        self.modifierBoutton.pack(side="right", padx=3, pady=3)

        self.supprimerBoutton = ctk.CTkButton(self.menu, text="supprimer", height=35, width=50, command=self.supprimer)
        self.supprimerBoutton.pack(side="right", padx=3, pady=3)

        self.tabFrame.grid_columnconfigure(0, weight=1)
        self.tabFrame.grid_rowconfigure(1, weight=1)
        self.tabFrame.grid_rowconfigure(0, weight=0)

        self.barreRecherche = ctk.CTkFrame(self.tabFrame, height=50)
        self.categorieTab = tk.ttk.Treeview(self.tabFrame, columns=self.categorieAttribue, show="headings")
        

        for attribue in self.categorieAttribue:
            self.categorieTab.heading(attribue, text=attribue)

        self.barreRecherche.grid(row=0, column=0, padx=3, pady=3, sticky="ew")
        self.categorieTab.grid(row=1, column=0, sticky="nsew")
        self.barreRecherche.grid_columnconfigure(0, weight=1)
        self.boxRecherche = ctk.CTkFrame(self.barreRecherche, width=300, height=50)
        self.boxRecherche.grid(row=0, column=0, pady=2)

        self.selecteur = ctk.CTkComboBox(self.boxRecherche, values=self.categorieAttribue)
        self.selecteur.set(self.categorieAttribue[0])

        ctk.CTkLabel(self.boxRecherche, text="", image=ctk.CTkImage(Image.open(self.rechecheImagePath))).pack(padx=2, pady=2, side="right")

        self.rechercheEntree = ctk.CTkEntry(self.boxRecherche, width=200)
        self.rechercheEntree.pack(padx=2, pady=2, side="right")
        #self.rechercheEntree.bind("<KeyRelease>", self.recherche)

        self.selecteur.pack(side="left", padx=2, pady=2)

    
    def recherche(self, event=None):
        critere = self.selecteur.get()
        texteRechere = self.rechercheEntree.get()
        print(*self.categorieTab.get_children())
        self.categorieTab.delete(*self.categorieTab.get_children())
        match critere:
            case "id":
                print(f"'{texteRechere}'")
                self.listeCategorie = obtenirCategorieParAttribue (employeId=eval(texteRechere.strip()))
            case "nom":
                self.listeCategorie = obtenirCategorieParAttribue (nom=texteRechere)
            case "desciption":
                self.listeCategorie = obtenirCategorieParAttribue (desciption=texteRechere)
        for categorie in self.listeCategorie:
            print(categorie.nom)
            self.categorieTab.insert("", tk.END, values=(categorie.nom, categorie.desciption, categorie.telephone, categorie.addresse))

        




    def ajouterCategorie(self):
        self.mode = "ajout"
        self.wait_window(categorieForm(self, self.avoirInfo,  {}, self.mode))
        
        print(self.reponse)
        if creerCategorie(employeId=self.controller.utilisateurCourant.id,
                    nom=self.reponse["nom"],
                    desciption=self.reponse["desciption"],
                    telephone=self.reponse["telephone"],
                    addresse=self.reponse["addresse"]
                ):
            nouveau = obtenirCategorieParAttribue (telephone=self.reponse["telephone"], addresse=self.reponse["addresse"])
            print(nouveau)
            self.categorieTab.insert("", tk.END, iid=nouveau[0].id,values=(self.reponse["nom"], self.reponse["desciption"], self.reponse["telephone"], self.reponse["addresse"]))
        #self.miseAJourTable()

    def modifierCategorie(self):
        selection = self.categorieTab.selection()
        if selection:
            self.mode = "modification"
            attribues = self.categorieTab.item(selection)["values"]
            print(selection)
            print("selection[0]: ",selection[0])
            categorie = { "nom": attribues[0], "desciption": attribues[1], "telephone": attribues[2], "addresse": attribues[3]}
            self.wait_window(categorieForm(self, self.avoirInfo,  categorie, self.mode))
            print(selection, selection[0])
            if modifierCategorie(categorie_id=eval(selection[0]),
                        nom=self.reponse["nom"],
                        desciption=self.reponse["desciption"],
                        telephone=self.reponse["telephone"],
                        addresse=self.reponse["addresse"]
            ):
                self.categorieTab.item(selection, values=(self.reponse["nom"], self.reponse["desciption"], self.reponse["telephone"], self.reponse["addresse"]))

    def supprimer(self):
        selection=self.categorieTab.selection()
        if selection:
            supprimerCategorie(selection[0])
            self.miseAJourTable()

        
    def miseAJourTable(self):
        self.listeCategorie = obtenirCategorieParAttribue()
        self.categorieTab.delete(*self.categorieTab.get_children())
        for categorie in self.listeCategorie:
            self.categorieTab.insert("", tk.END, iid=categorie.id, values=(categorie.nom, categorie.desciption, categorie.telephone, categorie.addresse))

    def avoirInfo(self, information):
        self.reponse = information
        print(self.reponse)



