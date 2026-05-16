def giai_thua_kep(n):

    if n == 0 or n == 1:
        return 1

    return n * giai_thua_kep(n - 2)


n = int(input("Nhap n: "))

print("n!! =", giai_thua_kep(n))

def giai_thua_kep(n):

    if n == 0 or n == 1:
        return 1

    return n * giai_thua_kep(n - 2)


def tinh_tong(k):

    if k == 1:
        return 1

    if k % 2 == 0:
        return tinh_tong(k - 1) - giai_thua_kep(k)

    return tinh_tong(k - 1) + giai_thua_kep(k)


k = int(input("Nhap k: "))

print("S =", tinh_tong(k))