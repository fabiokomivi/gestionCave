import customtkinter as ctk
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class ClientPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        #test
        ctk.CTkLabel(self, text="client").grid(row=0, column=0)
