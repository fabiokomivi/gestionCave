import customtkinter as ctk
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class CommandePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ctk.CTkLabel(self, text="commande").grid(row=0, column=0)