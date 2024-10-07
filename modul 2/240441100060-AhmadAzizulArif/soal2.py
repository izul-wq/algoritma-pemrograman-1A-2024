karakter1 = "jaka"
karakter2 = "Ida"

# diketahui skor jaka
skor_jaka = 1100
ipk_jaka = 3.5
# diketahui skor ida
skor_ida = 1000
ipk_ida = 3.5
# syarat skor
syarat_skor = 1100
syarat_ipk = 3.0

# perintah if else
if skor_jaka >= syarat_skor and ipk_jaka >= syarat_ipk:
    print(f"{karakter1} lulus Beasiswa")
else:
    print(f"{karakter1} tidak lulus Beasiswa karena nilainya kurang")

# perintah if else
if skor_ida >= syarat_skor and ipk_ida >= syarat_ipk:
    print(f"{karakter2} lulus Beasiswa")
else:
    print(f"{karakter2} tidak lulus Beasiswa karena nilainya kurang")