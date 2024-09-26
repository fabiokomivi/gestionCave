
import customtkinter as ctk 
from PIL import Image

class CoverImageApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cover Image Example")
        self.geometry("800x600")
        
        # Charger l'image à partir d'un fichier
        self.image = ctk.CTkImage(Image.open("/home/fabio/Bureau/python/appCTKenv/ctkAPP/images/settings.png"))
        
        # Créer un label pour afficher l'image
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(fill="both", expand=True)
        
        # Ajuster l'image au redimensionnement de la fenêtre
        self.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        # Calculer les dimensions à partir de la taille de la fenêtre
        window_width = event.width
        window_height = event.height
        
        # Redimensionner l'image tout en gardant le ratio d'aspect
        resized_image = self.image._size((window_width, window_height), Image.Resampling.LANCZOS)
        
        # Convertir l'image en format compatible avec Tkinter
        self.cover_image = ImageTk.PhotoImage(resized_image)
        
        # Mettre à jour l'image du label
        self.image_label.configure(image=self.cover_image)

if __name__ == "__main__":
    app = CoverImageApp()
    app.mainloop()
