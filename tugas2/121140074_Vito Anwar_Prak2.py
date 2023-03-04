#Praktikum 2
#Vito Anwar_121140074_rb

class Vito :
    def __init__(self, nama, nim, kelas, sks, angkatan, status):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
        self.angkatan = angkatan
        self.status = status
    
    def bermain(self):
        print(self.nama, "sedang bermain game")

    def tambah_sks(self, n):
        self.sks += n

    def melanggar_aturan(self):
        if self.status == "Mahasiswa Dikeluarkan !!!":
            self.status = self.status
        elif self.status == "Surat Peringatan 3":
            self.status = "Mahasiswa Dikeluarkan !!!"
        elif self.status == "Surat Peringatan 2":
            self.status = "Surat Peringatan 3"
        elif self.status == "Surat Peringatan 1":
            self.status = "Surat Peringatan 2"
        else :
            self.status = "Surat Peringatan 1"

    def cetak(self):
        print("-----------------------------------------")
        print("Nama     : ", self.nama)
        print("NIM      : ", self.nim)
        print("Kelas    : ", self.kelas)
        print("SKS      : ", self.sks)
        print("Angkatan : ", self.angkatan)
        print("Status   : ", self.status)
        print("-----------------------------------------")
    
vito = Vito("Vito Anwar", 121140074, "RB", 20, 2021, "Mahasiswa Aktif")

vito.cetak()

print()
print("C untuk cetak data")
print("T untuk tambah sks")
print("B untuk fungsi bermain")
print("M untuk fungsi melanggar")
print("S untuk Keluar Program.")
stop = False
while stop == False:
    button = input("input pilihan :")
    if button == "C":
        vito.cetak()
    elif button == "T":
        n = int(input("tambah berapa sks : "))
        vito.tambah_sks(n)
    elif button == "B":
        vito.bermain()
    elif button == "M":
        vito.melanggar_aturan()
    else :
        stop = True
