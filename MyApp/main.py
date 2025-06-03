import customtkinter as ctk
from view.mahasiswa.mahasiswa_view import Halaman2
from view.admin.admin_view import Halaman1
import color
import os
from PIL import Image, ImageTk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pindah Tampilan Pakai pack_forget()")
        self.geometry("800x500")
        
        self.tampilan_a = Halaman1(self, self)
        self.tampilan_b = Halaman2(self, self)

        # Mulai dengan menampilkan tampilan A
        self.tampilan_b.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = Main()
    app.mainloop()