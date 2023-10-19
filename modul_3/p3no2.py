a = int(input("Masukkan Batas Awal Angka : "))
b = int(input("Masukkan Batas Akhir Angka : "))


if ((b < a or b == a) or ((a < 0 or b < 0))) :
    print(" Tolong Masukkan Batas Angka Dengan Benar")

else : 
    for i in range (a, b+1):
        if ((i == 2 or i == 3) or (i ==5 or i == 7)):
            print(i)
        if ((i % 2 == 0 or i % 3 == 0) or (i % 5 == 0 or i % 7 == 0)) :
            continue       
        if i == 1 :
            continue
        print(i)
