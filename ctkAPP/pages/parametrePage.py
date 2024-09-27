import customtkinter as ctk
ctk.set_default_color_theme("/home/fabio/Bureau/python/appCTKenv/ctkAPP/themes/myBlue.json")  # Thème bleue

class ParametrePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text="settting").grid(row=0, column=0)
        self.switch = ctk.CTkSwitch(self, text="dark", command=controller.setTheme)
        self.switch.grid(row=1, column=0)
        self.button = ctk.CTkButton(self, text="dark", command=controller.setTheme)
        self.button.grid(row=2, column=0)
        ctk.CTkLabel(self, text="test").grid(column=0, row=3)
        ctk.CTkLabel(self, text="test2").grid(column=0, row=4)