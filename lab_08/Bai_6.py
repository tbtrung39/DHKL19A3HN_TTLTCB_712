def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN là:", lcm(a, b))