n = int(input("Masukkan jumlah elemen array: "))

arr = []
print("Masukkan elemen array:")
for i in range(n):
    elemen = int(input(f"Elemen ke-{i+1}: "))
    arr.append(elemen)

minimum = arr[0]
for i in arr:
    if i < minimum:
        minimum = i

print("\nInput: arr[] =", arr)
print("Output:", minimum)
print("Penjelasan:", minimum, "adalah elemen minimum yang ada dalam array.")
