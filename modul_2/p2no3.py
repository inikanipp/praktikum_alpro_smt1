print("=== Gunting, Batu, Kertas ===")

suit1 = str(input("Masukkan Suit 1 : ").lower())
suit2 = str(input("Masukkan Suit 2 : ").lower())

if suit1 == "gunting" :
    if suit2 == "batu" :
        print("Pemenang : Batu")
    elif suit2 == "kertas" :
        print("Pemenang : gunting")
    elif suit2 == "gunting" :
        print("Seri")
    else :
        print("Maaf Tidak Terdefinisi")
elif suit1 == "batu" :
    if suit2 == "gunting" :
        print("Pemenang : batu")
    elif suit2 == "kertas" :
        print("Pemenang : kertas")
    elif suit2 == "batu" :
        print("Seri")
    else :
        print("Maaf Tidak Terdefinisi")
elif suit1 == "kertas" :
    if suit2 == "batu" :
        print("Pemenang : kertas")
    elif suit2 == "gunting" :
        print("Pemenang : gunting")
    elif suit2 == "kertas" :
        print("Seri")
    else :
        print("Maaf Tidak Terdefinisi")
else :
    print("Maaf Tidak Terdefinisi")