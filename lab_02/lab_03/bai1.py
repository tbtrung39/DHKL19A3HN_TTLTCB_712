n = int(input("Nhap n: "))
tong = 1
tich = 1
for i in range(1, n + 1):
    tich = tich * (2*i) / (2*i + 1)
    tong += tich
print("Ket qua:", round(tong, 3))