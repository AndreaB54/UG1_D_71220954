print("="*20, "KASIR", "="*20)

harga_barang = int(input("Harga Barang : "))

#pilih
pilihan = str(input("Apakah anda membeli barang lagi ? [yes/no] : "))
if pilihan.lower() == "yes" :
	while True:
		harga_barang2 = int(input("Harga Barang : "))
		tanya = str(input("Apakah anda membeli barang lagi [yes/no] : "))
		break
elif pilihan.lower() == "no" :
	jumlah = harga_barang + harga_barang2
	print("TOTAL BELANJA : ", jumlah)
else:
	print("INVALID")