
import customtkinter as ctk
from .content.profil import Profil
from .content.pembayaran import Pembayaran
from .content.riwayat_tagihan import RiwayatTagihan

class Halaman2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)  # kolom konten kanan
        self.grid_rowconfigure(0, weight=1)

        # Sidebar di kiri
        sidebar = ctk.CTkFrame(self, width=300)
        sidebar.grid(row=0, column=0, sticky="ns")

        # Solusi penting:
        sidebar.pack_propagate(False)
        sidebar.grid_propagate(False) 

        ctk.CTkLabel(sidebar, text="Navigasi", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        ctk.CTkButton(sidebar,anchor="w", text="Profil", command=self.tampilkan_konten1).pack(pady=5, padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w", text="Riwayat Tagihan", command=self.tampilkan_konten2).pack(pady=5,padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w", text="Pembayaran", command=self.tampilkan_konten3).pack(pady=5, padx=5, fill="x")

        # Frame konten di kanan, isi akan diganti
        self.frame_konten = ctk.CTkFrame(self)
        self.frame_konten.grid(row=0, column=1, sticky="nsew")

        # Inisialisasi dengan Konten1
        self.konten1 = Profil(self.frame_konten)
        self.konten2 = RiwayatTagihan(self.frame_konten)
        self.konten3 = Pembayaran(self.frame_konten)

        self.konten1.pack(fill="both", expand=True)

    def tampilkan_konten1(self):
        self.konten2.pack_forget()
        self.konten3.pack_forget()
        self.konten1.pack(fill="both", expand=True)

    def tampilkan_konten2(self):
        self.konten1.pack_forget()
        self.konten3.pack_forget()
        self.konten2.pack(fill="both", expand=True)

    def tampilkan_konten3(self):
        self.konten1.pack_forget()
        self.konten2.pack_forget()
        self.konten3.pack(fill="both", expand=True)

