print("PROGRAM MEMBANTU AMBAPPE MEMBUAT HIASAN LANTAI BERBENTUK BELAH KETUPAT")
print("-------------------------------------------------")
karakter = input("Masukkan karakter 'x' atau 'o': ")
baris = int(input("Masukkan berapa baris: "))

if karakter.lower() == "x" or karakter.lower() == "o":
    for i in range(baris):
        print(" " * (baris - i) + f" {karakter}" * (i + 1))      #baris = misal 5   i = 0 (index)   baris-i = 5-0= 7(spasi)    5-1= 4(spasi)
                #spasi                  karakter
    for j in range(baris - 1):
        print(" " * (j + 2) + f" {karakter}" * (baris - 1 - j))  # j = 0 (index) baris - 1 = 5 -1 = 4 perulangan. (j + 2)= 0 + 2 = 2 spasi. (baris - 1 - j)= 5 - 1 - 0 = 4
                #spasi                  karakter