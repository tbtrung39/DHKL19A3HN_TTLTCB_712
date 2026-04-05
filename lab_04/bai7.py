a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
max_ab = max(a, b)
bcnn = max_ab
while True:
    if bcnn % a == 0 and bcnn % b == 0:
        break
    bcnn += 1
print("BCNN của", a, "và", b, "là:", bcnn)