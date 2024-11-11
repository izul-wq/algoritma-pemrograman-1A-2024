def welcome_message(title):
    style = "=" * (len(title) + 6)
    print(style)
    print(f"== {title} ==")
    print(style)
    print()

def list_karyawan():
    data_karyawan = []
    i = 0
    while True:
        print(f"Masukkan data karyawan ke-{i+1}: ")
        
        while True:
            nip = input("Masukkan NIP: ")
            if nip.isdigit():
                break
            else:
                print("!! NIP HARUS BERUPA ANGKA !!")
        
        nama = input("Masukkan nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")
        
        karyawan = [nip, nama, alamat, departemen, jabatan]
        data_karyawan.append(karyawan)
        print()
        i += 1
        
        if i >= 5:
            konfirmasi = input("Apakah Anda ingin menambahkan karyawan lagi? (y/n): ")
            if konfirmasi.lower() != "y":
                break
            
    return data_karyawan

def mencari_karyawan(list_karyawan, pilihan, kunci):
    hasil_cari = []
    
    for karyawan in list_karyawan:
        if pilihan  == "1" and kunci in karyawan[0]: #Untuk NIP
            hasil_cari.append(karyawan)
        elif pilihan == "2" and kunci.lower() in karyawan[1].lower():    #Untuk nama
            hasil_cari.append(karyawan)
        elif pilihan == "3" and kunci.lower() in karyawan[2].lower():    #Untuk alamat
            hasil_cari.append(karyawan)
        elif pilihan == "4" and kunci.lower() in karyawan[3].lower():    #Untuk departemen
            hasil_cari.append(karyawan)
        elif pilihan == "5" and kunci.lower() in karyawan[4].lower():    #Untuk jabatan
            hasil_cari.append(karyawan)

    return hasil_cari

welcome_message("Program Mencari Karyawan")

data_karyawan = list_karyawan()

while True:
    print("\nPilih menu mencari karyawan:")
    print("1. NIP\n2. Nama\n3. Alamat\n4. Departemen\n5. Jabatan\nKetik 'exit' untuk keluar")
    pilihan = input("Masukkan pilhan menu (1-5): ")
    
    if pilihan.lower() == 'exit':
        exit()
    
    while not (pilihan == "1" or pilihan == "2" or pilihan == "3"or pilihan == "4" or pilihan == "5"):
        print("!! PILIHAN MENU HARUS 1-5 !!")
        pilihan = input("Masukkan pilhan menu (1-5): ")
    
    kunci = input("Masukkan kata kunci yang ingin dicari: ")
    
    hasil_cari = mencari_karyawan(data_karyawan, pilihan, kunci)
    if hasil_cari:
        print("\nHasil pencarian")
        for karyawan in hasil_cari:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan {karyawan[4]}")
    else:
        print("Tidak ada karyawan yang ditemukan")