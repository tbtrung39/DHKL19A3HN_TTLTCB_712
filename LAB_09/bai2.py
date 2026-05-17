# Bài 2: Tính UCLN của n số bằng đệ quy

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input("Nhap n: "))
a = []

for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

ucln = a[0]

for i in range(1, n):
    ucln = gcd(ucln, a[i])

print("UCLN =", ucln)