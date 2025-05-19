import customtkinter as ctk

class Tagihan(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="Ini Konten profil", font=ctk.CTkFont(size=18)).pack(padx=20, pady=20)
