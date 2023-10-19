def luas_kerucut (jarcut,selcut) :
    lkerucut = 22/7*jarcut*(jarcut+selcut)
    return lkerucut

def luas_segilima (s, sm) :
    import math
    tsegitiga = math.sqrt((sm**2 - (1/2*s)**2))
    luassegilima = (1.72*s*s) + 5*(1/2*s*tsegitiga)
    return luassegilima

def prisma_segilima (s, t) :
    lpersegi = s*t 
    lsegilima = 1.72*s*s
    luas_prisma = 5*(lpersegi) + 2*(lsegilima)
    return luas_prisma

ulang = "ya"
while ulang == "ya" :
    print("===============No.1===============")
    print("===Untuk Luas Permukaan Kerucut===")
    print("===============No.2===============")
    print("====Untuk Luas Permukaan Limas====")
    print("===============No.3===============")
    print("===Untuk Luas Permukaan Prisma ===")
    inp = str(input("Pilih nomor : "))

    if inp == "1" :
        jarcut = float(input("Masukkan Jari-jari : "))
        selcut = float(input("Masukkan Panjang Selimut : "))
        print(round(luas_kerucut(jarcut,selcut),2))
    elif inp == "2" :
        s = float(input("Masukkan sisi : "))
        sm = float(input("Masukkan Panjang Selimut Miring: "))
        print(round(luas_kerucut(s, sm),2))
    elif inp == "3" :
        s = float(input("Masukkan sisi : "))
        t = float(input("Masukkan Tinggi Prisma: "))
        print(round(luas_kerucut(s, t),2))
    else :
        print("maaf pilihan cuma ada 3 kang")
    ulang = str(input("Ulang kah ? "))
    if ulang != "ya" :
        print("MAKASEHHH")

# def inputan_kerucut () :
#     input = 
# def inputan_limas () :
# def inputan_prisma ()
