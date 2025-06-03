
import customtkinter as ctk
import color
from .content.profil import Profil
from .content.pembayaran import Pembayaran
from .content.riwayat_pembayaran import RiwayatPembayaran
from tkinter import *
from PIL import Image, ImageTk
import os

class Halaman2(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=color.gray)
        self.controller = controller
        # global color

        self.grid_columnconfigure(1, weight=1)  # kolom konten kanan
        self.grid_rowconfigure(1, weight=1)

        # Sidebar di kiri
        sidebar = ctk.CTkFrame(self, corner_radius=0, fg_color=color.white, width=300)
        sidebar.grid(row=1, column=0, sticky="ns", pady=0)
    
        # Solusi penting:
        sidebar.pack_propagate(False)
        sidebar.grid_propagate(False) 

        ctk.CTkLabel(sidebar, text="Navigasi", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        ctk.CTkButton(sidebar,anchor="w",hover_color=color.gray, fg_color=color.white, text="Profil", text_color=color.black, command=self.tampilkan_konten1).pack(pady=5, padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w",hover_color=color.gray, fg_color=color.white,text="Riwayat Tagihan",text_color=color.black, command=self.tampilkan_konten2).pack(pady=5,padx=5, fill="x")
        ctk.CTkButton(sidebar,anchor="w",hover_color=color.gray, fg_color=color.white,text="Pembayaran",text_color=color.black, command=self.tampilkan_konten3).pack(pady=5, padx=5, fill="x")

        # Toolbar di atas
        toolbar_r = ctk.CTkFrame(self, height=50, fg_color=color.white)
        toolbar_r.grid(row=0, column=1, sticky="nsew")
        toolbar_l = ctk.CTkFrame(self, height=50,corner_radius=0, fg_color=color.white)
        toolbar_l.grid(row=0, column=0, sticky="nsew", pady=0)

        btn_switch = ctk.CTkButton(toolbar_r, anchor="e", text="Switch", command=self.ke_tampilan_a)
        btn_switch.pack(pady=5, padx=5, fill="x")

        # Frame konten di kanan, isi akan diganti
        self.frame_konten = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_konten.grid(row=1, column=1, sticky="nsew", padx=(0, 200))

        # Inisialisasi dengan Konten1
        self.konten1 = Profil(self.frame_konten)
        self.konten2 = RiwayatPembayaran(self.frame_konten)
        self.konten3 = Pembayaran(self.frame_konten)

        # tampilkan konten pertama
        self.konten2.pack_forget()
        self.konten3.pack_forget()
        self.konten1.pack(fill="both", expand=True)

    def tampilkan_konten1(self):
        self.konten1.pack(fill="both", expand=True)
        self.konten2.pack_forget()
        self.konten3.pack_forget()

    def tampilkan_konten2(self):
        self.konten2.pack(fill="both", expand=True)
        self.konten1.pack_forget()
        self.konten3.pack_forget()

    def tampilkan_konten3(self):
        self.konten3.pack(fill="both", expand=True)
        self.konten1.pack_forget()
        self.konten2.pack_forget()

    def ke_tampilan_a(self):
        self.pack_forget()
        self.controller.tampilan_a.pack(fill="both", expand=True)

