import my_Triangle

a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if my_Triangle.is_TamGiac(a, b, c):
    print("Day la tam giac")

    cv = my_Triangle.ChuViTamGiac(a, b, c)
    print("Chu vi =", cv)

    dt = my_Triangle.S_TamGiac(a, b, c)
    print("Dien tich =", dt)

else:
    print("Khong phai tam giac")