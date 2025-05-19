import customtkinter as ctk

class Halaman1(ctk.CTkFrame):
    def __init__(self, master, kembali):
        super().__init__(master)

        ctk.CTkLabel(self, text="Ini Halaman 2").pack(pady=20)
        ctk.CTkButton(self, text="Kembali ke Halaman 1", command=kembali).pack()


 