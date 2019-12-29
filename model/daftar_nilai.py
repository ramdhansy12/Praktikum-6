data= { }
def tambah_data (nama, nim , tugas, uts, uas) :
    nilaiakhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
    data[nama] = nama, nim, tugas, uts, uas,nilaiakhir

def ubah_data(nama) :
    if nama in data.keys():
        del data[nama]
        print("\n==========Inputkan Data Baru===========")
        from view.input_nilai import inputan
        inputan()
    else :
        print("======================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("======================")
        print("(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

def cari_data(nama):
    if nama in data.keys():
        print("\n|===================================================================|")
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("|===================================================================|")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |"
              .format(nama, data[nama][1], data[nama][2],data[nama][3], data[nama][4], data[nama][5]))
        print("|===================================================================|")
    else:
        print("===========================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("===========================")

def hapus_data(nama):
    if nama in data.keys():
        del data[nama]
        print('Nama Berhasil dihapus')
        return True
    else:
        print("===========================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("===========================")
        return False
