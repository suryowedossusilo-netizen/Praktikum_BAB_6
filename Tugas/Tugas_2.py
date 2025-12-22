def elemen_batas(arr):
    n = len(arr)

    left_max = [0] * n
    right_min = [0] * n

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    right_min[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], arr[i])

    for i in range(n):
        if arr[i] == left_max[i] and arr[i] == right_min[i]:
            return arr[i], i

    return -1, -1

n = int(input("Masukkan jumlah elemen: "))

arr = []
print("Masukkan elemen array:")
for _ in range(n):
    arr.append(int(input()))

hasil, idx = elemen_batas(arr)

print(f"\nInput: arr[] = {arr}")
print(f"Output: {hasil}")

if hasil != -1:
    print(
        f"Penjelasan: {hasil} posisi di dalam index {idx}. "
        f"Semua elemen di sebelah kiri arr[{idx}] lebih kecil dari itu "
        f"dan semua elemen di sebelah kanan lebih besar."
    )
else:
    print("Penjelasan: Tidak ada unsur seperti itu daalam array")
