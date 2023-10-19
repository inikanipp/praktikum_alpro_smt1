print("SELAMAT DATANG DI PROGRAM PENGECEKAN NILAI ")
nama = str(input("Nama : "))
ntugas = float(input("Nilai Tugas : "))
nuts = float(input("Nilai UTS : "))
nuas = float(input("Nilai UAS : "))
ntugasa = float(input("Nilai Tugas Akhir :"))

total = ntugas+nuts+nuas+ntugasa
mean = total/4

if mean <= 40 and mean >= 0:
    print("NAMA : ", nama, ", NILAI : E")
elif mean <= 60 and mean >= 0:
    print("NAMA : ", nama, ", NILAI : D")
elif mean <= 70 and mean >= 0:
    print("NAMA : ", nama, ", NILAI : C")
elif mean <= 80 and mean >= 0:
    print("NAMA : ", nama, ", NILAI : B")
elif mean <= 100 and mean >= 0:
    print("NAMA : ", nama, ", NILAI : A")
else :
    print("NILAI TIDAK TERDEFINISI")