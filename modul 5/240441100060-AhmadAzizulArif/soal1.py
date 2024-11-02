def calculate_discount(total_belanja, anggota):
    if anggota.lower() == "bronze":
        diskon_anggota = 5
    elif anggota.lower() == "silver":
        diskon_anggota = 10
    elif anggota.lower() == "gold":
        diskon_anggota = 15
    else:
        diskon_anggota = 0
    
    if total_belanja > 1000000:
        diskon_belanja = 5
    else:
        diskon_belanja = 0
    
    mendapatkan_diskon = diskon_anggota + diskon_belanja
    total_diskon = total_belanja * (mendapatkan_diskon / 100)
    total_harga = total_belanja - total_diskon

    return total_belanja, total_harga, mendapatkan_diskon

while True:
    total_belanja = int(input("Masukkan total belanja Anda: Rp"))
    anggota = input("Anda sebagai anggota apa? [bronze/silver/gold/bukan anggota] ")
    total_belanja, total_harga, mendapatkan_diskon = calculate_discount(total_belanja, anggota)

    print(f"Anda mendapatkan diskon sebesar {mendapatkan_diskon}%")
    print("Total belanja anda sebesar Rp", total_belanja)
    print("Total belanja anda setelah diskon sebesar Rp", int(total_harga))
    print()
    
    konfirmasi = input("Apakah anda ingin mengulanginya lagi? [ya/tidak] ")
    if konfirmasi != "ya":
        break
    print()