boxmakan = []
boxharga = []
boxindex = []

jumlah = int(input("Masukkan Jumlah Data Yang diinginkan : "))

for i in range (jumlah) :
    print(f"============ MAKANAN {i+1} ================")
    makan = str(input('Masukkan Makanan : '))
    boxmakan.append(makan)
    harga = int(input("Masukkan Harga   : "))
    boxharga.append(harga)
    print("=======================================")

for index, j in enumerate (boxmakan) :
    boxindex.append(index)

print( )

print("============ DAFTAR MENU ==============")
for k in boxindex :
    print(f"============ MAKANAN {k+1} ================")
    print("Makanan  :   ", boxmakan[k])
    print("Harga    :   ", boxharga[k])
    print("=======================================")

