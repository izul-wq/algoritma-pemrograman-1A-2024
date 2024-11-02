def fibonacci(n):
    if  n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

angka = int(input("Masukkan angka: "))
if  angka < 0:
    print("Jangan masukkan angka negatif")
else:
    for i in range(1, angka + 1):
        print(fibonacci(i), end=" ")