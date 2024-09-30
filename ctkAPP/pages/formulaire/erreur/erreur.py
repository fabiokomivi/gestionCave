import customtkinter as ctk

class erreur(ctk.CTkToplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        parent.update_idletasks()  # Assure que la géométrie est à jour
        frame = ctk.CTkFrame(self)
        frame.pack(padx=3, pady=3)
        ctk.CTkLabel(frame, text=message).grid(column=0, row=0, padx=3, pady=0)
        ctk.CTkButton(frame, text="ok", command=self.destroy).grid(column=0, row=1, padx=3, pady=0)
        self.wait_visibility()

        self.grab_set()

        self.after(3000, self.destroy)
