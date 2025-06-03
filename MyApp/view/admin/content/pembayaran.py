
import customtkinter as ctk
from PIL import Image
import color
import os

ctk.set_appearance_mode("light")  # light or dark
ctk.set_default_color_theme("blue")


class Pembayaran(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=color.gray)
        self.pack(fill="both", expand=True)

        # Load icons (pastikan file gambar ada di folder yang sama)
        folder_path = os.path.join(os.path.dirname(__file__), "folder.png")
        exe_path = os.path.join(os.path.dirname(__file__), "exe.png")
        self.folder_icon = ctk.CTkImage(Image.open(folder_path), size=(32, 32))
        self.excel_icon = ctk.CTkImage(Image.open(exe_path), size=(32, 32))

        self.create_widgets()

    def create_widgets(self):
        
        base_frame_scroll = ctk.CTkScrollableFrame(self, fg_color=color.gray)
        base_frame_scroll.pack(fill="both", expand=True, padx=(0, 200))
        base_frame_scroll._scrollbar.grid_remove()

        # Header
        header_frame = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        header_frame.pack(fill="x", pady=10, padx=10)

        upload_btn = ctk.CTkButton(header_frame, text="Upload")
        upload_btn.pack(side="left", padx=5)

        create_btn = ctk.CTkButton(header_frame, text="Create +")
        create_btn.pack(side="left", padx=5)

        search_entry = ctk.CTkEntry(header_frame, placeholder_text="Search")
        search_entry.pack(side="right", padx=5)

        # Folder section
        folder_frame = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        folder_frame.pack(fill="x", expand=True, padx=0)

        folder_label = ctk.CTkLabel(folder_frame, text="Pembayaran Mahasiswa", font=ctk.CTkFont(size=22, weight="bold"))
        folder_label.pack(anchor="w", padx=10, pady=5)

        folders_grid = ctk.CTkFrame(folder_frame, fg_color="transparent")
        folders_grid.pack(pady=0, fill="x", expand=True)

        data_pembayaran = [
            ("Pembayaran Semester Ganjil", "Rp 80.000.000"),
            ("Pembayaran Semester Genap", "Rp 45.000.000"),
            ("Pembayaran Kelas Reguler", "Rp 100.000.000"),
            ("Pembayaran Kelas Karyawan", "Rp 25.000.000"),
            ("Pembayaran SPP", "Rp 90.000.000"),
            ("Pembayaran Lain-lain", "Rp 10.000.000"),
        ]

        data_riwayat_pemabayaran = [
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Pending"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Pending"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Pending"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
            ("#23456", "23 Jan 2023", "Basic Plan", "spp", "1.999.888", "29.299", "Paid"),
        ]


        for col in range(3):
            folders_grid.grid_columnconfigure(col, weight=1)

        for index, (nama, jumlah) in enumerate(data_pembayaran):
            i = index // 3
            j = index % 3

            folder = ctk.CTkFrame(folders_grid, fg_color=color.white, height=120, corner_radius=16, border_width=1)
            folder.grid(row=i, column=j, padx=10, pady=10, sticky="we")
            folder.pack_propagate(False)

            icon_label = ctk.CTkLabel(folder, image=self.folder_icon, text="")
            icon_label.pack(pady=(10, 5))

            # Nama pembayaran (teks atas)
            nama_label = ctk.CTkLabel(folder, text=nama, font=ctk.CTkFont(size=13, weight="bold"), justify="center", wraplength=130)
            nama_label.pack()

            # Jumlah pembayaran (teks bawah)
            jumlah_label = ctk.CTkLabel(folder, text=jumlah, font=ctk.CTkFont(size=12), justify="center")
            jumlah_label.pack()

        # Recent files section
        recent_header = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        recent_header.pack(fill="x", padx=10, pady=(10, 0))

        # Label Recent di kiri
        recent_label = ctk.CTkLabel(recent_header, text="Recent", font=ctk.CTkFont(size=14, weight="bold"))
        recent_label.pack(side="left")

        # Dropdown urutan di kanan
        sort_by_option = ctk.CTkOptionMenu(
            recent_header,
            values=["Nama", "Tanggal", "Ukuran", "Pemilik"],
            command=self.sort_data  # Fungsi ini kamu buat sendiri nanti
        )
        sort_by_option.set("Urut Berdasarkan")  # Placeholder
        sort_by_option.pack(side="right")

        # Header tabel
        table_header = ctk.CTkFrame(base_frame_scroll)
        table_header.pack(fill="x", padx=(10))

        table_frame = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        table_frame.pack(fill="x", padx=10, pady=0)

        headers = ["Pembayaran ID", "Tgl Pembayaran", "Semester", "Jenis Tagihan", "Jumlah Tagihan", "Jumlah Dibayar", "Status"]
        for h in headers:
            ctk.CTkLabel(table_header, text=h, font=ctk.CTkFont(size=12, weight="normal"), width=130, anchor="w").pack(side="left", padx=5)

        # for col, header in enumerate(headers):
        #     lbl = ctk.CTkLabel(table_frame, text=header, font=ctk.CTkFont(weight="bold"))
        #     lbl.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        data = [
            ("Daily reports.xls", "2/12/2020", "2.3 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "1.2 MB", "Me"),
            ("Daily reports.xls", "2/12/2020", "12 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "22 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "22 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "22 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "22 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "22 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "22 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "22 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "1.4 MB", "Me"),
        ]

        # Pastikan parent table_frame bisa meluas
        table_frame.grid_columnconfigure(0, weight=1)
        
        for row, (name, mod, size, owner) in enumerate(data):
            row_frame = ctk.CTkFrame(table_frame, fg_color=color.white)
            row_frame.grid(row=row+1, column=0, sticky="ew", columnspan=4, padx=(0, 0), pady=5)

            row_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

            ctk.CTkLabel(row_frame, image=self.excel_icon, text=name, compound="left").grid(row=0, column=0, pady=5, padx=10, sticky="w")
            ctk.CTkLabel(row_frame, text=mod).grid(row=0, column=1, pady=5, padx=10, sticky="w")
            ctk.CTkLabel(row_frame, text=size).grid(row=0, column=2, pady=5, padx=10, sticky="w")
            ctk.CTkLabel(row_frame, text=owner).grid(row=0, column=3, pady=5, padx=10, sticky="w")

    def sort_data(self, pilihan):
        print(f"Urut berdasarkan: {pilihan}")



