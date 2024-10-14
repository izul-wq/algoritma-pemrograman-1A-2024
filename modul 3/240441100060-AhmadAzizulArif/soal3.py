print("Toko penyewaan DVD milik Juminten")
while True:
    lama_minjam = int(input("Masukkan hari keberapa anda mengembalikkan DVD: "))
    total_denda = 0
    if lama_minjam >= 5:
        denda_dibawah_10 = lama_minjam - 5
        total_denda += denda_dibawah_10 * 2500 
        
    if lama_minjam >= 10:
        denda_diatas_10 = lama_minjam - 10
        total_denda += (denda_diatas_10 // 5) * 5500
                
    if total_denda > 0:
        print(f"Anda mendapatkan denda sebesar Rp.{total_denda:,}")
    else:
        print(f"Anda meminjan selama {lama_minjam} hari jadi tidak terkena denda")
    
    konfirmasi_user = input("Apdakah Anda ingin menghitungnya lagi? [ya/tidak]")
    if konfirmasi_user != "ya":
        print("Terimakasih")
        break