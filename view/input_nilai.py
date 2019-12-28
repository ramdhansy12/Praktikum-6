def inputan():
    from model.daftar_nilai import tambah_data
    while (True):
        nama = input("NAMA   : ")
        if nama == '':
            print('Nama tidak boleh kosong')
        else:
            break
    while (True):
        try:
            nim = int(input("NIM    : "))
            if nim == '':
                print('Masukan Nim dengan Angka')
        except ValueError:
            print('Masukan Nim dengan Angka')
        else:
            break
    while (True):
        try:
            tugas = int(input("TUGAS  : "))
            if tugas == '':
                print('Masukan TUGAS dengan Angka')
        except ValueError:
            print('Masukan TUGAS dengan Angka')
        else:
            break
    while (True):
        try:
            uts = int(input("UTS    : "))
            if uts == '':
                print('Masukan UTS dengan Angka')
        except ValueError:
            print('Masukan UTS dengan Angka')
        else:
            break
    while (True):
        try:
            uas = int(input("UAS    : "))
            if uas == '':
                print('Masukan UAS dengan Angka')
        except ValueError:
            print('Masukan UAS dengan Angka')
        else:
            break
    tambah_data(nama, nim, tugas, uts, uas)
    print("(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")
def ubah():
    from model.daftar_nilai import ubah_data
    ubah_data(nama=input("Masukan nama yang ingin diubah : "))

def hapus():
    from model.daftar_nilai import hapus_data
    hapus_data(nama=input("Masukan nama yang ingin dihapus : "))
    print("(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

def cari():
    from model.daftar_nilai import cari_data
    cari_data(nama=input("Masukan nama yang di cari : "))