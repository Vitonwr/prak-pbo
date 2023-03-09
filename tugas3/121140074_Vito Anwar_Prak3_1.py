class AkunBank:
    list_pelanggan = []
  
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan.append(self)
    
    def lihat_menu(self):
        print("** Selamat datang di Bank Jago **")
        print("Halo ", self.__nama_pelanggan, " ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
    
    def lihat_saldo(self):
        print(self.__nama_pelanggan, " memiliki saldo Rp ", self.__jumlah_saldo)
        print()
    
    def tarik_tunai(self):
        jumlah_tarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if jumlah_tarik > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= jumlah_tarik
            print("Saldo berhasil ditarik!")
        print()
    
    def transfer(self):
        nominal_transfer = int(input("Masukkan nominal yang ingin ditransfer: "))
        no_tujuan = int(input("Masukkan no rekening tujuan: "))
        for pelanggan in self.__class__.list_pelanggan:
            if pelanggan.__no_pelanggan == no_tujuan:
                if nominal_transfer > self.__jumlah_saldo:
                    print("Nominal saldo yang Anda punya tidak cukup!")
                    print()
                    return
                else:
                    pelanggan.__jumlah_saldo += nominal_transfer
                    self.__jumlah_saldo -= nominal_transfer
                    print("Transfer Rp ", nominal_transfer, " ke ", pelanggan.__nama_pelanggan, " sukses!")
                    print()
                    return

        print("No rekening tujuan tidak dikenal! Kembali ke menu utama .......")
        print()

Akun1 = AkunBank(1234, "Vito Anwar", 5000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)
Akun4 = AkunBank(2708, "Anatasya Anwar", 202100000)
Akun5 = AkunBank(2410, "Miko Anwar", 10000000)
Akun6 = AkunBank(2102, "Hilman Nur Anwar", 15000000)

Akun1.lihat_menu()

stop = False;
while not stop:
    menu = input("Masukkan nomor input: ")
    if menu == "1":
        Akun1.lihat_saldo()
    elif menu == "2":
        Akun1.tarik_tunai()
    elif menu == "3":
        Akun1.transfer()
    elif menu == "4":
        break
    else:
        print("Input tidak valid! Silakan ulangi.")
    Akun1.lihat_menu()
