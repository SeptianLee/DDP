



#TUGAS 2
total = 0
n = 1

while n <= 19:
    total += n
    n += 2

print("1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 =", total)




#TUGAS 3
jumlah_baris = int(input("Masukkan jumlah baris: "))

for baris in range(1, jumlah_baris + 1):
    for kolom in range(baris):
        print("*", end=" ")
    print()

