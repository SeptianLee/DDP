
#buat variable list dengan value : [namakendaraan, jenis kendaraan, cckendaraan, warna kendaraan, roda kendaraan]
#tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan] 
#tambahkan setelah jenis kendaraan dengan value : [merk kendaraan]



kendaraan = [
    ["mobil", "SUV", "1800cc", "hitam", 4],
    ["motor", "matic", "100cc", "putih", 2],
    ["motor", "Bajaj", "100cc", "merah", 3]
]

hrgkendaraan = [2000, 200, 100]

mrkkendaraan = ["suzuki", "honda", "tvs"]

for i in range(len(kendaraan)):
    kendaraan[i].append(hrgkendaraan[i])
    kendaraan[i].insert(2, mrkkendaraan[i])

for data in kendaraan:
    print(data)




#buat program pythondengan match case untuk menghitung luas bangun datar
#jika pilih 1, maka menghitung luas persegi
#jika pilih 2, maka menghitung luas lingkaran
#jika pilih 2, maka menghitung segitiga




import math

def hitung_luas_persegi(sisi):
    return sisi ** 2

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def main():
    print("Program Menghitung Luas Bangun Datar")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    
    pilihan = int(input("Masukkan pilihan (1/2/3): "))
    
    match pilihan:
        case 1:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = hitung_luas_persegi(sisi)
            print(f"Luas persegi adalah {luas}")
        case 2:
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = hitung_luas_lingkaran(jari_jari)
            print(f"Luas lingkaran adalah {luas}")
        case 3:
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = hitung_luas_segitiga(alas, tinggi)
            print(f"Luas segitiga adalah {luas}")
        case _:
            print("Pilihan tidak valid")
    
if __name__ == "__main__":
    main()
