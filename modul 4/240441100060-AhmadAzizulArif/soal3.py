nama = "Mas Ironi"

gaji_harian = 100000
max_lembur_perhari = 8
max_lembur_perminggu = 40
total_jam_lembur_mingguan = 0
total_gaji_lembur = 0
hari = 1

jam_lembur_hari1, gaji_lembur_hari1 = 0, 0
jam_lembur_hari2, gaji_lembur_hari2 = 0, 0
jam_lembur_hari3, gaji_lembur_hari3 = 0, 0
jam_lembur_hari4, gaji_lembur_hari4 = 0, 0
jam_lembur_hari5, gaji_lembur_hari5 = 0, 0
jam_lembur_hari6, gaji_lembur_hari6 = 0, 0
jam_lembur_hari7, gaji_lembur_hari7 = 0, 0

print(f"Program menghitung gaji {nama}")

while hari<=7:
    jam_lembur_harian = int(input(f"Berapa jam {nama} lembur pada hari ke-{hari}? (0,1,2,3,4,6,8): "))
    
    while not (jam_lembur_harian == 0 or jam_lembur_harian == 1 or jam_lembur_harian == 2 or jam_lembur_harian == 3 or jam_lembur_harian == 4 or jam_lembur_harian == 5 or  jam_lembur_harian == 6 or jam_lembur_harian == 7 or jam_lembur_harian == 8 or jam_lembur_harian > 8):
        print("Masukkan ulang jam lembur dengan sesuai perintah")
        jam_lembur_harian = int(input(f"Berapa jam {nama} lembur pada hari ke-{hari}? (0,1,2,3,4,6,8): "))
        
    # harian
    if jam_lembur_harian > max_lembur_perhari:
        print("Lembur melebihi batas, dan akan disesuaikan dengan maksimal lembur perhari")
        jam_lembur_harian = max_lembur_perhari
        
    # mingguan
    if total_jam_lembur_mingguan >= max_lembur_perminggu:
        print("TOTAL LEMBUR MINGGUAN MELEBIHI BATAS")
        jam_lembur_harian = 0
    else:
        sisa_lembur_harian = max_lembur_perminggu - total_jam_lembur_mingguan
        if jam_lembur_harian > sisa_lembur_harian:
            jam_lembur_harian = sisa_lembur_harian
    
    # menghitung total jam lembur mingguan
    total_jam_lembur_mingguan += jam_lembur_harian
    
    # gaji lembur perjam
    # tidak ada lembur
    if jam_lembur_harian == 0:
        gaji_lembur = 0
    # lembur 1 sampai 3 jam
    elif jam_lembur_harian < 4:
        gaji_lembur = jam_lembur_harian * 25000
    # lembur 4 jam
    elif jam_lembur_harian == 4:
        gaji_lembur = 100000
    # lembur 6 jam
    elif jam_lembur_harian == 5:
        gaji_lembur = 150000
    # lembur 6 jam
    elif jam_lembur_harian == 6:
        gaji_lembur = 200000
    # lembur 7 jam
    elif jam_lembur_harian == 7:
        gaji_lembur = 250000
    # lembur 8 jam
    elif jam_lembur_harian == 8:
        gaji_lembur = 300000
    
    if hari == 1:
        jam_lembur_hari1, gaji_lembur_hari1 = jam_lembur_harian, gaji_lembur
    elif hari == 2:
        jam_lembur_hari2, gaji_lembur_hari2 = jam_lembur_harian, gaji_lembur
    elif hari == 3:
        jam_lembur_hari3, gaji_lembur_hari3 = jam_lembur_harian, gaji_lembur
    elif hari == 4:
        jam_lembur_hari4, gaji_lembur_hari4 = jam_lembur_harian, gaji_lembur
    elif hari == 5:
        jam_lembur_hari5, gaji_lembur_hari5 = jam_lembur_harian, gaji_lembur
    elif hari == 6:
        jam_lembur_hari6, gaji_lembur_hari6 = jam_lembur_harian, gaji_lembur
    elif hari == 7:
        jam_lembur_hari7, gaji_lembur_hari7 = jam_lembur_harian, gaji_lembur

    # menghitung total gaji lembur
    total_gaji_lembur += gaji_lembur
    # menaikkan hari
    hari += 1
    
# gaji tanpa lembur
total_gaji_tanpa_lembur = 7 * gaji_harian

total_gaji_mingguan_dan_lembur = total_gaji_lembur + total_gaji_tanpa_lembur

print("-- LEMBUR PERHARI --")
print(f"{nama} lembur hari 1: {jam_lembur_hari1} jam, bonus lembur Rp{gaji_lembur_hari1}")
print(f"{nama} lembur hari 2: {jam_lembur_hari2} jam, bonus lembur Rp{gaji_lembur_hari2}")
print(f"{nama} lembur hari 3: {jam_lembur_hari3} jam, bonus lembur Rp{gaji_lembur_hari3}")
print(f"{nama} lembur hari 4: {jam_lembur_hari4} jam, bonus lembur Rp{gaji_lembur_hari4}")
print(f"{nama} lembur hari 5: {jam_lembur_hari5} jam, bonus lembur Rp{gaji_lembur_hari5}")
print(f"{nama} lembur hari 6: {jam_lembur_hari6} jam, bonus lembur Rp{gaji_lembur_hari6}")
print(f"{nama} lembur hari 7: {jam_lembur_hari7} jam, bonus lembur Rp{gaji_lembur_hari7}")

print("-- TOTAL GAJI MINGGUAN --")
print(f"Total jam lembur perminggu {nama} adalah {total_jam_lembur_mingguan} jam")
print(f"Total gaji lembur selama satu minggu {nama} sebesar Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur {nama} sebesar Rp{total_gaji_tanpa_lembur}")
print(f"Total gaji minguan dan lembur {nama} sebesar Rp{total_gaji_mingguan_dan_lembur}")