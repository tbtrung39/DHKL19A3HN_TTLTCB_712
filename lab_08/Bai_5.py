def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN là:", gcd(a, b))