def tinh_x(n):

    if n == 0:
        return 1

    tong = 0

    for i in range(n):

        tong = tong + (n - i) ** 2 * tinh_x(i)

    return tong


n = int(input("Nhap n: "))

print("Xn =", tinh_x(n))