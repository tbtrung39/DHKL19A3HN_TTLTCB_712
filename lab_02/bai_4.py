n = int(input("Nhập số: "))

if abs(n) < 100:
    print(0)
else:
    print(abs(n) // 100 % 10)