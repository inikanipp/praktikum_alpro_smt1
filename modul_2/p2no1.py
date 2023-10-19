print("SELAMAT DATANG DIPROGRAM PENGECEKAN UMUR")
umur = int(input("Masukkan Umur : "))

if umur > 50 :
    print("Tua")
elif umur > 25 :
    print("Dewasa")
elif umur > 17 :
    print("Muda")
elif umur > 7 :
    print("Anak-anak")
elif umur > 0 :
    print("Balita")
else :
    print("Umur Tidak Terdeteksi")