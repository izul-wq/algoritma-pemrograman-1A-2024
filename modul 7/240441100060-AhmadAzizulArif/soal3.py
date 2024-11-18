kelas = {}

def tambah_siswa():
    nama = input("Nama siswa: ")
    asal_sekolah = input("Asal sekolah: ")
    plotting = input("Plotting bimbingan: ")

    kelas_dengan_ruang = None
    for nama_kelas, siswa_list in kelas.items():
        if len(siswa_list) < 3:
            kelas_dengan_ruang = nama_kelas
            break

    if kelas_dengan_ruang:
        kelas[kelas_dengan_ruang].append({"nama": nama, "asal_sekolah": asal_sekolah, "plotting": plotting})
        print(f"Siswa {nama} berhasil ditambahkan ke {kelas_dengan_ruang}.")
    else:
        total_siswa = 0
        for siswa_list in kelas.values():
            total_siswa += len(siswa_list)
        
        nomor_kelas = total_siswa // 3 + 1
        kelas_nama = f"Kelas {nomor_kelas}"
        
        kelas[kelas_nama] = [{"nama": nama, "asal_sekolah": asal_sekolah, "plotting": plotting}]
        print(f"Siswa {nama} berhasil ditambahkan ke {kelas_nama}.")

def tampilkan_data():
    if not kelas:
        print("Belum ada data siswa.")
    else:
        for nama_kelas, siswa_list in kelas.items():
            print(f"{nama_kelas}:")
            no = 1
            for siswa in siswa_list:
                print(f"  {no}. Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}, Plotting: {siswa['plotting']}")
                no += 1

def update_siswa():
    tampilkan_data()
    nama_cari = input("Masukkan nama siswa yang akan diperbarui: ")

    for siswa_list in kelas.values():
        for siswa in siswa_list:
            if siswa["nama"].lower() == nama_cari.lower():
                print("Data ditemukan. Silakan masukkan data baru.")
                siswa["nama"] = input("Nama siswa baru: ") or siswa["nama"]
                siswa["asal_sekolah"] = input("Asal sekolah baru: ") or siswa["asal_sekolah"]
                siswa["plotting"] = input("Plotting bimbingan baru: ") or siswa["plotting"]
                print(f"Data siswa {nama_cari} berhasil diperbarui.")
                return
    
    print("Data siswa tidak ditemukan.")

def hapus_siswa():
    tampilkan_data()
    nama_cari = input("Masukkan nama siswa yang akan dihapus: ")

    for nama_kelas, siswa_list in kelas.items():
        for siswa in siswa_list:
            if siswa["nama"].lower() == nama_cari.lower():
                siswa_list.remove(siswa)
                if not siswa_list:
                    del kelas[nama_kelas]
                print(f"Data siswa {nama_cari} berhasil dihapus.")
                return
    
    print("Data siswa tidak ditemukan.")

def menu():
    while True:
        print("\n=== Menu Administrasi Siswa ===")
        print("1. Tambah Siswa")
        print("2. Tampilkan Data")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            update_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

menu()
