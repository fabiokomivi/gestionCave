import customtkinter as ctk
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class ConnexionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.connexionFrame = ctk.CTkFrame(self, height=500, width=500)
        self.connexionFrame.grid_propagate(False)
        self.connexionFrame.grid(row=0, column=0, pady=100)

        for i in range(3):
            self.connexionFrame.grid_rowconfigure(i, weight=1)
        self.connexionFrame.grid_columnconfigure(0, weight=1)
        

        ctk.CTkLabel(self.connexionFrame, text="connexion", height=100, width=150, fg_color="green").grid(row=0, column=0, padx=20, sticky="ew")
        self.userEntree = ctk.CTkEntry(self.connexionFrame, placeholder_text="utilisateur", height=10)
        self.userEntree.grid(row=1, column=0, sticky="nsew", padx=20, pady=(30, 10))
        self.mpdEntree = ctk.CTkEntry(self.connexionFrame, placeholder_text="mot de passe", height=30)
        self.mpdEntree.grid(row=2, column=0, sticky="nsew", padx=20, pady=(10, 30))
        