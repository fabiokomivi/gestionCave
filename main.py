"""import tkinter as tk
from tkinter import ttk

# Fonction pour forcer la sélection d'une ligne fixe
def on_select(event):
    # Obtenir l'élément sélectionné
    selected_item = tree.selection()
    
    # Comparer avec l'élément fixe
    if selected_item and selected_item[0] != fixed_row_id:
        # Forcer la sélection sur la ligne fixe
        tree.selection_set(fixed_row_id)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Treeview Example")

# Créer un Treeview avec deux colonnes
tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# Ajouter des données au Treeview
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
for index, (name, age) in enumerate(data):
    tree.insert("", "end", iid=index, values=(name, age))

# Forcer la sélection sur la première ligne (ligne fixe)
fixed_row_id = "1"
tree.selection_set(fixed_row_id)

# Binding pour forcer la sélection sur la ligne fixe
tree.bind("<<TreeviewSelect>>", on_select)

# Pack le Treeview
tree.pack()
print(enumerate(data))

# Lancer la boucle principale
root.mainloop()
"""
"""
import customtkinter as ctk

class FenetreFille(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Fenêtre Fille")
        self.geometry("400x300")

        # Ajoute des widgets ici
        label = ctk.CTkLabel(self, text="Je suis la fenêtre fille")
        label.pack(pady=20)
        self.wait_visibility()

        # Empêche toute interaction avec la fenêtre mère
        self.transient(parent)  # Place la fenêtre fille au-dessus de la fenêtre mère
        self.grab_set_global()  # Capture tous les événements d'entrée pour la fenêtre fille globalement
        self.focus()  # Assure que la fenêtre fille a le focus

class FenetreMere(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fenêtre Mère")
        self.geometry("500x400")

        bouton = ctk.CTkButton(self, text="Ouvrir Fenêtre Fille", command=self.ouvrir_fenetre_fille)
        bouton.pack(pady=50)

    def ouvrir_fenetre_fille(self):
        # Crée une nouvelle fenêtre fille
        FenetreFille(self)

if __name__ == "__main__":
    app = FenetreMere()
    app.mainloop()
"""


"""def centreFenetre(self):

        pere_x = self.master.winfo_x()
        pere_y = self.master.winfo_y()
        pere_largeur = self.master.winfo_width()
        pere_hauter = self.master.winfo_height()

        enfant_largeur = self.winfo_reqwidth()
        enfant_hauteur = self.winfo_reqheight()

        position_x = pere_x + (pere_largeur // 2) - (enfant_largeur // 2)
        position_y = pere_y + (pere_hauter // 2) - (enfant_hauteur // 2)

        self.geometry(f"+{position_x}+{position_y}")

def infoTaille(self):
     print(f"{self.winfo_width()}, {self.winfo_height()}")"""
import customtkinter as ctk

class PasswordEntry(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=10, pady=10)

        self.password_var = ctk.StringVar()

        self.entry = ctk.CTkEntry(self, show="*", textvariable=self.password_var)
        self.entry.pack(side="left", padx=(0, 10))

        self.toggle_button = ctk.CTkButton(self, text="👁️", command=self.toggle_password_visibility)
        self.toggle_button.pack(side="left")

    def toggle_password_visibility(self):
        if self.entry.cget("show") == "*":
            self.entry.configure(show="")
            self.toggle_button.configure(text="👁️‍🗨️")  # change the button icon if you want
        else:
            self.entry.configure(show="*")
            self.toggle_button.configure(text="👁️")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"
    
    root = ctk.CTk()
    root.title("Password Entry with Eye Icon")

    PasswordEntry(root)

    root.mainloop()
