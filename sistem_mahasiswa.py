class Mahasiswa:
    # Class attribute untuk menghitung total object Mahasiswa yang dibuat
    _jumlah_mahasiswa = 0

    def __init__(self, nim, nama, prodi, ipk=0.0):
        # Validasi menggunakan static method sebelum menetapkan atribut
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError("NIM harus berupa angka dan minimal 8 digit!")

        # Public & protected attributes
        self.nim = nim
        self.nama = nama
        self._prodi = prodi

        # Private attribute (Encapsulation)
        self.__ipk = 0.0
        self.ipk = ipk  # Memanggil setter untuk validasi nilai awal

        Mahasiswa._jumlah_mahasiswa += 1

    # --- PROPERTY & SETTER (Encapsulation untuk atribut private __ipk) ---
    @property
    def ipk(self):
        return self.__ipk

    @ipk.setter
    def ipk(self, nilai):
        if 0.0 <= nilai <= 4.0:
            self.__ipk = float(nilai)
        else:
            raise ValueError("IPK harus berada di antara 0.00 sampai 4.00!")

    # --- INSTANCE METHOD ---
    def tampilkan_info(self):
        predikat = Mahasiswa.cek_predikat(self.__ipk)
        print(f"NIM      : {self.nim}")
        print(f"Nama     : {self.nama}")
        print(f"Prodi    : {self._prodi}")
        print(f"IPK      : {self.__ipk:.2f} ({predikat})")
        print("-" * 40)

    # --- CLASS METHOD ---
    @classmethod
    def total_mahasiswa(cls):
        return cls._jumlah_mahasiswa

    @classmethod
    def dari_string(cls, data_str):
        """Membuat object Mahasiswa dari format 'NIM-Nama-Prodi-IPK'."""
        nim, nama, prodi, ipk_str = data_str.split("-")
        return cls(nim.strip(), nama.strip(), prodi.strip(), float(ipk_str))

    # --- STATIC METHOD ---
    @staticmethod
    def validasi_nim(nim):
        """Memastikan NIM hanya berisi angka dan panjang minimal 8 karakter."""
        return str(nim).isdigit() and len(str(nim)) >= 8

    @staticmethod
    def cek_predikat(ipk):
        """Menentukan predikat kelulusan berdasarkan nilai IPK."""
        if ipk >= 3.51:
            return "Cum Laude"
        elif ipk >= 3.01:
            return "Sangat Memuaskan"
        elif ipk >= 2.76:
            return "Memuaskan"
        else:
            return "Perlu Perbaikan"


class SistemAkademik:
    def __init__(self, nama_kampus):
        self.nama_kampus = nama_kampus
        self.daftar_mahasiswa = []

    # --- INSTANCE METHOD ---
    def tambah_mahasiswa(self, mahasiswa):
        if isinstance(mahasiswa, Mahasiswa):
            self.daftar_mahasiswa.append(mahasiswa)
            print(f"[OK] Mahasiswa '{mahasiswa.nama}' berhasil ditambahkan.")
        else:
            print("[ERROR] Data bukan merupakan object Mahasiswa!")

    def cari_mahasiswa(self, nim):
        for mhs in self.daftar_mahasiswa:
            if mhs.nim == nim:
                return mhs
        return None

    def ubah_ipk(self, nim, ipk_baru):
        mhs = self.cari_mahasiswa(nim)
        if mhs:
            try:
                mhs.ipk = ipk_baru  # Menggunakan setter @ipk.setter
                print(f"[OK] IPK {mhs.nama} berhasil diperbarui menjadi {mhs.ipk:.2f}.")
            except ValueError as e:
                print(f"[GAGAL] {e}")
        else:
            print(f"[ERROR] Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def tampilkan_semua(self):
        print(f"\n=== DATA MAHASISWA - {self.nama_kampus.upper()} ===")
        if not self.daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return
        for mhs in self.daftar_mahasiswa:
            mhs.tampilkan_info()
        print(f"Total Object Mahasiswa Terdaftar: {Mahasiswa.total_mahasiswa()}")


def main():
    # Membuat object dari class SistemAkademik
    sistem = SistemAkademik("Universitas Banten Jaya")

    # Membuat object Mahasiswa secara langsung menggunakan __init__()
    mhs1 = Mahasiswa("14012500096", "Satria Panji Pangestu", "Ilmu Komputer", 3.85)
    mhs2 = Mahasiswa("14012500097", "Ahmad Hidayatulloh", "Ilmu Komputer", 3.45)

    # Membuat object Mahasiswa menggunakan @classmethod (dari_string)
    mhs3 = Mahasiswa.dari_string("14012500098 - Siti Aminah - Sistem Informasi - 3.60")

    sistem.tambah_mahasiswa(mhs1)
    sistem.tambah_mahasiswa(mhs2)
    sistem.tambah_mahasiswa(mhs3)

    # Menu interaktif sederhana di terminal
    while True:
        print("\n--- MENU SISTEM DATA MAHASISWA ---")
        print("1. Tampilkan Semua Data Mahasiswa")
        print("2. Tambah Mahasiswa Baru")
        print("3. Ubah IPK Mahasiswa (Uji Property/Setter)")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            sistem.tampilkan_semua()

        elif pilihan == "2":
            try:
                nim = input("Masukkan NIM   : ").strip()
                nama = input("Masukkan Nama  : ").strip()
                prodi = input("Masukkan Prodi : ").strip()
                ipk = float(input("Masukkan IPK   : ").strip())
                mhs_baru = Mahasiswa(nim, nama, prodi, ipk)
                sistem.tambah_mahasiswa(mhs_baru)
            except ValueError as e:
                print(f"[GAGAL] Input tidak valid: {e}")

        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa : ").strip()
            try:
                ipk_baru = float(input("Masukkan IPK baru (0.0 - 4.0): ").strip())
                sistem.ubah_ipk(nim, ipk_baru)
            except ValueError:
                print("[GAGAL] IPK harus berupa angka.")

        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()