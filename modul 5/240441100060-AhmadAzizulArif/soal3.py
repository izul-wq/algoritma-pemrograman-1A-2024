def faktorial():
    while True:
        n = int(input("Masukkan angka faktorial: "))
        
        if n < 0:
            print("Faktorial tidak bisa dihitung karena angka negatif")
        hasil = 1
        print(n, "! = ", end="")
        
        for i in range(n, 0, -1):
            if i == 1:
                print(i, end="")
            else:
                print(i, "X ", end="")
            hasil = hasil * i
            
        print(" = ", hasil )
        print()
        konfirmasi = input("Apakah kamu ingin mengulanginya lagi? [ya/tidak] ")
        if konfirmasi != "ya":
            break

faktorial()