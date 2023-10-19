def faktorial_1 (n) :
    if n == 0 :
        return 1
    else :
        return n*faktorial_1(n-1)

nilai = int(input("angka : "))
if nilai < 0 :
    print("eror")
else :
    print(faktorial_1(nilai))