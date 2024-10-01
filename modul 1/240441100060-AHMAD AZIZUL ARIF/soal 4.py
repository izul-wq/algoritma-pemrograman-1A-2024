# Bantu Darsoo untuk menghitung berapa banyak cara untuk membuat tim tersebut
# Darsono memiliki total 7 orang
orang = 7
# Darsono ingin memilih 4 orang untuk masuk kedalam timnya
memilih = 4

# berapa banyak cara untuk membentuk tim tersebut!
# faktorial 7
faktorial_orang = 7*6*5*4*3*2*1
# faktorial 4
faktorial_memilih = 4*3*2*1
# faktorial orang - faktorial memilih adalah 3 faktorial
faktorial_OrangMemilih = 3*2*1

# Rumus
banyak_cara = faktorial_orang // (faktorial_memilih * faktorial_OrangMemilih)

# Output banyak cara
print("Banyak cara untuk membuat timnya adalah :")
print(banyak_cara)

