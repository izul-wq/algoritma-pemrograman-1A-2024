def cek_palindrom(kata):
    kebalikan = ""
    for i in kata:
        kebalikan = i + kebalikan
    if kata == kebalikan:
        print(f"Kata {kata} adalah Palindrom")
    else:
        print(f"Kata {kata} adalah Bukan Palindrom")
    
kata = input("Masukkan kata: ")
if not kata.isalpha():
    print("Inputkan sebuah kata")
else:
    cek_palindrom(kata)