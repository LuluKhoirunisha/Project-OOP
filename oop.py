class Perpustakaan:
    def _init_(self, name):
        self.nama = name
        self.__buku = []

    def tambah_buku(self, buku):
        self.__buku.append(buku) 

    def tampilkan_buku(self):
        for buku in self.__buku:
         print(buku.info())
        
    def _str_(self):
        return f"Perpustakaan: {self.nama}"
    
class Buku:
    def _init_(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    
    def info(self):
        return f"Buku: {self.judul} oleh (self.penulis)"
    
class BukuFiksi(Buku):
    def _init_(self, judul, penulis, genre):
        super()._init_(judul, penulis)
        self.genre = genre

    def info(self):
        return f"Buku Fiksi: (self.judul) oleh {self.penulis}, Genre: {self.genre}"
    
class BukuNonFiksi(Buku):
    def _init_(self, judul, penulis, topik):
        super()._init_(judul, penulis)
        self.topik = topik

    def info(self):
        return f"Buku Non-fiksi: (self.judul) oleh {self.penulis}, Topik: {self.topik}"
    
Perpustakan = Perpustakaan("Perpustakaan Kota")

buku1 = BukuFiksi("Harry Potter", "J.K. Rowling", "fantasi")
buku2 = BukuNonFiksi("Sapiens", "Yuval Noah Harari", "Sejarah")

Perpustakaan.tambah_buku(buku1)
Perpustakaan.tambah_buku(buku2)

print(Perpustakaan)
Perpustakaan.tampilkan_buku()