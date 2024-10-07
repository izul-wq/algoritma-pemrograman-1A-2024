perawat = "Sumanto"

print(f"Selamat Datang di Program BMI {perawat}")
print("-------------------------------------")

nama = input("Masukkan nama anda : ")
usia = int(input("Masukkan usia anda : "))

# perintah if
if usia < 18:
    print("Maaf anda belum dewasa")
    exit()

berat_badan = float(input("Masukkan berat badan anda (kg) : "))
tinggi_badan = float(input("Masukkan tinggi badan anda (m) : "))
BMI = berat_badan / (tinggi_badan**2)

print(BMI)
# perintah if elif 
if BMI < 18.5:
    print(f"{perawat}: {nama} anda Kurus, makanya makan")
elif BMI <= 24.9:
    print(f"{perawat}: Bagus {nama} BMI kamu Normal, pertahanin")
elif BMI <= 29.9:
    print(f"{perawat}: {nama} anda Gemuk, diet dong")
elif BMI >= 30:
    print(f"{perawat}: {nama} anda Obesitas, diet, olahraga yaa!")