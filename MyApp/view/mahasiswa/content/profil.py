import customtkinter as ctk
from PIL import Image
import os

ctk.set_appearance_mode("light")  # light or dark
ctk.set_default_color_theme("blue")


class Profil(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Load icons (pastikan file gambar ada di folder yang sama)
        folder_path = os.path.join(os.path.dirname(__file__), "folder.png")
        exe_path = os.path.join(os.path.dirname(__file__), "exe.png")
        self.folder_icon = ctk.CTkImage(Image.open(folder_path), size=(32, 32))
        self.excel_icon = ctk.CTkImage(Image.open(exe_path), size=(32, 32))

        self.create_widgets()

    def create_widgets(self):
        # Header
        header_frame = ctk.CTkFrame(self)
        header_frame.pack(fill="x", pady=10, padx=10)

        upload_btn = ctk.CTkButton(header_frame, text="Upload")
        upload_btn.pack(side="left", padx=5)

        create_btn = ctk.CTkButton(header_frame, text="Create +")
        create_btn.pack(side="left", padx=5)

        search_entry = ctk.CTkEntry(header_frame, placeholder_text="Search")
        search_entry.pack(side="right", padx=5)

        # Folder section
        folder_frame = ctk.CTkFrame(self)
        folder_frame.pack(fill="x", padx=10)

        folder_label = ctk.CTkLabel(folder_frame, text="Files > Folder", font=ctk.CTkFont(size=14, weight="bold"))
        folder_label.pack(anchor="w", pady=5)

        folders_grid = ctk.CTkFrame(folder_frame)
        folders_grid.pack(pady=10)

        for i in range(2):  # 2 rows
            for j in range(3):  # 3 columns
                folder = ctk.CTkFrame(folders_grid, width=150, height=90, corner_radius=8, border_width=1)
                folder.grid(row=i, column=j, padx=10, pady=10)
                folder.pack_propagate(False)

                icon_label = ctk.CTkLabel(folder, image=self.folder_icon, text="")
                icon_label.pack(pady=5)

                folder_text = ctk.CTkLabel(folder, text="Name of the Folder\n23 files", justify="center")
                folder_text.pack()

        # Recent files section
        recent_label = ctk.CTkLabel(self, text="Recent", font=ctk.CTkFont(size=14, weight="bold"))
        recent_label.pack(anchor="w", padx=10, pady=(20, 0))

        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill="x", padx=10, pady=10)

        headers = ["Name", "Modified", "Size", "Owned"]
        for col, header in enumerate(headers):
            lbl = ctk.CTkLabel(table_frame, text=header, font=ctk.CTkFont(weight="bold"))
            lbl.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        data = [
            ("Daily reports.xls", "2/12/2020", "2.3 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "1.2 MB", "Me"),
            ("Daily reports.xls", "2/12/2020", "12 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "22 MB", "John"),
            ("Daily reports.xls", "2/12/2020", "1.4 MB", "Me"),
        ]

        for row, (name, mod, size, owner) in enumerate(data, start=1):
            # Icon + filename
            ctk.CTkLabel(table_frame, image=self.excel_icon, text=name, compound="left").grid(
                row=row, column=0, padx=10, pady=3, sticky="w"
            )
            # Other columns
            ctk.CTkLabel(table_frame, text=mod).grid(row=row, column=1, padx=10, pady=3, sticky="w")
            ctk.CTkLabel(table_frame, text=size).grid(row=row, column=2, padx=10, pady=3, sticky="w")
            ctk.CTkLabel(table_frame, text=owner).grid(row=row, column=3, padx=10, pady=3, sticky="w")


