import customtkinter as ctk
import tkinter.messagebox as msg

# Simulasi penyimpanan sementara (bisa diganti DB)
data_jenis_tagihan = []

class JenisTagihan(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.configure(corner_radius=10)

        # --- Judul ---
        self.title_label = ctk.CTkLabel(self, text="Jenis Tagihan", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # --- Form Input ---
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10)

        self.kode_entry = self._create_labeled_entry("Kode", 0)
        self.nama_entry = self._create_labeled_entry("Nama Tagihan", 1)

        # --- Tombol Aksi ---
        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.pack(pady=5)

        self.add_btn = ctk.CTkButton(self.btn_frame, text="Tambah", command=self.tambah_data)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.edit_btn = ctk.CTkButton(self.btn_frame, text="Edit", command=self.edit_data)
        self.edit_btn.grid(row=0, column=1, padx=5)

        # --- Tabel Jenis Tagihan (Listbox) ---
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(pady=10, fill="both", expand=True)

        self.listbox = ctk.CTkTextbox(self.table_frame, width=500, height=200)
        self.listbox.pack(fill="both", expand=True)
        self.listbox.configure(state="disabled")

        self.listbox.bind("<Double-Button-1>", self.load_selected_data)

        self.refresh_list()

    def _create_labeled_entry(self, label_text, row):
        label = ctk.CTkLabel(self.form_frame, text=label_text)
        label.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        entry = ctk.CTkEntry(self.form_frame, width=200)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def tambah_data(self):
        kode = self.kode_entry.get().strip().upper()
        nama = self.nama_entry.get().strip()

        if not kode or not nama:
            msg.showwarning("Validasi", "Kode dan Nama harus diisi!")
            return

        for jt in data_jenis_tagihan:
            if jt["kode"] == kode:
                msg.showerror("Duplikat", "Kode jenis tagihan sudah ada.")
                return

        data_jenis_tagihan.append({"kode": kode, "nama": nama})
        self.clear_form()
        self.refresh_list()

    def edit_data(self):
        kode = self.kode_entry.get().strip().upper()
        for jt in data_jenis_tagihan:
            if jt["kode"] == kode:
                jt["nama"] = self.nama_entry.get().strip()
                self.clear_form()
                self.refresh_list()
                return
        msg.showerror("Error", "Kode tagihan tidak ditemukan.")

    def load_selected_data(self, event):
        cursor_index = self.listbox.index("@%s,%s" % (event.x, event.y))
        baris = self.listbox.get("1.0", "end").splitlines()
        if not baris or cursor_index > len(baris):
            return

        line = baris[int(cursor_index)-1]
        if " - " not in line:
            return
        kode, nama = line.split(" - ")
        self.kode_entry.delete(0, "end")
        self.kode_entry.insert(0, kode)
        self.nama_entry.delete(0, "end")
        self.nama_entry.insert(0, nama)

    def refresh_list(self):
        self.listbox.configure(state="normal")
        self.listbox.delete("1.0", "end")
        for jt in data_jenis_tagihan:
            self.listbox.insert("end", f"{jt['kode']} - {jt['nama']}\n")
        self.listbox.configure(state="disabled")

    def clear_form(self):
        self.kode_entry.delete(0, "end")
        self.nama_entry.delete(0, "end")


