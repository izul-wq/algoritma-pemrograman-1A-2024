# Andi mempunyai celengan berbentuk balok dan taung, hitunglah volume dari kedua celengan miliknya tersebut!
# Diketahui
# Ukuran celengan balok
panjang_celengan_balok = 20 # cm
lebar_celengan_balok = 13 # cm
tinggi_celengan_balok = 7 # cm

# untuk menghitung volume celengan balok menggunakan rumus "V = p * l * t"
volume_celegan_balok = panjang_celengan_balok * lebar_celengan_balok * tinggi_celengan_balok

# output celengan balok
print("Volume celengan balok Andi adalah :")
print(volume_celegan_balok,"cm^3")

# Ukuran celengan tabung
pi = 22 // 7
diameter_celengan_tabung = 14 # cm
LuasSelimut_celengan_tabung = 440 # cm^2

# untuk menghitung volume celengan tabung menggunakan rumus "V = pi * (jari-jari**2) * t"
# dikarenakan jari-jarinya belum diketahui jadi harus menghitung jari-jarinya dulu dengan rumus "jari-jari = diameter / 2"
jari_jari = diameter_celengan_tabung // 2

# dikarenakan tingginya juga belum diketahui jadi harus menghitung tingginya dulu dengan rumus "tinggi = luas selimut / (2 * pi * jari-jari)"
tinggi_celengan_tabung = LuasSelimut_celengan_tabung // (2 * pi * jari_jari)

# setelah diketahui jari-jari dan tinggi nya sekarang menghitung volume nya
volume_celegan_tabung = pi * (jari_jari**2) * tinggi_celengan_tabung

# Output celengan tabung
print("Volume celengan tabung Andi adalah :")
print(volume_celegan_tabung,"cm^3")