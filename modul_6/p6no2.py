mapala_1 = set()
badminton_1 = set()
teater_1 = set()
tari_1 = set()

mapala_1 = {"BUDI","ANI","JOKO","SITI","RINA","AGUS"}
badminton_1 = {"JOKO","SITI","EKA","RINI","HADI","DENI"}
teater_1 = {"ANI","DEDI","FIKA","MAYA","AHMAD"}
tari_1 = {"SITI","FIKA","GUSMAN","DWI","RANI","NANDA"}
lebih_1_ukm = set()
# penambahan data

def mapala () :
    print("==========| UKM MAPALA |=========")
    jnama = int(input("MASUKKAN JUMLAH NAMA : "))
    for a in range (jnama) :
        pecinta_alam = str(input(f"Masukkan Nama Ke - {a+1} : ").upper())
        mapala_1.add(pecinta_alam)
    print("=================================")
def badminton () :
    print("========| UKM BADMINTON |========")
    jnama = int(input("MASUKKAN JUMLAH NAMA : "))
    for a in range (jnama) :
        bulutangkis = str(input(f"Masukkan Nama Ke - {a+1} : ").upper())
        badminton_1.add(bulutangkis)
    print("=================================")
def initeater () :
    print("=========| UKM TEATER |==========")
    jnama = int(input("MASUKKAN JUMLAH NAMA : "))
    for a in range (jnama) :
        teater = str(input(f"Masukkan Nama Ke - {a+1} : ").upper())
        teater_1.add(teater)
    print("=================================")
def tari () :
    print("==========| UKM TARI |===========")
    jnama = int(input("MASUKKAN JUMLAH NAMA : "))
    for a in range (jnama) :
        tari_tradisional = str(input(f"Masukkan Nama Ke {a+1} : "))
        tari_1.add(tari_tradisional)
    print("=================================")

nama_dihapus = []
boxtidakikut_ukm = set()
nama_anggota = (mapala_1,badminton_1,teater_1,tari_1)

ulang = 1 
while ulang == 1 :
    print("======== NAMA ANGGOTA UKM =======")
    print("UKM MAPALA       : ", mapala_1)
    print("UKM BADMINTON    : ", badminton_1)
    print("UKM TEATER       : ", teater_1)
    print("UKM TARI         : ", tari_1)
    print("=================================")
    print( )
    print("===== PENDATAAN ANGGOTA UKM =====")
    print("=================================")
    print("===| NO. 1 UNTUK UPDATE DATA |===")
    print("===| NO. 2 UNTUK HAPUS DATA  |===")
    print("=================================")

    choose = int(input("MASUKKAN PILIHAN : "))
    if choose == 1 :
        print("========  UPDATE DATA   =========")
        print("====| NO. 1 UNTUK MAPALA    |====")
        print("====| NO. 2 UNTUK BADMINTON |====")
        print("====| NO. 3 UNTUK TEATER    |====")
        print("====| NO. 4 UNTUK TARI      |====")
        print("=================================")

        jumlah_pilihan = int(input('MASUKKAN JUMLAH PILIHAN : '))

        print("=================================")

        boxpilihan = []
        for i in range (jumlah_pilihan) : 
            pilihan = int(input(f"MASUKKAN PILIHAN KE {i+1}: "))
            if pilihan > 4 :
                print("TIDAK BISA, TIDAK BISA PILIHAN CUMA 4")
            else :
                boxpilihan.append(pilihan)

        for j in (boxpilihan) :
            if j == 1 :
                mapala()
            elif j == 2 :
                badminton()
            elif j == 3 :
                initeater()
            elif j == 4 :
                tari()

    elif choose == 2 :
        print("========== HAPUS DATA  ==========")
        print("|     NO. 1 HAPUS DI 1 UKM      |")
        print("|NO. 2 HAPUS DI LEBIH DARI 1 UKM|")
        print("=================================")
        jhapus = int(input("MASUKKAN PILIHAN : "))
        if jhapus == 1 :
            namahapus = str(input("MASUKKAN NAMA MAHASISWA : ").upper())
            print("=========== PILIH UKM  ==========")
            print("=======| NO. 1 MAPALA    |=======")
            print("=======| NO. 2 BADMINTON |=======")
            print("=======| NO. 3 TEATER    |=======")
            print("=======| NO. 4 TARI      |=======")
            ukmhapus = int(input("MASUKKAN PILIHAN UKM MAHASISWA : "))
            if ukmhapus == 1 :
                if namahapus not in mapala_1 :
                    print("NAMA TIDAK ADA DI UKM MAPALA")
                else :
                    mapala_1.remove(namahapus)
                    nama_dihapus.append(namahapus)
            elif ukmhapus == 2 :
                if namahapus not in badminton_1 :
                    print("NAMA TIDAK ADA DI UKM BADMINTON")
                else :
                    badminton_1.remove(namahapus)
                    nama_dihapus.append(namahapus)
            elif ukmhapus == 3 :
                if namahapus not in teater_1 :
                    print("NAMA TIDAK ADA DI UKM TEATER")
                else :
                    teater_1.remove(namahapus)
                    nama_dihapus.append(namahapus)
            elif ukmhapus == 4 :
                if namahapus not in tari_1 :
                    print("NAMA TIDAK ADA DI UKM TARI")
                else :
                    tari_1.remove(namahapus)
                    nama_dihapus.append(namahapus)
            else :
                print("MOHON CEK LAGI PILIHANNYA")

            for xyz in nama_dihapus :
                for namadelete in nama_anggota :
                    # print(xyz,namadelete)
                    if xyz in namadelete :
                        continue
                    else :
                        boxtidakikut_ukm.add(xyz)

        elif jhapus == 2 :
            namahapus = str(input("MASUKKAN NAMA MAHASISWA : ").upper())
            jumlahukm = []
            jukm = int(input('MASUKKAN JUMLAH UKM : '))
            if jukm <= 4 :
                for x in range(jukm) :
                    pukm = int(input(f"MASUKKAN PILIHAN UKM KE - {x+1}: "))
                    jumlahukm.append(pukm)
                for y in (jumlahukm) :
                    if y == 1 :
                        if namahapus not in mapala_1 :
                            print("NAMA TIDAK ADA DI UKM MAPALA")
                        else :
                            mapala_1.remove(namahapus)
                            nama_dihapus.append(namahapus)
                    elif y == 2 :
                        if namahapus not in badminton_1 :
                            print("NAMA TIDAK ADA DI UKM BADMINTON")
                        else :
                            badminton_1.remove(namahapus)
                            nama_dihapus.append(namahapus)
                    elif y == 3 :
                        if namahapus not in teater_1 :
                            print("NAMA TIDAK ADA DI UKM TEATER")
                        else :
                            teater_1.remove(namahapus)
                            nama_dihapus.append(namahapus)
                    elif y == 4 :
                        if namahapus not in tari_1 :
                            print("NAMA TIDAK ADA DI UKM TARI")
                        else :
                            tari_1.remove(namahapus)
                            nama_dihapus.append(namahapus)
                    else :
                        print("MAAF TIDAK ADA UKM DENGAN NO. ", y)
            else :
                print("PILIHAN JANGAN BANYAK BANYAK")
                
            for xyz in nama_dihapus :
                for namadelete in nama_anggota :
                    # print(xyz,namadelete)
                    if xyz in namadelete :
                        continue
                    else :
                        boxtidakikut_ukm.add(xyz)
        else :
            print("TIDAK BISA")

    else :
        print("KOK BISA MILIH LEBIH DARI 2")


    
    for angoota_1 in nama_anggota :
        for anggota_2 in nama_anggota :
            if angoota_1 == anggota_2 :
                continue
            else :
                lebih_1_ukm.update(angoota_1&anggota_2)

    kurang_dari_4 = []
    for ukm4 in nama_anggota :
        if len(ukm4) < 4 :
            kurang_dari_4.append(ukm4)
        else :
            continue

    kurang_dari_4_men = []

    for apapun in kurang_dari_4 :
        if apapun == mapala_1 :
            kurang_dari_4_men.append("MAPALA")
        elif apapun == badminton_1 :
            kurang_dari_4_men.append("BADMINTON")
        elif apapun == teater_1 :
            kurang_dari_4_men.append("TEATER")
        elif apapun == tari_1 :
            kurang_dari_4_men.append("TARI")


    fix_tdk_ikutukm = []
    
    for apacoba in boxtidakikut_ukm :
        if apacoba in mapala_1 :
            continue
        elif apacoba in badminton_1 :
            continue
        elif apacoba in teater_1 :
            continue
        elif apacoba in tari_1 :
            continue
        else :
            fix_tdk_ikutukm.append(apacoba)

    print("=================================")
    print("========= PENDATAAN UKM =========")
    print("|MAHASISWA YANG IKUT LEBIH 1 UKM|")
    print(" NAMA MAHASISWA : ", lebih_1_ukm)
    print("=================================")
    print("UKM DENGAN ANGGOTA KURANG DARI 4")
    print("UKM              : ", kurang_dari_4_men)
    print("=================================")
    print("=== MAHASISWA TIDAK IKUT UKM ====")
    print("NAMA             : ", fix_tdk_ikutukm)
    print( )
    ulang = int(input("MASUKKAN 1 UNTUK MENGULANG/ 2 UNTUK TIDAK : "))
    if ulang != 1 :
        print("ARIGATOU")

    






