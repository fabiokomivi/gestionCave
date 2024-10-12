"""import tkinter as tk
import customtkinter as ctk

# Fonction pour ouvrir la fenêtre fille
def open_child_window():
    # Création de la fenêtre fille
    child = ctk.CTkToplevel(root)
    child.geometry("300x200")
    child.title("Fenêtre Fille")

    # Attend que la fenêtre fille soit visible avant d'appliquer grab_set
    child.wait_visibility()  # Attendre que la fenêtre soit visible
    child.grab_set()  # Empêche toute interaction avec la fenêtre mère tant que la fille est ouverte
    child.focus()  # Donne le focus à la fenêtre fille

    # Ajout d'un bouton pour fermer la fenêtre fille
    close_button = ctk.CTkButton(child, text="Fermer", command=child.destroy)
    close_button.pack(pady=20)

    # Attend que la fenêtre fille soit fermée avant de redonner le contrôle à la fenêtre mère
    root.wait_window(child)

# Initialisation de la fenêtre mère
root = ctk.CTk()
root.geometry("400x300")
root.title("Fenêtre Mère")

# Bouton pour ouvrir la fenêtre fille
open_button = ctk.CTkButton(root, text="Ouvrir la Fenêtre Fille", command=open_child_window)
open_button.pack(pady=20)

root.mainloop()
"""
"""import tkinter as tk

def submit_data():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    print(f"Nom: {nom}, Prénom: {prenom}")
    child_window.destroy()  # Ferme la fenêtre fille

def open_child_window():
    global child_window, entry_nom, entry_prenom
    child_window = tk.Toplevel(root)
    child_window.title("Fenêtre Fille")
    child_window.geometry("250x150")
    
    tk.Label(child_window, text="Nom:").pack()
    entry_nom = tk.Entry(child_window)
    entry_nom.pack()
    
    tk.Label(child_window, text="Prénom:").pack()
    entry_prenom = tk.Entry(child_window)
    entry_prenom.pack()
    
    tk.Button(child_window, text="Soumettre", command=submit_data).pack()
    
    child_window.grab_set()  # Récupère le focus sur la fenêtre fille

# Fenêtre principale
root = tk.Tk()
root.geometry("300x200")
root.title("Fenêtre Mère")

button = tk.Button(root, text="Ouvrir la fenêtre fille", command=open_child_window)
button.pack(pady=20)

root.mainloop()
"""
"""
import tkinter as tk
from tkinter import simpledialog

class FenetreFille(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Fenêtre Fille")
        self.geometry("250x150")
        
        # Champs pour le nom et le prénom
        tk.Label(self, text="Nom:").pack()
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack()

        tk.Label(self, text="Prénom:").pack()
        self.entry_prenom = tk.Entry(self)
        self.entry_prenom.pack()
        
        # Bouton de soumission
        tk.Button(self, text="Soumettre", command=self.submit_data).pack()
        
        # Empêche l'accès à la fenêtre mère
        self.grab_set()

    def submit_data(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        print(f"Nom: {nom}, Prénom: {prenom}")
        self.parent.update()
        self.destroy()  # Ferme la fenêtre fille

class FenetreMere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Fenêtre Mère")

        # Bouton pour ouvrir la fenêtre fille
        tk.Button(self, text="Ouvrir la fenêtre fille", command=self.open_child_window).pack(pady=20)

        self.label = tk.Label(self, text="", width=150)
        self.label.pack()

    def update(self):
        self.label.configure(text="toto+lale")

    def open_child_window(self):
        FenetreFille(self)

if __name__ == "__main__":
    app = FenetreMere()
    app.mainloop()
"""
"""import tkinter as tk

class FenetreFille(tk.Toplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.title("Fenêtre Fille")
        self.geometry("250x150")

        # Fonction de rappel à appeler pour transmettre les données
        self.callback = callback

        # Champs pour le nom et le prénom
        tk.Label(self, text="Nom:").pack()
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack()

        tk.Label(self, text="Prénom:").pack()
        self.entry_prenom = tk.Entry(self)
        self.entry_prenom.pack()
        
        # Bouton de soumission
        tk.Button(self, text="Soumettre", command=self.submit_data).pack()

        # Empêche l'accès à la fenêtre mère
        self.grab_set()

    def submit_data(self):
        # Récupère les valeurs des champs
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()

        # Appelle la fonction de rappel pour passer les données à la fenêtre mère
        self.callback(nom, prenom)

        # Ferme la fenêtre fille
        self.destroy()

class FenetreMere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Fenêtre Mère")

        # Label pour afficher les informations reçues de la fenêtre fille
        self.label_info = tk.Label(self, text="Informations: ")
        self.label_info.pack(pady=20)

        # Bouton pour ouvrir la fenêtre fille
        tk.Button(self, text="Ouvrir la fenêtre fille", command=self.open_child_window).pack(pady=20)

    def open_child_window(self):
        # Ouvre la fenêtre fille et lui passe la fonction de rappel pour récupérer les données
        FenetreFille(self, self.receive_data)

    def receive_data(self, nom, prenom):
        # Fonction appelée par la fenêtre fille pour transmettre les données
        self.label_info.config(text=f"Nom: {nom}, Prénom: {prenom}")

if __name__ == "__main__":
    app = FenetreMere()
    app.mainloop()"""
"""import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.entry = tk.Entry(self, fg='grey')
        self.entry.insert(0, "Nom")  # Ajouter le placeholder au démarrage
        self.entry.pack(pady=20)

        # Associer les événements focus pour gérer l'affichage du texte
        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_focusout)

    def on_entry_click(self, event):
        if self.entry.get() == "Nom":
            self.entry.delete(0, "end")  # Efface le placeholder
            self.entry.config(fg='black')

    def on_focusout(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, "Nom")  # Remet le placeholder si vide
            self.entry.config(fg='grey')

if __name__ == "__main__":
    app = App()
    app.mainloop()
"""
"""import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

# Créer la fenêtre principale
root = tk.Tk()
root.title("Affichage d'images dans un Treeview")
root.geometry("400x300")

# Créer un Treeview
tree = ttk.Treeview(root)

# Créer une colonne
tree["columns"] = ("Nom")

# Configurer les colonnes
tree.column("#0", width=100, minwidth=50)  # Colonne pour afficher les images
tree.column("Nom", width=200, minwidth=100)

# Configurer les en-têtes
tree.heading("#0", text="Image")
tree.heading("Nom", text="Nom")

# Charger des images
img1 = PhotoImage(file="ctkAPP/images/employe.png")  # Remplacer par le chemin de votre image
img2 = PhotoImage(file="ctkAPP/images/employe.png")

# Insérer des éléments avec des images dans le Treeview
tree.insert("", "end", text="Item 1", image=img1, values=("Image 1"))
tree.insert("", "end", text="Item 2", image=img2, values=("Image 2"))

# Placer le Treeview dans la fenêtre
tree.pack(pady=20)

# Démarrer la boucle principale
root.mainloop()"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def creer_facture_pdf(commande, client, lignes_commandes):
    # Chemin du fichier PDF
    file_name = f"facture_{commande.id}.pdf"
    
    # Créer un fichier PDF
    pdf = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4
    
    # Titre de la facture
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(100, 750, "FACTURE")
    
    # Informations du client
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 700, f"Client : {client.nom} {client.prenom}")
    pdf.drawString(50, 685, f"Adresse : {client.addresse}")
    pdf.drawString(50, 670, f"Téléphone : {client.telephone}")
    
    # Informations de la commande
    pdf.drawString(50, 640, f"Commande n° : {commande.id}")
    pdf.drawString(50, 625, f"Date : {commande.dateCommande.strftime('%d/%m/%Y')}")

    # Créer un tableau pour les lignes de commande
    data = [["Produit", "Quantité", "Prix Unitaire", "Total"]]
    
    for ligne in lignes_commandes:
        produit = ligne.boisson.nom
        quantite = ligne.quantite
        prix_unitaire = ligne.boisson.prix
        total = quantite * prix_unitaire
        data.append([produit, quantite, prix_unitaire, total])
    
    # Ajouter un total général
    total_general = sum(ligne.quantite * ligne.boisson.prix for ligne in lignes_commandes)
    data.append(["", "", "Total Général", total_general])
    
    # Créer un tableau avec les données
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Définir la position du tableau
    table.wrapOn(pdf, width, height)
    table.drawOn(pdf, 50, 500)
    
    # Terminer le PDF
    pdf.save()

    print(f"Facture PDF générée : {file_name}")

# Exemple d'appel
# commande, client, et lignes_commandes doivent être des objets correspondant à ta base de données
creer_facture_pdf(commande, client, lignes_commandes)

