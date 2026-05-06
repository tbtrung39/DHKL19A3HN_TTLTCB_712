def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print("UCLN cua", a, "va", b, "la:", ucln(a,b))