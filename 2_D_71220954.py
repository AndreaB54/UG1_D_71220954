# kalimat = str(input("Kalimat yang ingin diteliti : "))
# kata = str(input("Kata yang dicari : "))

# def menghitung ():
#     hasil = ""
#     for kata in kalimat :
#         huruf_kecil = kalimat.lower()
#         hasil = kalimat.count(kata)
#     return hasil

# print("\nJumlah kata yang dicari : ", menghitung())

# def menghitung ():
#     hasil = ""
#     for kata in kalimat :
#         huruf_kecil = kalimat.lower()
#         hasil = kalimat.count(kata)
#     return hasil

angka = str(input("Masukkan angka : "))
hitung = str(input("Masukkan angka yg dihitung : "))

def menghitung():
    hasil = ""
    for hitung in angka : 
        huruf_kecil = angka.lower()
        hasil = angka.count(hitung)
    return hasil
print("Angka", hitung, "muncul sebanyak", menghitung(), "kali")