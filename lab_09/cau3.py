def luy_thua(a, n):

    if n == 0:
        return 1

    return a * luy_thua(a, n - 1)


a = int(input("Nhap a: "))
n = int(input("Nhap n: "))

print("Ket qua:", luy_thua(a, n))