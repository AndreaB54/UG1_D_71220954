# print("="*20, "KASIR", "="*20)

# harga_barang = int(input("Harga Barang : "))

# #pilih
# pilihan = str(input("Apakah anda membeli barang lagi ? [yes/no] : "))
# if pilihan.lower() == "yes" :
# 	while True:
# 		harga_barang2 = int(input("Harga Barang : "))
# 		tanya = str(input("Apakah anda membeli barang lagi [yes/no] : "))
# 		break
# elif pilihan.lower() == "no" :
# 	jumlah = harga_barang + harga_barang2
# 	print("TOTAL BELANJA : ", jumlah)
# else:
# 	print("INVALID")

print(f"{20*'='} KASIR {20*'='}")
print()
harga_barang1 = int(input('Harga Barang : '))
total_harga = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_harga[0] = harga_barang1
n = 1

while True:
    pilihan = str(input('Apakah anda membeli barang lagi? [yes/no] : '))
    total_belanja = sum(total_harga)
    pilihan = pilihan.lower()
    if pilihan == 'yes':
        print()
        harga_barang2 = int(input('Harga Barang : '))
        total_harga[n] = harga_barang2
        n += 1
    elif pilihan == 'no':
        print(f'\nTOTAL BELANJA : {total_belanja}')
        break
    else:
        print('\nINVALID')