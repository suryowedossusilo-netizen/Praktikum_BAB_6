n = int(input("Masukkan jumlah elemen: "))

arr = []
print("Masukkan elemen array:")
for _ in range(n):
    arr.append(int(input()))

k = int(input("Masukkan nilai k: "))

arr_urut = sorted(arr)
hasil = arr_urut[k - 1]

print(f"\nInput: arr[] = {arr}, k = {k}")
print(f"Output: {hasil}")
print(
    f"Penjelasan: Elemen terkecil ke-{k} dalam array yang diberikan adalah {hasil}."
)
