from hinhhoc import my_Triangle
from hinhhoc import my_square

# Tam giac
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if my_Triangle.is_TamGiac(a, b, c):

    print("Day la tam giac")

    print("Chu vi tam giac =",
          my_Triangle.ChuViTamGiac(a, b, c))

    print("Dien tich tam giac =",
          my_Triangle.S_TamGiac(a, b, c))

else:
    print("Khong phai tam giac")


# Hinh vuong
x = float(input("Nhap canh hinh vuong: "))

print("Chu vi hinh vuong =",
      my_square.ChuViHinhVuong(x))

print("Dien tich hinh vuong =",
      my_square.DienTichHinhVuong(x))