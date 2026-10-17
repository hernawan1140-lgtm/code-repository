print("=== PROGRAM PEMESANAN MAKANAN ===")

total = 0

jumlah_makanan = int(input("Berapa jenis makanan yang ingin dipesan? "))

for i in range(jumlah_makanan):
    print("\nMakanan ke-", i + 1)

    makanan = input("Nama makanan: ")
    harga = int(input("Harga makanan: Rp "))
    jumlah = int(input("Jumlah pesanan: "))

    subtotal = harga * jumlah
    total = total + subtotal

    print("Subtotal", makanan, ": Rp", subtotal)

print("\n=== STRUK PEMESANAN ===")
print("Total harga semua pesanan: Rp", total)
print("Terima kasih telah memesan!")