def closest_pair(arr1, arr2, x):
    i = 0
    j = len(arr2) - 1

    min_diff = float('inf')
    best_a = 0
    best_b = 0

    while i < len(arr1) and j >= 0:
        jumlah = arr1[i] + arr2[j]
        diff = abs(jumlah - x)

        if diff < min_diff:
            min_diff = diff
            best_a = arr1[i]
            best_b = arr2[j]

        if jumlah > x:
            j -= 1
        elif jumlah < x:
            i += 1
        else:
            break

    return best_a, best_b, min_diff

print("Array HARUS sudah terurut (ascending)")

m = int(input("Masukkan jumlah elemen arr1: "))
arr1 = list(map(int, input("Masukkan elemen arr1 (pisahkan spasi): ").split()))

n = int(input("Masukkan jumlah elemen arr2: "))
arr2 = list(map(int, input("Masukkan elemen arr2 (pisahkan spasi): ").split()))

x = int(input("Masukkan nilai x: "))

a, b, diff = closest_pair(arr1, arr2, x)

print("\n=== HASIL ===")
print("Pasangan terbaik :", a, "dan", b)
print("Jumlah =", a + b)
print("Selisih |jumlah - x| =", diff)
