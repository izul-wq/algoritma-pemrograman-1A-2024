list_barang = []

def tambah_barang():
    while True:
        id_barang = input("Masukkan ID Barang (angka): ")
        if not id_barang.isdigit():
            print("!!ID barang harus berupa angka!!")
            continue
        id_barang = int(id_barang)
        
        for i in list_barang:
            if i['id'] == id_barang:
                print("!!Barang dengan ID tersebut sudah ada!!")
                break
        else:
            break
    nama_barang = input("Masukkan Nama Barang: ")
    prioritas = input("Prioritas Barang (Darurat, Biasa, Non-Darurat): ")
    while prioritas.lower() not in ["darurat", "biasa", "non-darurat"]:
        print("Masukkan sesuai dengan format yang ditentukan (darurat, biasa, non-darurat)")
        prioritas = input("Prioritas Barang (darurat, biasa, non-darurat): ")
    
    barang = {"id": id_barang, "nama": nama_barang, "prioritas": prioritas}
    
    if prioritas.lower() == "darurat":
        list_barang.insert(0, barang)
    elif prioritas.lower() == "biasa":
        for i in range(len(list_barang)):
            if list_barang[i]["prioritas"].lower() == "non-darurat":
                list_barang.insert(i, barang)
                return
        list_barang.append(barang)
    elif prioritas.lower() == "non-darurat":
        list_barang.append(barang)
    
def tampilkan_barang():
    print("\nDaftar Barang:")
    for i in list_barang:
        print(f"ID: {i["id"]}, Nama: {i["nama"]}, Prioritas: {i["prioritas"]}")

while True:
    tambah_barang()
    tampilkan_barang()
    
    konfirmasi = input("\nApakah Anda ingin menambah barang lagi? (y/n): ")
    if konfirmasi.lower() != "y":
        break

print("Terima Kasih!")