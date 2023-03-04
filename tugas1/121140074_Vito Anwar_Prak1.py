#Vito Anwar_121140074_rb

username = ("informatika")
password = ("12345678")

i = int(1)

while(i <= 3):
   user = input("masukan username : ")
   passw = input("masukan password : ")
   if(user == username and passw == password):
      print("Login Berhasil")
      break
   elif(i == 3):
      print("Akun anda diblokir")
      break
   else:
      print("Username atau Password salah coba lagi")
      i += 1
