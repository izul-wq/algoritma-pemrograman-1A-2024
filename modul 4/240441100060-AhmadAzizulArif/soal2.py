print("PROGRAM KONVERSI BILANGAN DESIMAL KE BINER MILIK MARTEEN FAIZ")
print("-------------------------------------------------")
angka = int(input("Masukkan angka: "))
digit = ""
while (angka>0):
    sisa_bagi = angka % 2
    digit = str(sisa_bagi) + digit
    print(digit)
    angka = angka // 2