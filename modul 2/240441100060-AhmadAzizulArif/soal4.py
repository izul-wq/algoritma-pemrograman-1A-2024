tahun = int(input("Masukkan tahun : "))

# Perintah if bersarang
if tahun % 400 == 0:
    print(f"Tahun {tahun} adalah Tahun Kabisat")
else:
    if tahun % 100 == 0:
        print(f"Tahun {tahun} Bukan Tahun Kabisat")
    else:
        if tahun % 4 == 0:
            print(f"Tahun {tahun} adalah Tahun Kabisat")
        else:
            print(f"Tahun {tahun} Bukan Tahun Kabisat")