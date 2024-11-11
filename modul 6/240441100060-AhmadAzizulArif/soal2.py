def welcome_message(title):
    style = "=" * (len(title) + 6)
    print(style)
    print(f"== {title} ==")
    print(style)

daftar_buku = [
    (1, "Rindu"),
    (2, "Pulang - Pergi"),
    (3, "Hujan"),
    (4, "Jingga dan Senja")
]

daftar_peminjam = []

def tampilkan_buku():
    print("\nDaftar Buku:")
    for i in daftar_buku:
        print(f"ID Buku: {i[0]}, Judul Buku: {i[1]}")

def pinjam_buku():
    tampilkan_buku()
    id_buku = int(input("\nMasukkan ID Buku yang ingin dipinjam: "))
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY): ")
    
    for buku in daftar_buku:
        if buku[0] == id_buku:
            id_peminjaman = len(daftar_peminjam) + 1
            peminjam = (id_peminjaman, id_buku, nama_peminjam, tanggal_peminjaman)
            daftar_peminjam.append(peminjam)
            print(f"Buku berhasil dipinjam. ID Peminjaman: {id_peminjaman}")
            return
        
    print("ID Buku Tidak Ditemukan")

def tampilkan_peminjam():
    if not daftar_peminjam:
        print("Tidak ada peminjam")
    else:
        print("\nDaftar Peminjam:")
        for peminjam in daftar_peminjam:
            print(f"ID Peminjaman: {peminjam[0]}, ID Buku: {peminjam[1]}, Nama Peminjam: {peminjam[2]}, Tanggal Peminjaman: {peminjam[3]}")

def perbarui_peminjaman():
    while True:
        konfirmasi = input("\nApakah Anda Tahu ID Peminjaman Anda? (y/n)")
        if konfirmasi == 'n':
            tampilkan_peminjam()
        elif konfirmasi == "y":
            id_peminjaman = int(input("\nMasukkan ID peminjaman yang ingin diperbarui: (Kalau tidak ya ketik ulang)"))
            for peminjam in daftar_peminjam:
                if peminjam[0] == id_peminjaman:
                    id_buku_baru = int(input("Masukkan ID Buku Baru! (Kalau tidak ya ketik ulang): "))
                    nama_baru = input("Masukkan Nama Baru! (Kalau tidak ya ketik ulang): ")
                    tanggal_baru = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY)! (Kalau tidak ya ketik ulang): ")
                    daftar_peminjam.remove(peminjam)
                    peminjam_baru = (id_peminjaman, id_buku_baru, nama_baru, tanggal_baru)
                    daftar_peminjam.append(peminjam_baru)
                    print("Data Berhasil Diperbarui")
                    return
            
            print("ID Buku tidak ada dalam daftar peminjaman")
        else:
            print("Masukkan yang benar")

def kembalikan_buku():
    while True:
        konfirmasi = input("\nApakah Anda Tahu ID Peminjaman Anda? (y/n)")
        if konfirmasi == 'n':
            tampilkan_peminjam()
        elif konfirmasi == "y":
            id_buku = int(input("Masukkan ID Peminjaman Anda: "))
            for peminjaman in daftar_peminjam:
                if peminjaman[0] == id_buku:
                    daftar_peminjam.remove(peminjaman)
                    print("Buku berhasil dikembalikan")
                    return
            print("ID Peminjaman tidak ada dalam daftar peminjaman")

def menu():
    welcome_message("SELAMAT DATANG DI PERPUSTAKAAN")
    
    while True:
        print("\nProgram Peminjaman Buku")
        print("1. Tampilkan Daftar Buku")
        print("2. Pinjam Buku")
        print("3. Tampilkan Peminjam Buku")
        print("4. Perbarui Peminjam Buku")
        print("5. Kembalikan Buku")
        print("6. Keluar")
        
        pilihan = input("Pilih Menu (1-6): ")
        
        if pilihan == "1":
            tampilkan_buku()
        elif pilihan =="2":
            pinjam_buku()
        elif pilihan == "3":
            tampilkan_peminjam()
        elif pilihan == "4":
            perbarui_peminjaman()
        elif pilihan == "5":
            kembalikan_buku()
        elif pilihan == "6":
            print("Terima Kasih")
            break
        else:
            print("Pilihan Tidak Tersedia")

menu()