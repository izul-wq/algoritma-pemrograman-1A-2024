print("Selamat datang di bar")
print("-----------------------")

nama = input("Masukkan nama anda : ")
usia = int (input("Masukkan usia anda : "))

diskon_member = 0
diskon_belanja = 0

# perintah if bersarang
if usia < 18:
    print("Maaf usia anda belum mencukupi")
    exit()
else:
    total_belanja = int(input("Masukkan total belanja anda Rp "))
    kartu_member = input("Apakah anda memiliki kartu member? [ya/tidak] : ").lower()
    if kartu_member == "ya":
        diskon_member += 15 # menyatakan diskon 15
    elif kartu_member == "tidak":
        print("Kamu tidak mendapatkan diskon")
    
    if total_belanja > 500000:
        diskon_belanja += 10 # menyatakan diskon 10

# Perumusan
mendapatkan_diskon = diskon_member + diskon_belanja
total_diskon = total_belanja * (mendapatkan_diskon / 100)
total_harga = total_belanja - total_diskon
    
print(f"diskon yang didapatkan {nama} sebanak {mendapatkan_diskon}%")
print(f"Jadi total harga pembelian minuman {nama} sebelum diskon Rp {total_belanja}")
print(f"Jadi total harga pembelian minuman {nama} setelah diskon Rp {total_harga}")