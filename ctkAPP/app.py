import time
import customtkinter as ctk
from widget.widget import menuItem
from pages.commandePage import CommandePage
from pages.clientPage import ClientPage
from pages.parametrePage import ParametrePage
from pages.gestionPage import GestionPage
from pages.categoriePage import CategoriePage
from pages.boissonPage import BoissonPage
from pages.employePage import EmployePage
from pages.stockPage import StockPage

from pages.bienvenue import BienvenuePage
from pages.connexionPage import ConnexionPage
from pages.contentPage import ContentPage
from PIL import Image 

from controleur.chefControler import *
from controleur.employeControler import *

# Initialiser CustomTkinter
ctk.set_appearance_mode("light")  # Mode sombre
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

#creerChef("amouzou", "fabio", "fabio2002", "06661918")
#creerEmploye(1, "toto", "patrick", "employe1", "01010101", "toto@gmail.com")

class APP(ctk.CTk):

    commandImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/commande.png"
    clientImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/client.png"
    bossImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/boss.png"
    dashboardImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/dashboard.png"
    deleteImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/delete.png"
    exitImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/exit.png"
    settingImagePath = "/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/settings.png"

    pagesPrimaire = {}
    pagesSecondaire = {}
    pagesEmploye = {}
    pagesChef = {}
    utilisateurType = ""
    utilisateurCourant = None



    def __init__(self):
        super().__init__()

        

        self.geometry("1200x650")
        self.minsize(1100, 650)
        self.title("CustomTkinter Application")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.initRootContent()
        
        self.after(1000, self.remplaceBienvenue)
        self.mainloop()

    def initMenu(self):
        self.menu = ctk.CTkFrame(self.contentMain, width=200)
        self.menu.grid_columnconfigure(0, weight=1)
        self.menu.grid_propagate(False)
        self.menu.grid(row=0, column=0, sticky="nsew")

        ctk.CTkLabel(self.menu, text="menu").grid(row=0, column=0, padx=5, sticky="ew", pady=(10, 15))

        menuItem(self.menu, self, "clients", self.clientImagePath, 1)
        menuItem(self.menu, self, "commandes", self.commandImagePath, 2)
        menuItem(self.menu, self, "gestions", self.bossImagePath, 3)
        menuItem(self.menu, self, "parametres", self.settingImagePath, 4)
        menuItem(self.menu, self, "quitter", self.exitImagePath, 5)

    
    def initRootContent(self):
        
        self.root=ctk.CTkFrame(self)  #creation de la fenetre root
        self.root.grid(row=0, column=0, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.pagesPrimaire["bienvenue"] = BienvenuePage(self.root, self)
        self.pagesPrimaire["connexion"] = ConnexionPage(self.root, self)
        self.pagesPrimaire["contenu"] = ContentPage(self.root, self)
        for pagePrimaire in self.pagesPrimaire.values():
            pagePrimaire.grid(row=0, column=0, sticky="nsew")
        self.pagesPrimaire["bienvenue"].tkraise()

        
        self.pagesSecondaire["pageEmploye"] = ctk.CTkFrame(self.pagesPrimaire["contenu"])
        self.pagesSecondaire["gestions"] = ctk.CTkFrame(self.pagesPrimaire["contenu"])
        for pageSecondaire in self.pagesSecondaire.values():

            pageSecondaire.grid_columnconfigure(0, weight=0)
            pageSecondaire.grid_columnconfigure(1, weight=1)
            pageSecondaire.grid_rowconfigure(0, weight=1)

            pageSecondaire.grid(row=0, column=0, columnspan=2, sticky="nsew")

        

        # menu employe
        self.menuEmploye = ctk.CTkFrame(self.pagesSecondaire["pageEmploye"], width=200)
        self.menuEmploye.grid_columnconfigure(0, weight=1)
        self.menuEmploye.grid_propagate(False)
        self.menuEmploye.grid(row=0, column=0, sticky="ns")

        ctk.CTkLabel(self.menuEmploye, text="menu").pack(pady=(10, 15))
        #self.chargerBoutonMenu()


        self.employeContenu=ctk.CTkFrame(self.pagesSecondaire["pageEmploye"])
        self.employeContenu.grid(row=0, column=1, sticky="nsew")
        self.employeContenu.grid_columnconfigure(0, weight=1)
        self.employeContenu.grid_rowconfigure(0, weight=1)

        self.pagesEmploye["clients"] = ClientPage(self.employeContenu, self)
        self.pagesEmploye["commandes"] = CommandePage(self.employeContenu, self)
        self.pagesEmploye["parametres"] = ParametrePage(self.employeContenu, self)
        self.pagesEmploye["gestions"] = GestionPage(self.employeContenu, self)
        for pageEmploye in self.pagesEmploye.values():
            pageEmploye.grid(row=0, column=0, sticky="nsew",padx=(5, 7), pady=7)


        #menu chef
        self.menuChef = ctk.CTkFrame(self.pagesSecondaire["gestions"], width=200)
        self.menuChef.grid_columnconfigure(0, weight=1)
        self.menuChef.grid_propagate(False)
        self.menuChef.grid(row=0, column=0, sticky="ns")

        ctk.CTkLabel(self.menuChef, text="menu").grid(row=0, column=0, padx=5, sticky="ew", pady=(10, 15))

        menuItem(self.menuChef, self, "categories", self.clientImagePath).pack(side="top", padx=5, pady=3, fill="x")
        menuItem(self.menuChef, self, "boissons", self.commandImagePath).pack(side="top", padx=5, pady=3, fill="x")
        menuItem(self.menuChef, self, "employes", self.bossImagePath).pack(side="top", padx=5, pady=3, fill="x")
        menuItem(self.menuChef, self, "stock", self.settingImagePath).pack(side="top", padx=5, pady=3, fill="x")
        menuItem(self.menuChef, self, "parametres", self.settingImagePath).pack(side="top", padx=5, pady=3, fill="x")
        menuItem(self.menuChef, self, "quitter", self.exitImagePath).pack(side="bottom", padx=5, pady=3, fill="x")

        self.chefContenu=ctk.CTkFrame(self.pagesSecondaire["gestions"])
        self.chefContenu.grid_columnconfigure(0, weight=1)
        self.chefContenu.grid_rowconfigure(0, weight=1)
        self.chefContenu.grid(row=0, column=1, sticky="nsew")

        self.pagesChef["boissons"] = BoissonPage(self.chefContenu, self)
        self.pagesChef["categories"] = CategoriePage(self.chefContenu, self)
        self.pagesChef["employes"] = EmployePage(self.chefContenu, self)
        self.pagesChef["stock"] = StockPage(self.chefContenu, self)
        for gestions in self.pagesChef.values():
            gestions.grid(row=0, column=0, sticky="nsew")

        self.pagesSecondaire["pageEmploye"].tkraise()  #mise en premier plan de la page des employes

    
    def chargerBoutonMenu(self):
        menuItem(self.menuEmploye, self, "clients", self.clientImagePath).pack(padx=3, pady=3, fill="x")
        menuItem(self.menuEmploye, self, "commandes", self.commandImagePath).pack(padx=3,pady=3, fill="x")
        if self.utilisateurType=="chef":
            menuItem(self.menuEmploye, self, "gestions", self.bossImagePath).pack(padx=3,pady=3, fill="x")
        menuItem(self.menuEmploye, self, "parametres", self.settingImagePath).pack(padx=3,pady=3, fill="x")
        menuItem(self.menuEmploye, self, "quitter", self.exitImagePath).pack(padx=3, pady=3, side="bottom", fill="x")




    def setTheme(self):
        # Basculer entre les modes clair et sombre
        current_mode = ctk.get_appearance_mode()
        print(current_mode)
        
        if current_mode == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
        print("done")


    def initPages(self):
        self.pages["commandes"] = CommandePage(self.contentEmploye, self)
        self.pages["clients"] = ClientPage(self.contentEmploye, self)
        self.pages["parametres"] = ParametrePage(self.contentEmploye, self)
        self.pages["gestions"] = GestionPage(self.contentEmploye, self)

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")
        self.pages["commandes"].tkraise()
        


    def loadImage(self, imagePath, size):
        return ctk.CTkImage(Image.open(imagePath), size=size)
    
    def changePage(self, pageName):
        if pageName == "quitter":
            self.quit()
        elif pageName in self.pagesPrimaire.keys():
            self.pagesPrimaire[pageName].tkraise()
        elif pageName in self.pagesSecondaire.keys():
            self.pagesSecondaire[pageName].tkraise()
        elif pageName in self.pagesEmploye.keys():
            self.pagesEmploye[pageName].tkraise()
        elif pageName in self.pagesChef.keys():
            self.pagesChef[pageName].tkraise()
        print(f"changing page to {pageName}")

    def remplaceBienvenue(self):
        time.sleep(1)
        self.changePage("connexion")


# Lancer l'application
APP()
