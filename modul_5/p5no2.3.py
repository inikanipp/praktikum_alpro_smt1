repeat = 1
while repeat == 1   :
    print("=============== Selamat Datang =================")
    print("========== Di Program Data Mahasiswa ===========")
    print("========== Jumlah Biodata Mahasiswa ============")
    print( )


    nama = []
    ininim = []
    inialamat = []
    iniprodi = []

    i = 0
    ulang = int(input("Masukkan JUmlah Biodata Mahasiswa : "))
    print( )
    while i < ulang :
        print("================================================")
        print(f"================ BIODATA KE {i+1} ==================")
        isinama = str(input('Masukkan Nama Mahasiswa     : ').upper())
        isinim = int(input('Masukkan NIM Mahasiswa      : '))
        isialamat = str(input('Masukkan Alamat Mahasiswa   : ').upper())
        isiprodi = str(input('Masukkan Prodi Mahasiswa    : ').upper())

        nama.append(isinama)
        ininim.append(isinim)
        inialamat.append(isialamat)
        iniprodi.append(isiprodi)

        i = i + 1

    kategori = ("Pilih Kategori Pencarian","NO. 1 Berdasarkan Nama", "NO. 2 Berdasarkan NIM","NO. 3 Berdasarkan Prodi","NO. 4 Berdasarkan Alamat")
    print("================================================")
    print(f"========|   {kategori[0]}  |=========")
    print(f"========|  {kategori[1]}     |=========")
    print(f"========|  {kategori[2]}      |=========")
    print(f"========|  {kategori[3]}    |=========")
    print(f"========|  {kategori[4]}   |=========")
    print( )

    inpt = str(input('Pilih Kategori Pencarian : '))
    print( )

    if inpt == "1" :
        data = str(input("Masukkan Nama : ").upper())
        if data not in nama :
            print("error")
        else :
            index = nama.index(data)
            print( )
            print("==================| BIODATA |==================")
            print("NAMA     : ", data )
            print("NIM      : ", ininim[index])
            print("Prodi    : ", iniprodi[index])
            print("Alamat   : ", inialamat[index])
            print("===============================================")
            print("===============================================")
            print( )
    elif inpt== "2" :
        data = int(input("Masukkan NIM : "))
        if data not in ininim :
            print("error")
        else :
            index = ininim.index(data)
            print( )
            print("==================| BIODATA |==================")
            print("NAMA     : ", nama[index])
            print("NIM      : ", data)
            print("Prodi    : ", iniprodi[index])
            print("Alamat   : ", inialamat[index])
            print("===============================================")
            print("===============================================")
            print( )
    elif inpt== "3" :
        data = str(input("Masukkan Prodi : ").upper())
        if data not in iniprodi :
            print("error")
        else :
            boxindex = []

            for noindex, noprodi in enumerate (iniprodi) :
                if data == noprodi :
                    boxindex.append(noindex)

            for vindex in boxindex :
                print( )
                print("==================| BIODATA |==================")
                print("NAMA     : ", nama[vindex])
                print("NIM      : ", ininim[vindex])
                print("Prodi    : ", data)
                print("Alamat   : ", inialamat[vindex])
                print("===============================================")
                print("===============================================")
                print( )
    elif inpt== "4" :
        data = str(input("Masukkan Alamat : ").upper())
        if data not in inialamat :
            print("error")
        else :
            boxindex = []

            for noindex, noalamat in enumerate (inialamat) :
                if data == noalamat :
                    boxindex.append(noindex)

            for vindex in boxindex :
                print( )
                print("==================| BIODATA |==================")
                print("NAMA     : ", nama[vindex])
                print("NIM      : ", ininim[vindex])
                print("Prodi    : ", iniprodi[vindex])
                print("Alamat   : ", data)
                print("===============================================")
                print("===============================================")
                print( )

    else :
        print(" ERORR COYY !!")
    print("=========== Apakah ingin Mengulang ? ==========")
    print("========= 1 Untuk YA/ 2 Untuk Tidak ===========")
    
    repeat = int(input("Masukkan Plihan : "))
    if repeat != 1 :
        print("================= Terima Kasih ================")
    

