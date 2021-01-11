from model.daftar_nilai import *
from view.view_nilai import *

while True:
    c = input("\nT)ambah, U)bah, C)ari, H)apus L)ist, K)eluar: ")

    if (c.lower() == 't'):
        tambah_data()

    elif (c.lower() == 'u'):
        ubah_data()

    elif (c.lower() == 'c'):
        cetak_hasil_pencarian()

    elif (c.lower() == 'h'):
        hapus_data()

    elif (c.lower() == 'l'):
        cetak_daftar_nilai()

    elif (c.lower() == 'k'):
        break

    else:
        print("Silahkan pilih menu yang tersedia!")