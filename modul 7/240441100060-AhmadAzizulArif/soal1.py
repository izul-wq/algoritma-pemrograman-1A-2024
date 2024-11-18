alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}

# a. hari pertama
alat_kesehatan["pengukur tekanan darah"] += 2
alat_kesehatan["termometer"] += 3

alat_kesehatan["stetoskop"] += 4

alat_kesehatan["pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2

alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

alat_dipinjam = set()

for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        alat_dipinjam.add(alat)

print("Barang yang dipinjam oleh Heni adalah: ")

for barang in alat_dipinjam:
    print(f"{barang}: {alat_kesehatan[barang]}")
