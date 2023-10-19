def pangkat_1(b, p) :
    if p > 1 :
        return b*pangkat_1(b, 1)
    else : 
        return b
    
print("===============Selamat Datang===============")
print("==Di Program Penghitung Bilangan Pangkat 2==")
bilangan = int(input("Masukkan Angka : "))
pangkat = 2

print(" Hasil Pangkat 2 nya adalah ", pangkat_1(bilangan,pangkat))