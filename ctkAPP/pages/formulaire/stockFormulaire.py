import customtkinter as ctk
from tkinter import filedialog
from controleur.boissonControler import *
from .erreur.erreur import erreur
from PIL import Image
import re

class stockForm(ctk.CTkToplevel):

    patternQuantite = r"[0-9]+"

    def __init__(self, parent, callback, information):
        super().__init__(parent)
        self.geometry("360x160")
        self.protocol("WM_DELETE_WINDOW", self.fermetureAnormale)

        self.callback=callback

        self.title(information)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        topFrame = ctk.CTkFrame(self)
        
                
        topFrame.grid_columnconfigure(0, weight=0)
        topFrame.grid_columnconfigure(1, weight=1)
        topFrame.rowconfigure(0, weight=1)
        
        topFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(topFrame, text=f"ajout de {information}").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        ctk.CTkLabel(topFrame, text="quantite:").grid(row=1, column=0,padx=(25, 5), pady=10)
        self.entreeQuantite = ctk.CTkEntry(topFrame, width=150, placeholder_text="quantite")
        
        self.entreeQuantite.grid(row=1, column=1, padx=5, pady=10)
        
        confirmationFrame= ctk.CTkFrame(topFrame)
        confirmationFrame.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        ctk.CTkButton(confirmationFrame, text="annuler", fg_color="red", command=self.destroy).pack(side="left", padx=10, pady=5)
        ctk.CTkButton(confirmationFrame, text="valider", fg_color="green", command=self.verification).pack(side="right", padx=10, pady=5)

        self.wait_visibility()
        self.grab_set()

    def verification(self):
        quantite = self.entreeQuantite.get()
        if not re.match(self.patternQuantite, quantite):
            self.rougir(self.entreeQuantite)
        else:
            self.callback(int(quantite))
            self.destroy()

    def fermetureAnormale(self):
        self.callback(0)
        self.destroy()

    def rougir(self, widget):
        widget.configure(fg_color = "red")
        self.after(1500, lambda:self.blanchir(widget))

    def blanchir(self, widget):
        widget.configure(fg_color="white")
   
