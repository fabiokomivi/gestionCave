import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bouton avec limite de taille")
        self.geometry("400x300")
        
        # Limiter la taille de la fenêtre (optionnel)
        self.maxsize(500, 400)
        
        # Configuration de la grille
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Création d'un bouton avec une taille maximale
        self.bouton = ctk.CTkButton(self, text="Bouton", width=200, height=100)
        
        # Positionnement du bouton avec des marges
        self.bouton.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Ajuster la grille pour que le bouton ne prenne pas tout l'espace
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()
