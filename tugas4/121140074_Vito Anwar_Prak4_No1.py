class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk
        
class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        super().__init__(nama, jenis, harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

class Ram(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas

class Hdd(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas, rpm):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas
        self.rpm = rpm
        
class Vga(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas

class Psu(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya):
        super().__init__(nama, jenis, harga, merk)
        self.daya = daya

p1 = Processor('Processor','Core i7 7740X',4350000,'Intel',4,'4.3GHz')
p2 = Processor('Processor','Ryzen 5 3600',250000,'AMD',4,'4.3GHz')
ram1 = Ram('RAM','DDR4 SODimm PC19200/2400MHz',328000,'V-Gen','4GB')
ram2 = Ram('RAM','DDR4 2400MHz',328000,'G.SKILL','4GB')
hdd1 = Hdd('SATA','HDD 2.5 inch',295000,'Seagate','500GB',7200)
hdd2 = Hdd('SATA','HDD 2.5 inch',295000,'Seagate','1000GB',7200)
vga1 = Vga('VGA','VGA GTX 1050',250000,'Asus','2GB')
vga2 = Vga('VGA','1060Ti',250000,'Asus','8GB')
psu1 = Psu('PSU','Corsair V550',250000,'Corsair','500W')
psu2 = Psu('PSU','Corsair V550',250000,'Corsair','500W')

rakit = [[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]]

for i, komputer in enumerate(rakit):
    print("")
    print("Komputer ", i+1)
    for objek in komputer:
        print(objek.nama,  " ", objek.jenis, " produksi ", objek.merk)
