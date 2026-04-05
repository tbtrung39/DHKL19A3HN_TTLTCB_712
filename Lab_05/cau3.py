n = int(input("Nhập số: "))
binary = ""

if n == 0:
    binary = "0"
else:
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

print("Nhị phân:", binary)