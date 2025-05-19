import customtkinter as ctk
from view.mahasiswa.mahasiswa_view import Halaman2

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("700x400")
root.title("Aplikasi dengan Halaman")

# Buat dan tampilkan Halaman2
halaman1 = Halaman2(root)
halaman1.pack(fill="both", expand=True)

root.mainloop()
