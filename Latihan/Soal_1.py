n = int(input("Masukkan jumlah elemen array: "))

arr = []
print("Masukkan elemen array (hanya 0 atau 1):")
for i in range(n):
    elemen = int(input(f"Elemen ke-{i+1}: "))
    arr.append(elemen)

jumlah = 0
for i in arr:
    if i == 1:
        jumlah += 1

print("\nInput: arr =", arr)
print("Output:", jumlah)
print("Penjelasan: Jumlah angka 1 dalam array yang diberikan adalah", jumlah)
