n = int(input("Masukkan jumlah elemen array: "))

arr = []
print("Masukkan elemen array:")
for i in range(n):
    elemen = int(input(f"Elemen ke-{i+1}: "))
    arr.append(elemen)

k = int(input("Masukkan nilai k: "))

batas = n // k

hasil = []
for i in set(arr):
    if arr.count(i) > batas:
        hasil.append(i)

print("\nInput: arr =", arr, ", k =", k)
print("Output:", hasil)
print(
    "Penjelasan: Di sini n/k adalah",
    batas,
    ", oleh karena itu elemen",
    hasil,
    "muncul lebih dari",
    batas,
    "kali dalam array."
)
