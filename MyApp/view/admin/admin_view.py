
import customtkinter as ctk
from .content.jenis_tagihan import JenisTagihan
from .content.pembayaran import Pembayaran
from .content.laporan import Laporan
from .content.mahasiswa_view import Mahasiswa
from .content.metode_pembayaran import MetodePembayaran
from .content.tagihan import Tagihan

class Halaman1(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.grid_columnconfigure(1, weight=1)  # kolom konten kanan
        self.grid_rowconfigure(0, weight=1)

        # Sidebar di kiri
        sidebar = ctk.CTkFrame(self, width=300)
        sidebar.grid(row=0, column=0, sticky="ns")

        # Solusi penting:
        sidebar.pack_propagate(False)
        sidebar.grid_propagate(False)

        btn_switch = ctk.CTkButton(sidebar, anchor="e", text="Switch", command=self.ke_tampilan_b)
        btn_switch.pack(pady=5, padx=5, fill="x") 

        ctk.CTkLabel(sidebar, text="Navigasi", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        ctk.CTkButton(sidebar,anchor="w", text="Mahasiswa", command=self.tampilkan_konten1).pack(pady=5, padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w", text="Jenis Tagihan", command=self.tampilkan_konten2).pack(pady=5,padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w", text="Tagihan", command=self.tampilkan_konten3).pack(pady=5, padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w", text="Pembayaran", command=self.tampilkan_konten4).pack(pady=5, padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w", text="Metode Pembayaran", command=self.tampilkan_konten5).pack(pady=5, padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w", text="Laporan", command=self.tampilkan_konten6).pack(pady=5, padx=5, fill="x")

        # Frame konten di kanan, isi akan diganti
        self.frame_konten = ctk.CTkFrame(self)
        self.frame_konten.grid(row=0, column=1, sticky="nsew")

        # Inisialisasi dengan Konten1
        self.konten1 = Mahasiswa(self.frame_konten)
        self.konten2 = JenisTagihan(self.frame_konten)
        self.konten3 = Tagihan(self.frame_konten)
        self.konten4 = Pembayaran(self.frame_konten)
        self.konten5 = MetodePembayaran(self.frame_konten)
        self.konten6 = Laporan(self.frame_konten)

        self.konten1.pack(fill="both", expand=True)

    def tampilkan_konten1(self):
        self.konten2.pack_forget()
        self.konten3.pack_forget()
        self.konten4.pack_forget()
        self.konten5.pack_forget()
        self.konten6.pack_forget()
        self.konten1.pack(fill="both", expand=True)

    def tampilkan_konten2(self):
        self.konten1.pack_forget()
        self.konten3.pack_forget()
        self.konten4.pack_forget()
        self.konten5.pack_forget()
        self.konten6.pack_forget()
        self.konten2.pack(fill="both", expand=True)

    def tampilkan_konten3(self):
        self.konten2.pack_forget()
        self.konten1.pack_forget()
        self.konten4.pack_forget()
        self.konten5.pack_forget()
        self.konten6.pack_forget()
        self.konten3.pack(fill="both", expand=True)

    def tampilkan_konten4(self):
        self.konten2.pack_forget()
        self.konten3.pack_forget()
        self.konten1.pack_forget()
        self.konten5.pack_forget()
        self.konten6.pack_forget()
        self.konten4.pack(fill="both", expand=True)

    def tampilkan_konten5(self):
        self.konten2.pack_forget()
        self.konten3.pack_forget()
        self.konten4.pack_forget()
        self.konten1.pack_forget()
        self.konten6.pack_forget()
        self.konten5.pack(fill="both", expand=True)

    def tampilkan_konten6(self):
        self.konten2.pack_forget()
        self.konten3.pack_forget()
        self.konten4.pack_forget()
        self.konten5.pack_forget()
        self.konten1.pack_forget()
        self.konten6.pack(fill="both", expand=True)

    def ke_tampilan_b(self):
        self.pack_forget()
        self.controller.tampilan_b.pack(fill="both", expand=True)
 