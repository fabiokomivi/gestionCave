import tkinter as tk

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