import time

print "_______PENDAFTARAN_______"
print "Silahkan Isilah semua di bawah ini"
nama=str(raw_input("Masukkan Nama Lengkap: "))
tanggal_lahir=str(raw_input("Masukkan Tanggal Lahir Anda: "))
Alamat=str(raw_input("Masukkan Alamat Anda: "))
print "Selamat datang "+nama+" Baik, Apakah anda memasukkan pendaftaran dengan Benar?"
print "Nama               : ",nama
print "Tanggal Lahir      : ",tanggal_lahir
print "Alamat             : ",Alamat
while True:
 x=str(raw_input("Apakah Anda ingin melanjutkan? Tekan (Y/N) untuk lanjut atau tidak!"))
 if x=='Y' or x=='y' or x=='Yes' or x=='yes' or x=='YES':
  print "Oke,kita lanjutkan..."
  x=str(raw_input("Buat Username:"))
  y=str(raw_input("Buat Password Baru:"))
  z=str(raw_input("Konfirmasikan Password: "))
  while True:
   if y==z:
    print "load..."
    time.sleep(7)
    print "Password cocok..."
    print "Silahkan anda login..."
    g=str(raw_input("Username: "))       
    p=str(raw_input("Password: "))
    if g==x and p==y:
     print "Login berhasil!"
     time.sleep(4)
     break
    else:
     print "Login gagal!,silahkan Coba lagi!!"
   else:
    print "Password tidak cocok"
    break
 elif x=='N' or x=='n' or x=='not' or x=='Not' or x=='NOT':
  print "keluar"
  break
 else:
  print "key yang anda masukkan salah!!"
                  
                
          
  
