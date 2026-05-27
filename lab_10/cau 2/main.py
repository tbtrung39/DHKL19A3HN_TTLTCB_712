import my_square

a = float(input("Nhap canh hinh vuong: "))

cv = my_square.ChuViHinhVuong(a)
dt = my_square.Dien_tich_hinh_vuong(a)

print("Chu vi hinh vuong =", cv)
print("Dien tich hinh vuong =", dt)