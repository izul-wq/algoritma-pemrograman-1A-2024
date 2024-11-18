siswa_basket = {"Asep", "Budi", "Agus", "Ucup", "Amel", "Farah"}
siswa_renang = {"Budi", "Agus", "Gatot", "Cecep", "Amel", "Tiara"}

def kedua_klub():
    siswa_kedua_klub = siswa_basket.intersection(siswa_renang)
    print("Siswa yang mengikuti kedua klub:")
    for siswa in siswa_kedua_klub:
        print(siswa, end=" ")

def satu_klub():
    siswa_hanya_basket = siswa_basket - siswa_renang
    siswa_hanya_renang = siswa_renang - siswa_basket
    siswa_hanya_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)

    print("\n\nSiswa yang hanya mengikuti satu klub:")
    for siswa in siswa_hanya_satu_klub:
        print(siswa, end=" ")

def siswa_unik():
    siswa_unik = siswa_basket.union(siswa_renang)
    print("\n\nDaftar semua siswa unik yang mengikuti setidaknya satu klub:")
    for siswa in siswa_unik:
        print(siswa, end=" ")
    jumlah_siswa_unik = len(siswa_unik)
    print("\n\nJumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)
    
kedua_klub()
satu_klub()
siswa_unik()