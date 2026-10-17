print("=== PROGRAM PEMESANAN MAKANAN ===")

total = 0

while True:
    makanan = input("Masukkan nama makanan: ")
    harga = int(input("Masukkan harga makanan: Rp "))
    jumlah = int(input("Masukkan jumlah pesanan: "))

    subtotal = harga * jumlah
    total += subtotal

    print("Makanan:", makanan)
    print("Subtotal: Rp", subtotal)
    print("-----------------------------")

    lanjut = input("Apakah ingin memesan lagi? (ya/tidak): ")

    if lanjut.lower() != "ya":
        break

print("\n=== STRUK PEMESANAN ===")
print("Total harga semua pesanan: Rp", total)
print("Terima kasih telah memesan!")