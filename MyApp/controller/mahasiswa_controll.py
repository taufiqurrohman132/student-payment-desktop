from model.mahasiswa import MahasiswaModel

class MahasiswaController:
    def __init__(self):
        self.model = MahasiswaModel()
        self.asc = "ASC"
        self.desc = "DESC"

        self.kolom_sort = {
            "Terbaru": ("id_mhs", self.desc),
            "Terlama": ("id_mhs", self.asc),
            "NIM": ("nim", self.asc),
            "Nama": ("nama", self.asc),
            "Semester": ("semester", self.asc),
            "Tahun Masuk": ("tahunmasuk", self.asc),
        }

        self.kondisi_status = {
            "Sudah Lunas": "Paid",
            "Belum Lunas": "Pending",
        }

    def ambil_data(self, sort_key="Terbaru", status_filter="Sudah Lunas"):
        kolom, arah = self.kolom_sort.get(sort_key, ("id_mhs", self.desc))
        status = self.kondisi_status.get(status_filter, None)
        return self.model.ambil_data(kolom, arah, status)
    
    def ambil_data_by_nim(self, nim):
        return self.model.ambil_data_by_nim(nim)
  
    def tambah(self, data_tuple):
        print("ini data tuple",*data_tuple)
        self.model.simpan(*data_tuple)

    def hapus_data(self, nim):
        self.model.hapus_data(nim)  