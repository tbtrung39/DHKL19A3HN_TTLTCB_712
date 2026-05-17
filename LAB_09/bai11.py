# Bài 11: Giai thừa kép và tính tổng

def gt_kep(n):
    if n == 0 or n == 1:
        return 1

    return n * gt_kep(n - 2)

def tong(k):
    if k == 1:
        return gt_kep(1)

    return tong(k - 1) + ((-1) ** (k + 1)) * gt_kep(k)

k = int(input("Nhap k: "))

print("S =", tong(k))