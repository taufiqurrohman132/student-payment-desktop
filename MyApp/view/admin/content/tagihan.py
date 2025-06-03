import customtkinter as ctk
import tkinter.messagebox as msg

# Simulasi data
data_mahasiswa = [
    {"nim": "22001", "nama": "Andi"},
    {"nim": "22002", "nama": "Budi"}
]

data_jenis_tagihan = [
    {"kode": "UKT", "nama": "Uang Kuliah Tunggal"},
    {"kode": "SPP", "nama": "Sumbangan Pembinaan Pendidikan"},
]

data_tagihan = []  # Simulasi database tagihan

class Tagihan(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        # Judul
        self.title_label = ctk.CTkLabel(self, text="Entri Tagihan Mahasiswa", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Frame Form
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=5)

        self.nim_option = self._create_dropdown("Mahasiswa (NIM - Nama)", self.get_mahasiswa_options(), 0)
        self.semester_entry = self._create_labeled_entry("Semester", 1)
        self.jenis_option = self._create_dropdown("Jenis Tagihan", self.get_jenis_options(), 2)
        self.nominal_entry = self._create_labeled_entry("Nominal", 3)
        self.status_entry = self._create_labeled_entry("Status (Lunas/Belum)", 4)

        # Tombol
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=5)

        self.btn_buat = ctk.CTkButton(self.button_frame, text="Buat Tagihan", command=self.buat_tagihan)
        self.btn_buat.grid(row=0, column=0, padx=5)

        self.btn_edit = ctk.CTkButton(self.button_frame, text="Edit Tagihan", command=self.edit_tagihan)
        self.btn_edit.grid(row=0, column=1, padx=5)

        # Tabel tagihan (TextBox simulasi)
        self.table = ctk.CTkTextbox(self, height=200)
        self.table.pack(pady=10, fill="both", expand=True)
        self.table.configure(state="disabled")
        self.table.bind("<Double-Button-1>", self.load_selected)

        self.refresh_table()

    def _create_labeled_entry(self, label, row):
        lbl = ctk.CTkLabel(self.form_frame, text=label)
        lbl.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        ent = ctk.CTkEntry(self.form_frame)
        ent.grid(row=row, column=1, padx=10, pady=5)
        return ent

    def _create_dropdown(self, label, options, row):
        lbl = ctk.CTkLabel(self.form_frame, text=label)
        lbl.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        opt = ctk.CTkComboBox(self.form_frame, values=options, width=200)
        opt.grid(row=row, column=1, padx=10, pady=5)
        if options:
            opt.set(options[0])
        return opt

    def get_mahasiswa_options(self):
        return [f"{m['nim']} - {m['nama']}" for m in data_mahasiswa]

    def get_jenis_options(self):
        return [f"{j['kode']} - {j['nama']}" for j in data_jenis_tagihan]

    def buat_tagihan(self):
        mhs_info = self.nim_option.get()
        semester = self.semester_entry.get().strip()
        jenis_info = self.jenis_option.get()
        nominal = self.nominal_entry.get().strip()
        status = self.status_entry.get().strip()

        if not all([mhs_info, semester, jenis_info, nominal, status]):
            msg.showwarning("Validasi", "Semua field harus diisi.")
            return

        nim = mhs_info.split(" - ")[0]
        jenis = jenis_info.split(" - ")[0]

        # Cek duplikat
        for t in data_tagihan:
            if t["nim"] == nim and t["semester"] == semester and t["jenis"] == jenis:
                msg.showerror("Duplikat", "Tagihan untuk mahasiswa ini dan jenis/semester sudah ada.")
                return

        data_tagihan.append({
            "nim": nim,
            "semester": semester,
            "jenis": jenis,
            "nominal": nominal,
            "status": status
        })

        self.clear_form()
        self.refresh_table()

    def edit_tagihan(self):
        mhs_info = self.nim_option.get()
        semester = self.semester_entry.get().strip()
        jenis_info = self.jenis_option.get()
        nim = mhs_info.split(" - ")[0]
        jenis = jenis_info.split(" - ")[0]

        for tag in data_tagihan:
            if tag["nim"] == nim and tag["semester"] == semester and tag["jenis"] == jenis:
                tag["nominal"] = self.nominal_entry.get().strip()
                tag["status"] = self.status_entry.get().strip()
                self.clear_form()
                self.refresh_table()
                return
        msg.showerror("Error", "Tagihan tidak ditemukan untuk diedit.")

    def load_selected(self, event):
        idx = int(self.table.index("@%s,%s" % (event.x, event.y)).split(".")[0]) - 1
        if 0 <= idx < len(data_tagihan):
            tag = data_tagihan[idx]
            self.nim_option.set(f"{tag['nim']} - " + self.get_nama(tag["nim"]))
            self.semester_entry.delete(0, "end")
            self.semester_entry.insert(0, tag["semester"])
            self.jenis_option.set(f"{tag['jenis']} - " + self.get_nama_jenis(tag["jenis"]))
            self.nominal_entry.delete(0, "end")
            self.nominal_entry.insert(0, tag["nominal"])
            self.status_entry.delete(0, "end")
            self.status_entry.insert(0, tag["status"])

    def refresh_table(self):
        self.table.configure(state="normal")
        self.table.delete("1.0", "end")
        for t in data_tagihan:
            nama = self.get_nama(t["nim"])
            nama_jenis = self.get_nama_jenis(t["jenis"])
            line = f"{t['nim']} ({nama}) | Semester {t['semester']} | {t['jenis']} ({nama_jenis}) | Rp{t['nominal']} | {t['status']}\n"
            self.table.insert("end", line)
        self.table.configure(state="disabled")

    def clear_form(self):
        self.semester_entry.delete(0, "end")
        self.nominal_entry.delete(0, "end")
        self.status_entry.delete(0, "end")

    def get_nama(self, nim):
        for m in data_mahasiswa:
            if m["nim"] == nim:
                return m["nama"]
        return "-"

    def get_nama_jenis(self, kode):
        for j in data_jenis_tagihan:
            if j["kode"] == kode:
                return j["nama"]
        return "-"
