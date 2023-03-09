class Kelas:
    # deklarasi atribut kelas
    atribut = "Halo semua !!"
    
    def __init__(self, public, protected, private):
        # deklarasi atribut public
        self.public = public

        # deklarasi atribut protected
        self._protected = protected 

        # deklarasi atribut private
        self.__private = private 
        
    # membuat metode public
    def public_metode(self):
        print("Aku metode public!")
        
    # membuat metode protected
    def _protected_metode(self):
        print("Aku metode protected!")
    
    # membuat metode private
    def __private_metode(self):
        print("Aku metode private!")
        
        
# membuat objek dari kelas
objek = Kelas(123, 456, 789)

# mengakses atribut Kelas
print(objek.atribut)

# mengakses atribut public
print("Atribut public: ", objek.public)

# mengakses atribut protected
print("Atribut protected: ", objek._protected)

# mengakses atribut private harus berada didalam kelas
print("Atribut private: ", objek._Kelas__private)

# memanggil metode public
objek.public_metode()

# memanggil metode protected
objek._protected_metode()

# memanggil metode private harus berada didalam kelas
objek._Kelas__private_metode()
