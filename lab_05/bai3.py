n = int(input("Nhập số n: "))
kq = ""
while n > 0:
    du = n % 2
    kq = str(du) + kq
    n = n // 2
print("Số nhị phân:", kq)