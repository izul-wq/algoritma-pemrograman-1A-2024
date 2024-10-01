# diketahui
S5 = 5
suku5 = 11
suku8_suku12 = 52
nilai_8_pertama = 8

a = S5 - 1
# mencari perbedaan antara suku 8 dan suku 12
hasil_perbedaan = (suku8_suku12 - 2 * suku5) / a

# menghitung suku pertama
suku_pertama = suku5 - a * hasil_perbedaan

# menghitung nilai dai 8 pertama 
nilai_suku_ke8 = (nilai_8_pertama // 2) * (2 * suku_pertama + (nilai_8_pertama - 1) * hasil_perbedaan)

# output
print(nilai_suku_ke8)