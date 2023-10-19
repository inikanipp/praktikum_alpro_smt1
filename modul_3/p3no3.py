ulang = "ya"

while ulang == "ya" :
    hari = int(input("Masukkan Jumlah Hari : "))
    if hari <= 7 and hari >= 0 :
        print("Pengembalian Berhasil")
    elif hari > 7 :
        a = hari // 7
        totala = a*5000
        haritelat = hari-7
        total = haritelat*2000
        jumlah = totala + total
        print("Total Denda Anda = ",jumlah )
    else :
        print("Terjadi Kesalahan")

    ulang = str(input("Apakah Anda Ingin Mengulang Lagi ?").lower())
    if ulang != "ya" :
        print("Terima Kasih")