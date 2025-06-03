import customtkinter as ctk
import color
from PIL import Image
import os

class Profil(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
       
        # bg_path = os.path.join(os.path.dirname(__file__), "image.png")
        # bg_image = ctk.CTkImage(Image.open(bg_path), size=(300, 300))

        # # Label background (diletakkan di parent langsung)
        # bg_label = ctk.CTkLabel(self, image=bg_image, text="")
        # bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        base_frame_scroll = ctk.CTkScrollableFrame(self, fg_color=color.gray)
        base_frame_scroll.pack(fill="both", expand=True)
        base_frame_scroll._scrollbar.grid_remove()


        # Judul Halaman
        ctk.CTkLabel(base_frame_scroll, text="Data Mahasiswa", font=ctk.CTkFont(size=22, weight="bold"), anchor="w", justify="left").pack(fill="x",padx=16, pady=(10, 5))
        ctk.CTkLabel(base_frame_scroll, text="Biodata Diri", font=ctk.CTkFont(size=16), anchor="w", justify="left").pack(fill="x", padx=16, pady=(0, 20))

        # Avatar
        foto_frame = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        # Load icons profil
        profil_path = os.path.join(os.path.dirname(__file__), "image.png")
        profil_icon = ctk.CTkImage(Image.open(profil_path), size=(300, 300))

        avatar = ctk.CTkLabel(foto_frame, image=profil_icon, text="")
        ubah_foto_btn = ctk.CTkButton(foto_frame, text="Ubah Foto", width=100)
        avatar.pack()
        ubah_foto_btn.pack(pady=(5, 10))
        foto_frame.pack()


        # Form Grid
        form_frame = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        form_frame.pack(pady=10, padx=150, fill="x")
        form_frame.columnconfigure(0, weight=1)  # Biar kolom 0 bisa melar
        form_frame.columnconfigure(1, weight=1)  # Biar kolom 0 bisa melar

        # Fungsi pembantu
        def add_row(row, col1_label, col1_input, col2_label=None, col2_input=None):
            label1 = ctk.CTkLabel(form_frame, text=col1_label)
            input1 = col1_input
            label1.grid(row=row, column=0, sticky="w", padx=5, pady=5)
            input1.grid(row=row+1, column=0, sticky="ew", padx=5, pady=5)

            if col2_label and col2_input:
                label2 = ctk.CTkLabel(form_frame, text=col2_label)
                input2 = col2_input
                label2.grid(row=row, column=1, sticky="w", padx=5, pady=5)
                input2.grid(row=row+1, column=1, padx=5, sticky="ew", pady=5)

        # Input Fields
        # mhs id
        ctk.CTkLabel(form_frame, text="Mahasiswa ID").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        mhs_id = ctk.CTkEntry(form_frame, border_color=color.blue)
        mhs_id.insert(0, "9283823823")
        mhs_id.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # name
        ctk.CTkLabel(form_frame, text="Nama Lengkap").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        mhs_name = ctk.CTkEntry(form_frame, border_color=color.blue)
        mhs_name.insert(0, "Samdola galih")
        mhs_name.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        add_row(4,
            "NIM", ctk.CTkEntry(form_frame, border_color=color.blue, placeholder_text="04319023"),
            "Program Studi", ctk.CTkEntry(form_frame,  border_color=color.blue, placeholder_text="Achmad Musyaffa Taufiqi")
        )
        add_row(6,
            "Fakultas", ctk.CTkComboBox(form_frame,  border_color=color.blue, values=["Laki-laki", "Perempuan"]),
            "Tahun Masuk", ctk.CTkEntry(form_frame,  border_color=color.blue, placeholder_text="Tangerang")
        )

        ctk.CTkFrame(form_frame, height=100, fg_color="transparent").grid(row=8, column=0, columnspan=2, sticky="w", padx=5, pady=5)
       
       
        # add_row(4,
        #     "Tanggal Lahir", ctk.CTkEntry(form_frame, placeholder_text="01/25/2000"),
        #     "Golongan Darah", ctk.CTkComboBox(form_frame, values=["A", "B", "AB", "O"])
        # )
        # add_row(6,
        #     "Agama", ctk.CTkComboBox(form_frame, values=["Islam", "Kristen", "Hindu", "Budha", "Lainnya"]),
        # )

        # Alamat
        # ctk.CTkLabel(form_frame, text="Alamat").grid(row=8, column=0, sticky="w", padx=5, pady=5)
        # alamat = ctk.CTkTextbox(form_frame, height=60, width=300)
        # alamat.insert("1.0", "Sidoarjo")
        # alamat.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        # No Telepon
        # ctk.CTkLabel(form_frame, text="No Telepon").grid(row=10, column=0, sticky="w", padx=5, pady=5)
        # ctk.CTkEntry(form_frame, placeholder_text="089121313").grid(row=11, column=0, columnspan=2, padx=5, pady=5)

        # # Informasi Akademik
        # ctk.CTkLabel(base_frame_scroll, text="Informasi Akademik", font=ctk.CTkFont(size=16)).pack(pady=(20, 10))

        # akademik_frame = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        # akademik_frame.pack(padx=20)

        # Program Studi dan Dosen Wali
        # ctk.CTkLabel(akademik_frame, text="Program Studi").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        # ctk.CTkComboBox(akademik_frame, values=["Ilmu Komputer - Teknik Informatika"]).grid(row=1, column=0, padx=5, pady=5)

        # ctk.CTkLabel(akademik_frame, text="Dosen Wali").grid(row=0, column=1, sticky="w", padx=5, pady=5)
        # ctk.CTkComboBox(akademik_frame, values=["M Rizky Hidayat"]).grid(row=1, column=1, padx=5, pady=5)

