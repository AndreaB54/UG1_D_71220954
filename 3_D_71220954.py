jumlah_row = int(input("Masukkan Angka: "))
def pola(jumlah_row) :
    angka = 1
    while angka < jumlah_row :
        print(" " * (jumlah_row - angka) + "* " * angka)
        angka = angka + 1

    angka = jumlah_row
    while angka >= 1 :
        print(" " * (jumlah_row - angka) + "* " * angka)
        angka = angka - 1

pola(jumlah_row)