import customtkinter as ctk
import tkinter as tk
from PIL import Image
import os
from functools import partial
import color

class MetodePembayaran(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Cari path gambar
        profil_path = os.path.join(os.path.dirname(__file__), "folder.png")
        if not os.path.exists(profil_path):
            raise FileNotFoundError(f"Gambar tidak ditemukan: {profil_path}")

        # Buat objek CTkImage dari PIL image
        self.folder_icon_ref = ctk.CTkImage(Image.open(profil_path), size=(50, 50))

        self.create_ui()

    def create_ui(self):

        base_frame_scroll = ctk.CTkScrollableFrame(self, fg_color=color.gray)
        base_frame_scroll.pack(fill="both", expand=True)

        base_frame_scroll._scrollbar.grid_remove()
        header_frame = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        header_frame.pack(fill="x", pady=10, padx=10)

        upload_btn = ctk.CTkButton(header_frame, text="Upload")
        upload_btn.pack(side="left", padx=5)

        create_btn = ctk.CTkButton(header_frame, text="Create +")
        create_btn.pack(side="left", padx=5)

        search_entry = ctk.CTkEntry(header_frame, placeholder_text="Search")
        search_entry.pack(side="right", padx=5)

        folder_frame = ctk.CTkFrame(base_frame_scroll, fg_color="transparent")
        folder_frame.pack(fill="both", expand=True, padx=(10, 200))

        folder_label = ctk.CTkLabel(folder_frame, text="Metode Pembayaran", font=ctk.CTkFont(size=22, weight="bold"))
        folder_label.pack(anchor="w", pady=5)

        folders_grid = ctk.CTkFrame(folder_frame, fg_color="transparent")
        folders_grid.pack(pady=10, fill="both", expand=True)

        for col in range(3):
            folders_grid.grid_columnconfigure(col, weight=1)

        for i in range(8):  # 2 rows
            for j in range(3):  # 3 columns
                folder = ctk.CTkFrame(folders_grid, corner_radius=16, height=150, fg_color=color.white, border_width=1)
                folder.grid(row=i, column=j, padx=10, pady=10, sticky="we")
                folder.pack_propagate(False)

                # Checkbox kiri atas
                checkbox = ctk.CTkCheckBox(folder, text="", width=20, height=20)
                checkbox.place(x=10, y=10, )

                # Tombol opsi kanan atas
                option_btn = ctk.CTkButton(
                    folder,
                    text="⋮",
                    width=24,
                    height=24,
                    fg_color="transparent",
                    hover=False,
                    font=ctk.CTkFont("Arial", 26, weight="bold"),
                    text_color="black"
                )
                option_btn.place(relx=1.0, x=-5, y=5, anchor="ne")
                option_btn.bind("<Button-1>", partial(self.show_options, name=f"Folder {i}-{j}"))

                # Ikon gambar
                icon_label = ctk.CTkLabel(folder, image=self.folder_icon_ref, text="")
                icon_label.pack(pady=(25, 2))  # Geser ke bawah supaya tidak tabrakan

                folder_text = ctk.CTkLabel(folder, text="Name of the Folder\n23 files", justify="center")
                folder_text.pack()

    def show_options(self, event, name="Folder"):
        menu = tk.Menu(self, tearoff=0, font=("Segoe UI", 13))  # Perbesar font di sini
        menu.add_command(label="Rename", command=lambda: print(f"Rename {name}"))
        menu.add_command(label="Delete", command=lambda: print(f"Delete {name}"))

        # Posisi popup
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
