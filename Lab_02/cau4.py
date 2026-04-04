n = int(input("Nhập số nguyên: "))

if abs(n) >= 100:
    hang_tram = abs(n) // 100 % 10
    print("Hàng trăm:", hang_tram)
else:
    print("0")
    