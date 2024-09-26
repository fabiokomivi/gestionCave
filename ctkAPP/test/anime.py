import customtkinter as ctk
import time

class AnimatedFrame(ctk.CTkFrame):
    def __init__(self, parent, text, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.text = text
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.animate_text()

    def animate_text(self):
        full_text = self.text
        current_text = ""
        index = 0

        def update_text():
            nonlocal index, current_text
            if index < len(full_text):
                current_text += full_text[index]
                self.label.configure(text=current_text)
                index += 1
            else:
                # Réinitialiser pour recommencer l'animation en boucle
                current_text = ""
                index = 0
            self.after(150, update_text)

        update_text()

# Exécution de l'exemple
if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("400x200")

    frame = AnimatedFrame(app, text="Bonjour, bienvenue dans l'animation de texte!")
    frame.grid(row=0, column=0, padx=20, pady=20)

    app.mainloop()
