import customtkinter as ctk

def ouvrir_fenetre_fille():
    # Masquer la fenêtre mère
    root.withdraw()  # Masquer la fenêtre mère

    # Créer une fenêtre fille
    fenetre_fille = ctk.CTk()
    fenetre_fille.title("Fenêtre Fille")

    # Ajouter un bouton pour fermer la fenêtre fille
    bouton_fermer = ctk.CTkButton(fenetre_fille, text="Fermer", command=lambda: fermer_fenetre(fenetre_fille))
    bouton_fermer.pack(pady=20)

    # Lancer la boucle principale de la fenêtre fille
    fenetre_fille.mainloop()

def fermer_fenetre(fenetre_fille):
    fenetre_fille.destroy()
    root.deiconify()  # Réafficher la fenêtre mère

# Créer la fenêtre principale
root = ctk.CTk()
root.title("Fenêtre Mère")

# Ajouter un bouton pour ouvrir la fenêtre fille
bouton_ouvrir = ctk.CTkButton(root, text="Ouvrir Fenêtre Fille", command=ouvrir_fenetre_fille)
bouton_ouvrir.pack(pady=20)

# Lancer la boucle principale de la fenêtre mère
root.mainloop()
