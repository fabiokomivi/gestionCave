import customtkinter as ctk
import tkinter as tk
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class BoissonPage(ctk.CTkFrame):

    boissonAttribue = ("nom", "categorie", "prix", "disponibilité")

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

        ctk.CTkButton(controlFrame, text="nouveau", width=100).grid(row=0, column=0)
        ctk.CTkButton(controlFrame, text="modifier", width=100).grid(row=1, column=0)
        ctk.CTkButton(controlFrame, text="supprimer", width=100).grid(row=2, column=0)

        for i in range(3):
            rechercheFramne.grid_rowconfigure(i, weight=1)
        rechercheFramne.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(rechercheFramne, text="recherche").grid(column=0, row=0)
        ctk.CTkComboBox(rechercheFramne, values=self.boissonAttribue).grid(column=0, row=1)
        self.rechercher = ctk.CTkEntry(rechercheFramne)

        self.rechercher.grid(column=0, row=2)

    def surSelection(self, event):
        print("selectionner")
