#no1
def profil(nama,alamat,gender,hobi):
    print ("nama:",nama)
    print ("alamat:",alamat)
    print ("gender:",gender)
    print ("hobi:",hobi)
    #memanggil

profil("septian","bogor","laki laki","music")

#no2
def point(nilai):
   if nilai < 60:
       return "Gagal"
   elif 61 <= nilai <= 70:
       return "Cukup"
   elif 71 <= nilai <= 80:
       return "Baik"
   elif 81 <= nilai <= 100:
       return "Sangat Baik"
   else:
       return "Nilai tidak valid"

print(point(88))

#no3
def cetak_bilangan_ganjil(hasil):
    for z in range(1, hasil+1, 2):
        print(z,end=" ")

cetak_bilangan_ganjil(100)