def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
ket_qua = ucln(a, b)
print("UCLN cua", a, "va", b, "la:", ket_qua)