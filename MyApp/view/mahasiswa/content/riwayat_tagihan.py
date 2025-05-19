# import customtkinter as ctk
# from tkinter import font

# class RiwayatTagihan(ctk.CTkFrame):
#     def __init__(self, master):
#         super().__init__(master)

#         self.grid_rowconfigure(0, weight=1)

#         # Konten kanan
#         konten = ctk.CTkFrame(self, fg_color="yellow")
#         konten.pack(fill="both", expand=True)  # Meluas ke seluruh parent

#         ctk.CTkLabel(konten, text="Riwayat Tagihan", anchor="w", font=ctk.CTkFont(size=14, weight="bold")).pack(fill="x", pady=5, padx=10)
#         # ctk.CTkLabel(konten, text="Mahasiswa sejahtera Riwayat Tagihan", anchor="w", font=ctk.CTkFont(size=10)).pack(fill="x", side="top", padx=10)

#         # header
#         header = ctk.CTkFrame(konten)
#         header.pack(padx=10, fill="x")

#         header.grid_columnconfigure(0, weight=1)
#         header.grid_columnconfigure(1, weight=1)

#         header1 = ctk.CTkFrame(header, fg_color="green")
#         header1.grid(row=0, column=0, padx=10, sticky="ew")
#         header1.pack_propagate(False)
#         header1.grid_propagate(False) 

#         header1.grid_columnconfigure(0, weight=1)
#         header1.grid_columnconfigure(1, weight=1)
#         header1.grid_columnconfigure(2, weight=1)

#         ctk.CTkLabel(header1, text="NIM", anchor="w", font=ctk.CTkFont(size=12)).grid(row=0, column=0, padx=10, sticky="ew")
#         ctk.CTkLabel(header1, text="Prodi", anchor="w", font=ctk.CTkFont(size=12)).grid(row=0, column=1, padx=10, sticky="ew")
#         ctk.CTkLabel(header1, text="Angkatan", anchor="w", font=ctk.CTkFont(size=12)).grid(row=0, column=2, padx=10, sticky="ew")

#         ctk.CTkLabel(header1, text="NIM", anchor="w", font=ctk.CTkFont(size=16, weight="bold")).grid(row=1, column=0, padx=10, sticky="ew")
#         ctk.CTkLabel(header1, text="Prodi", anchor="w", font=ctk.CTkFont(size=16, weight="bold")).grid(row=1, column=1, padx=10, sticky="ew")
#         ctk.CTkLabel(header1, text="Angkatan", anchor="w", font=ctk.CTkFont(size=16, weight="bold")).grid(row=1, column=2, padx=10, sticky="ew")


#         # header_in1 = ctk.CTkFrame(header1, fg_color="transparent")
#         # header_in1.pack(fill="x")
#         # header_in1.grid_columnconfigure(0, weight=1)
#         # header_in1.grid_columnconfigure(1, weight=1)
#         # header_in1.grid_columnconfigure(2, weight=1)

#         # ctk.CTkLabel(header_in1, text="NIM", anchor="w", font=ctk.CTkFont(size=12)).grid(row=0, column=0, padx=5, sticky="ew")
#         # ctk.CTkLabel(header_in1, text="Prodi", anchor="w", font=ctk.CTkFont(size=12)).grid(row=0, column=1, padx=5, sticky="ew")
#         # ctk.CTkLabel(header_in1, text="Angkatan", anchor="w", font=ctk.CTkFont(size=12)).grid(row=0, column=2, padx=5, sticky="ew")

#         # ctk.CTkLabel(header_in1, text="NIM", anchor="w", font=ctk.CTkFont(size=16, weight="bold")).grid(row=1, column=0, padx=5, sticky="ew")
#         # ctk.CTkLabel(header_in1, text="Prodi", anchor="w", font=ctk.CTkFont(size=16, weight="bold")).grid(row=1, column=1, padx=5, sticky="ew")
#         # ctk.CTkLabel(header_in1, text="Angkatan", anchor="w", font=ctk.CTkFont(size=16, weight="bold")).grid(row=1, column=2, padx=5, sticky="ew")


#         header2 = ctk.CTkFrame(header, fg_color="green")
#         header2.grid(row=0, column=1, padx=10, sticky="ew")
        
#         # header_in2 = ctk.CTkFrame(header2, fg_color="blue")
#         # header_in2.pack(fill="x")
#         # header_in2.grid_columnconfigure(0, weight=1)
#         # header_in2.grid_columnconfigure(1, weight=1)
#         # header_in2.grid_columnconfigure(2, weight=1)

#         # ctk.CTkLabel(header_in2, text="NIM", anchor="w", font=ctk.CTkFont(size=10)).grid(row=0, column=0, padx=5, sticky="ew")
#         # ctk.CTkLabel(header_in2, text="Prodi", anchor="w", font=ctk.CTkFont(size=10)).grid(row=0, column=1, padx=5, sticky="ew")
#         # ctk.CTkLabel(header_in2, text="Angkatan", anchor="w", font=ctk.CTkFont(size=10)).grid(row=0, column=2, padx=5, sticky="ew")





#         for i in range(1, 6):
#             ctk.CTkLabel(konten, text=f"- Item {i}").pack(anchor="w", padx=10, pady=2)
import customtkinter as ctk
import color

# Setup awal
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class RiwayatTagihan(ctk.CTkFrame):
    def __init__(self, master):
        global color
        super().__init__(master, fg_color="transparent", corner_radius=10)
        self.pack(padx=20, pady=20)
        self.build_ui()

    def build_ui(self):
        global color

        # Header
        ctk.CTkLabel(self, text="Riwayat Tagihan", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=16, pady=(16, 0))
        ctk.CTkLabel(self, text="Mhasiswa sejahtera Riwayat Tagihan", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=16, pady=(0, 10))

        # SECTION ATAS: Billing Summary & Payment Method
        top_frame = ctk.CTkFrame(self, fg_color="red",corner_radius=10)
        top_frame.pack(fill="x", pady=(0, 20), padx=6)

        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_columnconfigure(1, weight=1)


        # Billing Summary
        billing_frame = ctk.CTkFrame(top_frame, fg_color=color.white , corner_radius=10)
        billing_frame.grid(row=0, column=0, padx=10, sticky="ew")
        billing_frame.grid_propagate(False)
        billing_frame.pack_propagate(False)

        billing_frame_top = ctk.CTkFrame(billing_frame)
        billing_frame_top.pack(fill="x")

        bil_mhs = ctk.CTkLabel(billing_frame_top, text="Mahasiswa", font=ctk.CTkFont(size=14, weight="bold"))
        bil_mhs.pack(side="left",padx=10, pady=5)
        ctk.CTkButton(billing_frame_top, text="Upgrade", width=100).pack(side="right", padx=10, pady=5)

        billing_frame_in = ctk.CTkFrame(billing_frame, corner_radius=10)
        billing_frame_in.pack(fill="x", pady=(10, 0))
        billing_frame_in.grid_columnconfigure(0, weight=1)
        billing_frame_in.grid_columnconfigure(1, weight=1)
        billing_frame_in.grid_columnconfigure(2, weight=1)

        ctk.CTkLabel(billing_frame_in, anchor="w", text="NIM", font=ctk.CTkFont(size=12)).grid(row=0, column=0, padx=10, pady=( 0),  sticky="ew")
        ctk.CTkLabel(billing_frame_in, anchor="w", text="Program Studi", font=ctk.CTkFont(size=11)).grid(row=0, column=1, padx=10, pady=( 0),  sticky="ew")
        ctk.CTkLabel(billing_frame_in, anchor="w", text="Tahun Masuk", font=ctk.CTkFont(size=11)).grid(row=0, column=2, padx=10, pady=( 0),  sticky="ew")
        nim = ctk.CTkLabel(billing_frame_in, anchor="w", text="01010", font=ctk.CTkFont(size=14, weight="bold")).grid(row=1, column=0, padx=10, pady=( 0),  sticky="ew")
        prodi = ctk.CTkLabel(billing_frame_in, anchor="w", text="T.Informatika", font=ctk.CTkFont(size=14, weight="bold")).grid(row=1, column=1, padx=10, pady=( 0),  sticky="ew")
        thn_masuk = ctk.CTkLabel(billing_frame_in, anchor="w", text="2024", font=ctk.CTkFont(size=14, weight="bold")).grid(row=1, column=2, padx=10, pady=( 0),  sticky="ew")

        billing_status = ctk.CTkLabel(billing_frame, anchor="w", text="Status", font=ctk.CTkFont(size=11))
        billing_status.pack(side="left", padx=10)
        billing_status_value = ctk.CTkLabel(billing_frame, anchor="w", text="4000000 sudah di bayar dari 5000000", font=ctk.CTkFont(size=11, weight="bold"))
        billing_status_value.pack(side="left", padx=10)

        ctk.CTkProgressBar(billing_frame, width=400, height=20, progress_color="blue", determinate_speed=1).pack(fill="x", padx=10)


    
        # Payment Method
        payment_frame = ctk.CTkFrame(top_frame, fg_color=color.white, corner_radius=10)
        payment_frame.grid(row=0, column=1, padx=10, sticky="ew")
        # payment_frame.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        payment_frame.grid_propagate(False)
        payment_frame.pack_propagate(False)

        ctk.CTkLabel(payment_frame, text="Payment Method", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w",padx=10, pady=(0, 5))
        ctk.CTkLabel(payment_frame, text="MasterCard **** 4092", font=ctk.CTkFont(size=11)).pack(anchor="w",padx=10)
        ctk.CTkLabel(payment_frame, text="Expiry: 09/2024", font=ctk.CTkFont(size=11)).pack(anchor="w",padx=10)
        ctk.CTkLabel(payment_frame, text="billing@acme.corp", font=ctk.CTkFont(size=11)).pack(anchor="w",padx=10)
        ctk.CTkButton(payment_frame, text="Change", width=100).pack(anchor="e", pady=(5, 0),padx=10)

        # SECTION BAWAH: Invoices
        invoice_frame = ctk.CTkFrame(self,fg_color="transparent", corner_radius=10)
        invoice_frame.pack(fill="both", expand=True)

        header_frame = ctk.CTkFrame(invoice_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 10), padx=16)

        ctk.CTkLabel(header_frame, text="Riwayat", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        ctk.CTkButton(header_frame, text="Download", width=100).pack(side="right")

        # Header tabel
        table_header = ctk.CTkFrame(invoice_frame)
        table_header.pack(fill="x", pady=(0, 5), padx=16)

        headers = ["Invoice ID", "Billing Date", "Plan", "Amount", "Status"]
        for h in headers:
            ctk.CTkLabel(table_header, text=h, font=ctk.CTkFont(size=12, weight="normal"), width=120, anchor="w").pack(side="left", padx=5)

        # Data tabel
        data = [
            ("#23456", "23 Jan 2023", "Basic Plan", "$1200", "Paid"),
            ("#56489", "23 Feb 2023", "Pro Plan", "$7000", "Paid"),
            ("#56498", "23 Mar 2023", "Pro Plan", "$7000", "Paid"),
            ("#88380", "23 Apr 2023", "Growth Plan", "$5698", "Paid"),
            ("#90394", "23 May 2023", "Basic Plan", "$1200", "Paid"),
            ("#929348", "23 Jun 2023", "Growth Plan", "$1200", "Paid"),
            ("#88384", "23 Jul 2023", "Growth Plan", "$5698", "Pending"),
        ]

        for row in data:
            row_frame = ctk.CTkFrame(invoice_frame, fg_color=color.white)
            row_frame.pack(fill="x", pady=2, padx=16)

            for i, value in enumerate(row):
                colors = "green" if value == "Paid" else ("orange" if value == "Pending" else "black")
                label = ctk.CTkLabel(
                    row_frame,
                    text=value,
                    width=120, #lebar kolom
                    anchor="w",
                    font=ctk.CTkFont(weight="bold"),
                    text_color=colors if i == 4 else "black"
                )
                label.pack(side="left", padx=5, pady=5)


