import customtkinter as ctk

class Pembayaran(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="white")
        self.pack(padx=20, pady=20, fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Header
        ctk.CTkLabel(self, text="Biaya Kuliah", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=10, pady=(10, 5))

        # Tabs
        tab_frame = ctk.CTkFrame(self, fg_color="transparent")
        tab_frame.pack(fill="x", padx=10)
        for tab in ["Tagihan", "Riwayat Pembayaran", "Rekap Pembayaran"]:
            ctk.CTkButton(tab_frame, text=tab, width=140).pack(side="left", padx=5)

        # Informasi Tagihan
        info_frame = ctk.CTkFrame(self)
        info_frame.pack(pady=10, padx=10, fill="x")

        infos = [
            ("Total Tunggakan", "Rp 4.250.000"),
            ("Syarat KRS", "Rp 1.750.000"),
            ("Syarat UTS", "Rp 400.000"),
            ("Syarat UAS", "Rp 400.000")
        ]

        for label, value in infos:
            box = ctk.CTkFrame(info_frame, width=150, height=70)
            box.pack(side="left", padx=5, pady=5, expand=True, fill="both")
            ctk.CTkLabel(box, text=label).pack()
            ctk.CTkLabel(box, text=value, font=ctk.CTkFont(size=14, weight="bold")).pack()

        # Informasi Peringatan
        ctk.CTkLabel(self, text="Anda wajib melunasi tagihan di semester sebelumnya jika masih ada tunggakan", text_color="white", fg_color="#007bff", corner_radius=6, height=30).pack(fill="x", padx=10, pady=10)

        # Daftar Tagihan
        self.add_semester_section("Semester 5", [
            ("Ujian susulan", "2019/2020 Ganjil", "Rp300.000", "300.000"),
            ("Ujian susulan lagi", "2019/2020 Ganjil", "Rp300.000", "300.000")    
        ])
        self.add_semester_section("Semester 6", [
            ("BPP Pokok SP", "2019/2020 Genap sekali", "Rp1.350.000", "1.350.000"),
            ("Biaya Bulanan", "2019/2020 Genap", "Rp400.000", "0")
        ])

        # Total & Tombol
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(bottom_frame, text="Total tunggakan yang akan dibayarkan", font=ctk.CTkFont(weight="bold")).pack(side="left")
        ctk.CTkLabel(bottom_frame, text="Rp 1.650.000", font=ctk.CTkFont(size=14, weight="bold"), text_color="#28a745").pack(side="left", padx=10)
        ctk.CTkButton(bottom_frame, text="Pilih metode pembayaran", fg_color="#007bff", hover_color="#0056b3").pack(side="right")

    def add_semester_section(self, title, items):
        section = ctk.CTkFrame(self, fg_color="#f8f9fa", corner_radius=10)
        section.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(section, text=title, font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=10, pady=5)

        for item in items:
            frame = ctk.CTkFrame(section, fg_color="white", corner_radius=8)
            frame.pack(fill="x", padx=10, pady=5)

            ctk.CTkCheckBox(frame, width=300, text=item[0]).pack(side="left", padx=5)
            ctk.CTkLabel(frame,anchor="w", width=300, text=item[1]).pack(side="left", padx=5)
            ctk.CTkLabel(frame,anchor="w", width=300, text=item[2]).pack(side="left", padx=5)
            ctk.CTkEntry(frame, width=150, placeholder_text="Jumlah Bayar", justify="right").pack(side="left", padx=5)
            ctk.CTkButton(frame, text="Tunggakan", width=100).pack(side="right", padx=10)


# class Aplikasi(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistem Informasi Akademik - Pembayaran")
#         self.geometry("1000x700")
#         self.resizable(False, False)
#         Pembayaran(self)



