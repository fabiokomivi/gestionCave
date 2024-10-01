import customtkinter as ctk

class boissonForm(ctk.CTkToplevel):
    def __init__(self, parent, callback, mode, information):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        topFrame = ctk.CTkFrame(self)
        for i in range(5):
            if i == 0:
                topFrame.grid_rowconfigure(i, weight=0)
            else:
                topFrame.grid_rowconfigure(i, weight=1)
                
        topFrame.grid_columnconfigure(0, weight=0)
        topFrame.grid_columnconfigure(1, weight=1)
        
        topFrame.grid(row=0, column=0, sticky="nsew")
        photoLabel = ctk.CTkLabel(topFrame, width=150, height=150)
        entreeNom = ctk.CTkEntry(topFrame, width=150, placeholder_text="nom")
        entreePrix = ctk.CTkEntry(topFrame, width=150, placeholder_text="prix")
        selecteur = ctk.CTkComboBox(topFrame, width=150)
        entreeDescription = ctk.CTkTextbox(topFrame)
        boutonValider = ctk.CTkButton(topFrame, text="selectionner")
        photoLabel.grid(column=0, row=0, rowspan=3)
        entreeNom.grid(row=0, column=1)
        entreePrix.grid(row=1, column=1)
        selecteur.grid(row=2, column=1)
        boutonValider.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        entreeDescription.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5)
        self.mainloop()


boissonForm(ctk.CTk(), None, None, None)