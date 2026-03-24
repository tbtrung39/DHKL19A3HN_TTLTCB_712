n = int(input("Nhập n: "))

for x in range(1, n):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    if tong == x:
        print(x)