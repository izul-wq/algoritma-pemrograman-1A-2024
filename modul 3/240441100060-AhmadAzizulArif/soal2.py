print("Selamat datang di program membalikkan angka milik Sudarso!")
print("----------------------------------------------------------")

while True:
    angka = input("Masukkan Angka: ")
    membalikkan_angka = ""

    for digit in angka:
        membalikkan_angka = digit + membalikkan_angka
    print(membalikkan_angka)

    konfirmasi = input("Apakah mau mengulanginya lagi? [ya/tidak] ")
    if konfirmasi == "tidak":
        break