
import customtkinter as ctk
import tkinter.messagebox as msg
from PIL import Image
import color
import os
from controller.mahasiswa_controll import MahasiswaController
from tkinter import messagebox
from tkinter import END 

data_mahasiswa = []

class Mahasiswa(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.entryrefs = {}  # Simpan semua CTkEntry
        self.asc = "ASC"
        self.desc = "DESC"

        self.controller = MahasiswaController()

        self.pack(padx=20, pady=20, fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.base_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.base_frame.pack(fill="x", padx=(0, 200), expand=True)
        # self.base_frame._scrollbar.grid_remove()

        # Header
        ctk.CTkLabel(self.base_frame, text="Data Mahasiswa", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=10, pady=(10, 5))

        # # Dapatkan direktori sekarang, lalu naik 3 tingkat
        # base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

        # # Load icons (pastikan file gambar ada di folder yang sama)
        # edit_path = os.path.join(base_dir, "resouse","image", "edit.png")
        # self.edit_icon = ctk.CTkImage(Image.open(edit_path), size=(32, 32))
        # remove_path = os.path.join(base_dir, "resouse","image", "remove.png")
        # self.remove_icon = ctk.CTkImage(Image.open(remove_path), size=(32, 32))

        # SECTION BAWAH: Invoices
        self.invoice_frame = ctk.CTkFrame(self,fg_color="transparent", corner_radius=10)
        self.invoice_frame.pack(fill="both", expand=True, padx=(0, 200))

        self.header_frame = ctk.CTkFrame(self.invoice_frame, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(0, 10), padx=(16))

        self.sort_data("Terbaru") # nilai awal
        
        ctk.CTkLabel(self.header_frame, text="Riwayat", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        ctk.CTkButton(self.header_frame, text="Tambah", command=self.simpan_input, width=100).pack(side="right")
        
        # Dropdown urutan di kanan
        # Gabungan sort dan filter
        self.option_menu = ctk.CTkOptionMenu(
            self.header_frame,
            values=[
                "Terbaru",
                "Terlama",
                "Nama",
                "NIM",
                "Semester",
                "Tahun Masuk",
                "Sudah Lunas",
                "Belum Lunas"
            ],
            command=self.sort_data  # Fungsi dipanggil saat dipilih
        )
        self.option_menu.set("Terbaru")  # Placeholder
        self.option_menu.pack(side="right", padx=10)


        # Header tabel
        table_header = ctk.CTkFrame(self.invoice_frame)
        table_header.pack(fill="x", padx=(16, 10))

        headers = ["Nama", "NIM", "Program Studi", "Semester", "Tahun Masuk", "Status"]
        ctk.CTkLabel(table_header, text="NO", font=ctk.CTkFont(size=12, weight="normal"), width=50, anchor="w").pack(side="left", padx=10)
        for h in headers:
            ctk.CTkLabel(table_header, text=h, font=ctk.CTkFont(size=12, weight="normal"), width=140, anchor="w").pack(side="left", padx=5)

        self.refresh_list()

        form_frame = ctk.CTkFrame(self.base_frame, fg_color="transparent")
        form_frame.pack(pady=10, padx=10, fill="x")
        form_frame.columnconfigure(0, weight=1)  # Biar kolom 0 bisa melar
        form_frame.columnconfigure(1, weight=1)  # Biar kolom 0 bisa melar

        def add_row( row, col1_label, col1_input, col2_label=None, col2_input=None):
            label1 = ctk.CTkLabel(form_frame, text=col1_label)
            input1 = col1_input
            label1.grid(row=row, column=0, sticky="w", padx=5, pady=5)
            input1.grid(row=row+1, column=0, sticky="ew", padx=5, pady=5)
            # Simpan referensi entry1
            self.entryrefs[f"{col1_label}"] = input1

            if col2_label and col2_input:
                label2 = ctk.CTkLabel(form_frame, text=col2_label)
                input2 = col2_input
                label2.grid(row=row, column=1, sticky="w", padx=5, pady=5)
                input2.grid(row=row+1, column=1, padx=5, sticky="ew", pady=5)
                # Simpan referensi entry2
                self.entryrefs[f"{col2_label}"] = input2

        add_row(0,
            "Nama", ctk.CTkEntry(form_frame, border_color=color.blue, placeholder_text="04319023"),
            "NIM", ctk.CTkEntry(form_frame,  border_color=color.blue, placeholder_text="Achmad Musyaffa Taufiqi")
        )
        add_row(2,
            "Program Studi", ctk.CTkEntry(form_frame, border_color=color.blue, placeholder_text="04319023"),
            "Semester", ctk.CTkEntry(form_frame,  border_color=color.blue, placeholder_text="Achmad Musyaffa Taufiqi")
        )
        add_row(4,
            "Tahun Masuk", ctk.CTkEntry(form_frame, border_color=color.blue, placeholder_text="04319023"),
            "Status", ctk.CTkEntry(form_frame,  border_color=color.blue, placeholder_text="Achmad Musyaffa Taufiqi")
        )

    def tambah_mhs(self):
        for key, entry in self.entryrefs.items():
            return (f"{key}: {entry.get()}")

    def simpan_input(self):
        data = {key: entry.get() for key, entry in self.entryrefs.items()}
        
        # Cek apakah ada yang kosong
        kosong = [label for label, value in data.items() if not value]
        
        if hasattr(self, 'notif_label'):
            self.notif_label.destroy()  # Hapus label lama jika ada

        if kosong:
            # Tampilkan peringatan jika ada yang kosong
            notif = f"Kolom berikut harus diisi: {', '.join(kosong)}"
            self.notif_label = ctk.CTkLabel(self.header_frame, text=notif, text_color="red")
            self.notif_label.pack()
            return

        try:
            print("DATA YANG DITERIMA:", data)
            # Ubah dictionary ke tuple sesuai urutan field di DB
            values = (
                data["Nama"],
                data["NIM"],
                data["Program Studi"],
                data["Semester"],
                data["Tahun Masuk"]
                # data["Status"]
            )
            self.controller.tambah(values)
            ctk.CTkLabel(self, text="Data berhasil ditambahkan!", text_color="green").pack()

            # update list
            self.refresh_list()

            # Kosongkan semua entry
            for entry in self.entryrefs.values():
                entry.delete(0, END)

        except Exception as e:
            print("eror", e)
            ctk.CTkLabel(self, text=f"Error: {e}", text_color="red").pack()
    
    # def tampilkan 



    def _create_labeled_entry(self, label_text):
        frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        frame.pack(pady=5, fill="x")
        ctk.CTkLabel(frame, text=label_text).pack(anchor="w")
        entry = ctk.CTkEntry(frame)
        entry.pack(fill="x")
        return entry

    def tambah_data(self):
        nim = self.nim_entry.get()
        nama = self.nama_entry.get()
        jurusan = self.jurusan_entry.get()

        if not nim or not nama or not jurusan:
            msg.showwarning("Validasi", "Semua field harus diisi!")
            return

        for mhs in data_mahasiswa:
            if mhs["nim"] == nim:
                msg.showerror("Duplikat", "NIM sudah terdaftar.")
                return

        data_mahasiswa.append({"nim": nim, "nama": nama, "jurusan": jurusan})
        self.clear_form()
        # self.refresh_list()

    def edit_data(self):
        nim = self.nim_entry.get()
        for mhs in data_mahasiswa:
            if mhs["nim"] == nim:
                mhs["nama"] = self.nama_entry.get()
                mhs["jurusan"] = self.jurusan_entry.get()
                self.clear_form()
                self.refresh_list()
                return
        msg.showerror("Error", "Mahasiswa tidak ditemukan.")

    def hapus_data(self):
        nim = self.nim_entry.get()
        for mhs in data_mahasiswa:
            if mhs["nim"] == nim:
                data_mahasiswa.remove(mhs)
                self.clear_form()
                self.refresh_list()
                return
        msg.showerror("Error", "Mahasiswa tidak ditemukan.")

    def load_selected_data(self, mhs):
        self.nim_entry.delete(0, "end")
        self.nim_entry.insert(0, mhs["nim"])
        self.nama_entry.delete(0, "end")
        self.nama_entry.insert(0, mhs["nama"])
        self.jurusan_entry.delete(0, "end")
        self.jurusan_entry.insert(0, mhs["jurusan"])

    def clear_form(self):
        self.nim_entry.delete(0, "end")
        self.nama_entry.delete(0, "end")
        self.jurusan_entry.delete(0, "end")

    def sort_data(self, pilihan):
        # Tentukan kategori: apakah ini sort atau filter status
        sort_opsi = {"Terbaru", "Terlama", "Nama", "NIM", "Semester", "Tahun Masuk"}
        filter_opsi = {"Sudah Lunas", "Belum Lunas"}

        if pilihan in sort_opsi:
            self.sort_by = pilihan
        elif pilihan in filter_opsi:
            self.status_filter = pilihan
        else:
            print("Pilihan tidak dikenali:", pilihan)
            return

        # # Nilai default kalau belum di-set
        # sort = getattr(self, "sort_by", "Terbaru")
        # status = getattr(self, "status_filter", "Semua")

        # # Ambil data dari controller
        # data = self.controller.ambil_data(sort, status)

        # Tampilkan ulang ke UI
        self.refresh_list()


    def list_mahasiswa(self, data):
        print(data)
        # Scrollable frame hanya dibuat sekali
        if not hasattr(self, 'table_list'):
            self.table_list = ctk.CTkScrollableFrame(self.invoice_frame, fg_color="transparent", height=500)
            self.table_list.pack(fill="both", expand=True)
        else:
            # Bersihkan isinya jika sudah ada
            for widget in self.table_list.winfo_children():
                widget.destroy()

        # Tampilkan data baris per baris
        for i, row in enumerate(data):
            row_frame = ctk.CTkFrame(self.table_list, fg_color=color.white)
            row_frame.pack(fill="x", pady=2, padx=(10, 0))

            ctk.CTkLabel(
                row_frame,
                text=f"{i+1}.",
                width=30,
                anchor="w",
                font=ctk.CTkFont(weight="bold")
            ).pack(side="left", padx=10)

            for j, value in enumerate(row):
                print(row)
                colors = "green" if value == "Paid" else ("orange" if value == "Pending" else "black")
                ctk.CTkLabel(
                    row_frame,
                    text=value,
                    fg_color="green",
                    width=120,
                    anchor="w",
                    font=ctk.CTkFont(weight="bold"),
                    text_color=colors if j == 5 else "black"  # index 5 = status
                ).pack(side="left", padx=2, pady=5)

            # Ambil NIM dari row index 1
            nim = row[1]

            # Tambahkan tombol Hapus
            ctk.CTkButton(
                row_frame,
                text="Hapus",
                width=60,
                fg_color=color.red,
                hover_color="#cc0000",
                command=lambda nim=nim: self.konfirmasi_hapus(nim)
            ).pack(side="right", padx=5)
           
            # Tambahkan tombol Edit
            ctk.CTkButton(
                row_frame,
                text="Edit",
                width=60,
                fg_color=color.blue,
                hover_color="#cc0000",
                command=lambda nim=nim: self.edit_data(nim)
            ).pack(side="right", padx=5)
        
        
    def konfirmasi_hapus(self, nim):
        if messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus mahasiswa dengan NIM {nim}?"):
            self.controller.hapus_data(nim)  # Panggil controller
            # update list
            self.refresh_list()
    
    def edit_data(self, nim):
        data = self.controller.ambil_data_by_nim(nim)
        data_dict = {i: val for i, val in enumerate(data)} #data dictionary
        print(data_dict)
        for key, entry in self.entryrefs.items():
            entry.delete(0, 'end')  # Kosongkan dulu
            entry.insert(0, data_dict.get(key, key)) 

    def refresh_list(self):
        # Nilai default kalau belum di-set
        sort = getattr(self, "sort_by", "Terbaru")
        status = getattr(self, "status_filter", "Semua")

        # Ambil data dari controller
        data = self.controller.ambil_data(sort, status)
        self.list_mahasiswa(data)


