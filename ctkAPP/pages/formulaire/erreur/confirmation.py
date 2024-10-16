import customtkinter as ctk

class Confirmation(ctk.CTkToplevel):
    def __init__(self, parent, message, callback):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.fermetureAnormale)
        self.callback = callback
        frame = ctk.CTkFrame(self)
        frame.pack(padx=3, pady=3)

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(frame, text=message, corner_radius=10, fg_color="#AA7590").grid(column=0, row=0, columnspan=2, padx=3, pady=10)
        ctk.CTkButton(frame, text="continuer", fg_color="red", command=self.accepter).grid(column=1, row=1, padx=3, pady=0)
        ctk.CTkButton(frame, text="arreter", fg_color="green", command=self.decliner).grid(column=0, row=1, padx=3, pady=0)

        self.wait_visibility()

        self.grab_set()

    def accepter(self):
        self.callback(True)
        self.destroy()

    def decliner(self):
        self.callback(False)
        self.destroy()


    def fermetureAnormale(self):
        self.callback(False)
        self.destroy()
