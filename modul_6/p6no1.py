def panggil_1 () :
    nama = str(input("MASUKKAN NAMA : "))
    biodata["nama"] = nama

def panggil_2 () :
    alamat = str(input("MASUKKAN ALAMAT : "))
    biodata["alamat"] = alamat

def panggil_3 () :
    prodi = str(input("MASUKKAN PRODI : "))
    biodata["prodi"] = prodi

def panggil_4 () :
    semester = int(input("MASUKKAN SEMESTER : "))
    biodata["semester"] = semester

def panggil_5 () :
    angkatan = int(input("MASUKKAN ANGKATAN : "))
    biodata["angkatan"] = angkatan

def panggil_6 () :
    biodata["nama"] = "-"
    biodata["alamat"] = "-"
    biodata["prodi"]  = "-"
    biodata["semester"] = "-"
    biodata["angkatan"] = "-"

biodata = {"nama" : "SUSANTI",
           "alamat" : "SURAKARTA",
           "prodi" : "SISTEM INFORMASI",
            "semester" : 5,
            "angkatan" : 2015 }

def ini_biodata () :
    print("========== BIODATA MAHASISWI ==========")
    print("NAMA     : ",biodata["nama"])
    print("ALAMAT   : ",biodata["alamat"])
    print("PRODI    : ",biodata["prodi"])
    print("SEMESTER : ",biodata["semester"])
    print("ANGKATAN : ",biodata["angkatan"])
    print("=======================================")

repeat = 1
while repeat == 1 :
    ini_biodata()

    print("== APAKAH INGIN MEMPERBARUI BIODATA? ==")
    print("===== 1 UNTUK YA / 2 UNTUK TIDAK ======")
    perbarui = int(input('Masukkan Pilihan : '))
    print( )
    if perbarui == 1 :
        print("=======================================")
        print("=====|   PILIH PEMBARUAN         |=====")
        print("=====| NO. 1 UNTUK NAMA          |=====")
        print("=====| NO. 2 UNTUK ALAMAT        |=====")
        print("=====| NO. 3 UNTUK PRODI         |=====")
        print("=====| NO. 4 UNTUK SEMESTER      |=====")
        print("=====| NO. 5 UNTUK ANGKATAN      |=====")
        print("=====| NO. 6 UNTUK HAPUS BIODATA |=====")
        print("=======================================")
        print( )
        print("=======================================")
        print( )
        jpilih = int(input('MASUKKAN JUMLAH PILIHAN : '))
        
        print( )
        print("=======================================")
        print( )

        if jpilih <= 6 :
            boxpilih = []

            for i in range (jpilih) :
                update1 = int(input(f'MASUKKAN PILIHAN {i+1} : '))
                boxpilih.append(update1)

            for j in (boxpilih) :
                if j == 1 :
                    panggil_1()
                elif j == 2 :
                    panggil_2()
                elif j == 3 :
                    panggil_3()
                elif j == 4 :
                    panggil_4()
                elif j == 5 :
                    panggil_5()
                elif j == 6 :
                    panggil_6()
                else :
                    ("PILIHAN TYDACK ADA")
            print( )
            ini_biodata()
            print( )
            print(" APAKAH ANDA INGIN MENGULANG PROGRAM  ?")
            print("===== 1 UNTUK YA / 2 UNTUK TIDAK  =====")
            repeat = int(input("MASUKKAN PILIHAN : "))
            if repeat != 1 :
                print("============ TERIMA KASIH =============")
        else :
            print("=======================================")
            print("PILIHAN JANGAN BANYAK BANYAK BANG")
            print("=======================================")
            print( )
            print(" APAKAH ANDA INGIN MENGULANG PROGRAM  ?")
            print("===== 1 UNTUK YA / 2 UNTUK TIDAK  =====")
            repeat = int(input("MASUKKAN PILIHAN : "))
            if repeat != 1 :
                print("============ TERIMA KASIH =============")

    else :
        print(" APAKAH ANDA INGIN MENGULANG PROGRAM  ?")
        print("===== 1 UNTUK YA / 2 UNTUK TIDAK  =====")
        repeat = int(input("MASUKKAN PILIHAN : "))
        if repeat != 1 :
             print("============ TERIMA KASIH =============")
             
