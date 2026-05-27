import pt

print("1. Phuong trinh bac 1")
print("2. Phuong trinh bac 2")

chon = int(input("Nhap lua chon: "))

if chon == 1:
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))

    pt.pt_bac_1(a, b)

elif chon == 2:
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    c = float(input("Nhap c: "))

    pt.pt_bac_2(a, b, c)