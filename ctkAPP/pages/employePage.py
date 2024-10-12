import customtkinter as ctk
import tkinter as tk
from PIL import Image
from controleur.employeControler import *
from .formulaire.employeFormulaire import employeForm
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue
class EmployePage(ctk.CTkFrame):


    employeAttribue = ("nom", "prenom", "telephone", "addresse", "mot de passe")
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


        self.titre = ctk.CTkLabel(self, text="employes", font=ctk.CTkFont(family="Arial", size=25, weight="bold"), height=30)
        self.menu = ctk.CTkFrame(self, height=150)
        self.tabFrame = ctk.CTkFrame(self)
        
        self.titre.grid(row=0, column=0)
        self.menu.grid(row=1, column=0, sticky="ew", padx=5, pady=(5, 5))
        self.tabFrame.grid(row=2, column=0, sticky="nsew", padx=5, pady=(5, 5))

        self.frameGauche = ctk.CTkFrame(self.menu, height=50)
        self.frameGauche.pack(side="left", padx=3, pady=3)

        self.nouveauBoutton = ctk.CTkButton(self.frameGauche, text="nouveau", height=35, width=50, command=self.ajouterEmploye)
        self.nouveauBoutton.pack(side="left", padx=3, pady=3)

        self.modifierBoutton = ctk.CTkButton(self.frameGauche, text="modifier", height=35, width=50, command=self.modifierEmploye)
        self.modifierBoutton.pack(side="right", padx=3, pady=3)

        self.supprimerBoutton = ctk.CTkButton(self.menu, text="supprimer", height=35, width=50, command=self.supprimerEmploye)
        self.supprimerBoutton.pack(side="right", padx=3, pady=3)

        self.tabFrame.grid_columnconfigure(0, weight=1)
        self.tabFrame.grid_rowconfigure(1, weight=1)
        self.tabFrame.grid_rowconfigure(0, weight=0)

        self.barreRecherche = ctk.CTkFrame(self.tabFrame, height=50)

        style = tk.ttk.Style()
        style.configure("mystyle.Treeview", font=("Arial", 14))  # Augmenter la taille de la police
        style.configure("mystyle.Treeview.Heading", font=("Arial", 16, "bold"))  # Augmenter la taille de la police des titres
        style.configure("mystyle.Treeview", rowheight=30)  # Augmenter la hauteur des lignes


        self.employeTab = tk.ttk.Treeview(self.tabFrame, style="mystyle.Treeview",columns=self.employeAttribue, show="headings")
        

        for attribue in self.employeAttribue:
            self.employeTab.heading(attribue, text=attribue)

        self.barreRecherche.grid(row=0, column=0, padx=3, pady=3, sticky="ew")
        self.employeTab.grid(row=1, column=0, sticky="nsew")
        self.barreRecherche.grid_columnconfigure(0, weight=1)
        self.boxRecherche = ctk.CTkFrame(self.barreRecherche, width=300, height=50)
        self.boxRecherche.grid(row=0, column=0, pady=2)

        self.selecteur = ctk.CTkComboBox(self.boxRecherche, values=self.employeAttribue[0:4])
        self.selecteur.set(self.employeAttribue[0])

        ctk.CTkLabel(self.boxRecherche, text="", image=ctk.CTkImage(Image.open(self.rechecheImagePath))).pack(padx=2, pady=2, side="right")

        self.rechercheEntree = ctk.CTkEntry(self.boxRecherche, width=200)
        self.rechercheEntree.pack(padx=2, pady=2, side="right")
        self.rechercheEntree.bind("<KeyRelease>", self.recherche)

        self.selecteur.pack(side="left", padx=2, pady=2)
        self.miseAJourTable()

    def ajouterEmploye(self):
        self.wait_window(employeForm(self, self.avoirInfo, None, self.mode))
        if self.reponse:
            creerEmploye(self.controller.utilisateurCourant.id,
                        self.reponse["nom"],
                        self.reponse["prenom"],
                        self.reponse["telephone"],
                        self.reponse["addresse"],
                        self.reponse["mdp"])
            employe = obtenirEmployePar(telephone=self.reponse["telephone"], addresse=self.reponse["addresse"])[0]
            if employe:
                self.employeTab.insert("", tk.END, iid=employe.id, values=(employe.nom, employe.prenom, employe.telephone, employe.addresse, employe.motDePasse))

    def modifierEmploye(self):
        selection = self.employeTab.selection()
        if selection:
            self.mode = "modification"
            attribues = self.employeTab.item(selection)["values"]
            employe = { "nom": attribues[0], "prenom": attribues[1], "telephone": attribues[2], "addresse": attribues[3], "mdp": attribues[4]}
            self.wait_window(employeForm(self, self.avoirInfo,  employe, self.mode))
            if self.reponse:
                if modifierEmploye(employeId=eval(selection[0]),
                            nom=self.reponse["nom"],
                            prenom=self.reponse["prenom"],
                            telephone=self.reponse["telephone"],
                            addresse=self.reponse["addresse"],
                            mdp=self.reponse["mdp"]
                ):
                    self.employeTab.item(selection, values=(self.reponse["nom"], self.reponse["prenom"], self.reponse["telephone"], self.reponse["addresse"], self.reponse["mdp"]))


    def avoirInfo(self, information):
        self.reponse = information
        print(self.controller.utilisateurCourant.id)

    def miseAJourTable(self):
        employes = obtenirEmploye()
        if employes:
            self.employeTab.delete(*self.employeTab.get_children())
            for employe in employes:
                self.employeTab.insert("", tk.END, iid=employe.id, values=(employe.nom, employe.prenom, employe.telephone, employe.addresse, employe.motDePasse))

    def recherche(self, event=None):
        critere = self.selecteur.get()
        texteRechere = self.rechercheEntree.get()
        print(*self.employeTab.get_children())
        self.employeTab.delete(*self.employeTab.get_children())
        employes=None
        match critere:
            case "nom":
                employes = obtenirEmployePar(nom=texteRechere)
            case "prenom":
                employes = obtenirEmployePar(prenom=texteRechere)
            case "telephone":
                employes = obtenirEmployePar(telephone=texteRechere)
            case "addresse":
                employes = obtenirEmployePar(addresse=texteRechere)
        for employe in employes:
            print(employe.nom)
            self.employeTab.insert("", tk.END, iid=employe.id, values=(employe.nom, employe.prenom, employe.telephone, employe.addresse, employe.motDePasse))

    def supprimerEmploye(self):
        selection=self.employeTab.selection()
        if selection:
            print(selection[0])
            if supprimerEmploye(selection[0]):
                self.employeTab.delete(selection)