def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

n = int(input("Nhập số lượng số: "))

a = int(input("Nhập số thứ 1: "))

for i in range(2, n + 1):
    x = int(input("Nhập số tiếp theo: "))
    a = ucln(a, x)

print("Ước chung lớn nhất là:", a)