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

# Setup awal
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class RiwayatTagihan(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)
        self.pack(padx=20, pady=20)
        self.build_ui()

    def build_ui(self):
        # SECTION ATAS: Billing Summary & Payment Method
        top_frame = ctk.CTkFrame(self, corner_radius=10)
        top_frame.pack(fill="x", pady=(0, 20))

        # Billing Summary
        billing_frame = ctk.CTkFrame(top_frame, corner_radius=10)
        billing_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

        ctk.CTkLabel(billing_frame, text="Current Plan Summary", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=(0, 5))
        ctk.CTkLabel(billing_frame, text="Growth Plan", font=ctk.CTkFont(size=12)).pack(anchor="w")
        ctk.CTkLabel(billing_frame, text="Billing Cycle: Monthly", font=ctk.CTkFont(size=11)).pack(anchor="w")
        ctk.CTkLabel(billing_frame, text="Plan Cost: $5698", font=ctk.CTkFont(size=11)).pack(anchor="w")
        ctk.CTkLabel(billing_frame, text="Usage: 4550 / 5000 users", font=ctk.CTkFont(size=11)).pack(anchor="w", pady=(5, 0))
        ctk.CTkProgressBar(billing_frame, width=250, height=12, progress_color="blue", determinate_speed=1).pack(anchor="w", pady=5)
        ctk.CTkButton(billing_frame, text="Upgrade", width=100).pack(anchor="e", pady=(5, 0))

        # Payment Method
        payment_frame = ctk.CTkFrame(top_frame, corner_radius=10)
        payment_frame.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)

        ctk.CTkLabel(payment_frame, text="Payment Method", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=(0, 5))
        ctk.CTkLabel(payment_frame, text="MasterCard **** 4092", font=ctk.CTkFont(size=11)).pack(anchor="w")
        ctk.CTkLabel(payment_frame, text="Expiry: 09/2024", font=ctk.CTkFont(size=11)).pack(anchor="w")
        ctk.CTkLabel(payment_frame, text="billing@acme.corp", font=ctk.CTkFont(size=11)).pack(anchor="w")
        ctk.CTkButton(payment_frame, text="Change", width=100).pack(anchor="e", pady=(5, 0))

        # SECTION BAWAH: Invoices
        invoice_frame = ctk.CTkFrame(self, corner_radius=10)
        invoice_frame.pack(fill="both", expand=True)

        header_frame = ctk.CTkFrame(invoice_frame)
        header_frame.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(header_frame, text="Invoices", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        ctk.CTkButton(header_frame, text="Download", width=100).pack(side="right")

        # Header tabel
        table_header = ctk.CTkFrame(invoice_frame)
        table_header.pack(fill="x", pady=(0, 5))

        headers = ["Invoice ID", "Billing Date", "Plan", "Amount", "Status"]
        for h in headers:
            ctk.CTkLabel(table_header, text=h, font=ctk.CTkFont(size=12, weight="bold"), width=120, anchor="w").pack(side="left", padx=5)

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
            row_frame = ctk.CTkFrame(invoice_frame)
            row_frame.pack(fill="x", pady=2)

            for i, value in enumerate(row):
                color = "green" if value == "Paid" else ("orange" if value == "Pending" else "black")
                label = ctk.CTkLabel(
                    row_frame,
                    text=value,
                    width=120,
                    anchor="w",
                    text_color=color if i == 4 else "black"
                )
                label.pack(side="left", padx=5)


