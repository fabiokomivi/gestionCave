import customtkinter as ctk
import tkinter as tk
from controleur.categorieControler import *
from controleur.boissonControler import *
from .formulaire.boissonFormulaire import boissonForm
from .formulaire.erreur.confirmation import Confirmation
import io
from PIL import Image

ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class BoissonPage(ctk.CTkFrame):

    boissonAttribue = ("nom", "prix", "categorie")
    mode = ""
    reponse = {}
    autoriserSuppression = False

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_rowconfigure(0, minsize=200)
        self.grid_rowconfigure(1, weight=1)
        for i in range(3):
            if i==0:
                self.grid_columnconfigure(i, minsize=200)
            else:
                self.grid_columnconfigure(i, weight=1)
        self.initMenu()
        
        style = tk.ttk.Style()
        style.configure("mystyle.Treeview", font=("Arial", 14))  # Augmenter la taille de la police
        style.configure("mystyle.Treeview.Heading", font=("Arial", 16, "bold"))  # Augmenter la taille de la police des titres
        style.configure("mystyle.Treeview", rowheight=30)  # Augmenter la hauteur des lignes

        self.boissonTab = tk.ttk.Treeview(self,style="mystyle.Treeview", columns=self.boissonAttribue, show="headings")
        self.boissonTab.bind("<<TreeviewSelect>>", self.surSelection)

        for attribue in self.boissonAttribue:
            self.boissonTab.heading(attribue, text=attribue)

        self.boissonTab.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.miseAjour()


    def initMenu(self):
        visuelFrame = ctk.CTkFrame(self, width=200, height=200)
        controlFrame = ctk.CTkFrame(self)
        rechercheFramne = ctk.CTkFrame(self)

        visuelFrame.grid(row=0, column=0, padx=5, pady=5)
        controlFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        rechercheFramne.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        for i in range(3):
            controlFrame.grid_rowconfigure(i, weight=1)
        controlFrame.grid_columnconfigure(0, weight=1)

        ctk.CTkButton(controlFrame, text="nouveau", width=100, command=self.ajouterBoisson).grid(row=0, column=0)
        ctk.CTkButton(controlFrame, text="modifier", width=100, command=self.modifierBoisson).grid(row=1, column=0)
        ctk.CTkButton(controlFrame, text="supprimer", width=100, command=self.supprimerBoisson).grid(row=2, column=0)

        for i in range(3):
            rechercheFramne.grid_rowconfigure(i, weight=1)
        rechercheFramne.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(rechercheFramne, text="recherche").grid(column=0, row=0)
        self.selecteur = ctk.CTkComboBox(rechercheFramne, values=("nom", "prix"))
        self.rechercher = ctk.CTkEntry(rechercheFramne)

        self.rechercher.bind("<KeyRelease>", self.recherche)

        self.selecteur.grid(column=0, row=1)
        self.rechercher.grid(column=0, row=2)

        visuelFrame.pack_propagate(False)
        self.labelVisuel = ctk.CTkLabel(visuelFrame, text="")
        self.labelVisuel.pack(fill="both", expand=True, padx=3, pady=3)



    def surSelection(self, event):

        selection = self.boissonTab.selection()
        if selection:
            id = selection[0]
            boisson=obtenirBoissonParAttribue(tous=False, boissonId=id)[0]
            self.labelVisuel.configure(image=self.bitVersImage(boisson.image))
            self.labelVisuel.image=self.bitVersImage(boisson.image)

        

    def avoirInfo(self, dico):
        self.reponse=dico

    def ajouterBoisson(self):
        self.mode = "ajout"
        self.wait_window(boissonForm(self.controller, self.avoirInfo, self.mode, self.avoirCategories(),{}))
        if self.reponse:
            categorie = obtenirCategorieParAttribue(tous=False, nom=self.reponse["categorie"])
            categorieId = categorie[0].id

            if creerBoisson(nom=self.reponse["nom"], prix=self.reponse["prix"], categorieId=categorieId, image=self.reponse["image"]): #insertion de la boisson dans la base de donnees
                boisson = obtenirBoissonParAttribue(tous=False, nom=self.reponse["nom"])[0]
                if boisson:
                    self.boissonTab.insert("", tk.END, iid=boisson.id, values=(boisson.nom, boisson.prix, boisson.categorie.nom))


    def modifierBoisson(self):
        self.mode = "modification"
        selection = self.boissonTab.selection()
        if selection:
            boisson = obtenirBoissonParAttribue(tous=False, boissonId=selection[0])[0]
            dicoDonnees = {"id": boisson.id, "nom": boisson.nom, "prix": boisson.prix, "categorie": boisson.categorie.nom, "image": self.bitVersImage(boisson.image)}
            self.wait_window(boissonForm(self.controller, self.avoirInfo, self.mode, self.avoirCategories(),dicoDonnees))
            if self.reponse:

                categorie = obtenirCategorieParAttribue(tous=False, nom=self.reponse["categorie"])[0]

                if modifierBoisson(boissonId=boisson.id, nom=self.reponse["nom"],prix=self.reponse["prix"], categorieId=categorie.id, image=self.reponse["image"]):
                    self.boissonTab.item(selection[0], values=(self.reponse["nom"], self.reponse["prix"], self.reponse["categorie"]))


    def recherche(self, event=None):
        critere = self.selecteur.get()
        texteRechere = self.rechercher.get()
        match critere:
            case "nom":
                boissons = obtenirBoissonParAttribue(nom=texteRechere, tous=False)
            case "prix":
                boissons = obtenirBoissonParAttribue (prix=texteRechere, tous=False)


        self.boissonTab.delete(*self.boissonTab.get_children())
        for boisson in boissons:
            self.boissonTab.insert("", tk.END, iid=boisson.id, values=(boisson.nom, boisson.prix, boisson.categorie.nom))


    def supprimerBoisson(self):
        selection = self.boissonTab.selection()
        if selection:
            message = "cette action supprimera toutes\nles commandes unitaires associees"
            self.wait_window(Confirmation(self.controller, message, self.demandeAutorisation))
            if self.autoriserSuppression:
                if supprimerBoisson(selection[0]):
                    self.boissonTab.delete(selection[0])

    def avoirCategories(self):
        categories = obtenirCategorieParAttribue(tous=True)
        liste = []
        for categorie in categories:
            liste.append(categorie.nom)
        return liste

    def miseAjour(self):
        self.boissonTab.delete(*self.boissonTab.get_children())
        boissons = obtenirBoissonParAttribue(tous=True)
        for boisson in boissons:
            self.boissonTab.insert("", tk.END, iid=boisson.id, values=(boisson.nom, boisson.prix, boisson.categorie.nom))

    def bitVersImage(self, imageBinaire):
        if imageBinaire:
            fluxImage = io.BytesIO(imageBinaire)
            image = Image.open(fluxImage)
            ctkImgae = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)
            return ctkImgae
        
    def demandeAutorisation(self, permission):
        self.autoriserSuppression = permission
