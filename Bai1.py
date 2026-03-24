n = int(input("Nhập n: "))

tich = 1
tong = 1

for i in range(1, n + 1):
    tich *= (2 * i) / (2 * i + 1)
    tong += tich

print(round(tong, 3))