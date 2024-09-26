import customtkinter as ctk
from PIL import Image

class BienvenuePage(ctk.CTkFrame):
    vinImage = ctk.CTkImage(Image.open("/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/bgimg1.png"), size=(500, 200))
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white")
        ctk.CTkLabel(self, text="bienvenue").grid(row=0, column=0)
        ctk.CTkLabel(self, text="EGATE CELLAR", font=("Arial", 55), text_color="black").grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(self, text="", width=300, image=self.vinImage).grid(row=0, column=1, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)



