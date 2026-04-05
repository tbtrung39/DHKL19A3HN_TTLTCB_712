gio_dau = 100000
gio_thue = float(input("Nhap so gio thue san: "))
khung_gio = int(input("Nhap gio bat dau thue (0-24): "))
if gio_thue <= 3:
    tong_tien = gio_thue * gio_dau
else:
    tong_tien = 3 * gio_dau + (gio_thue - 3) * gio_dau * 0.75
if 11 <= khung_gio <= 15:
    tong_tien = tong_tien * 0.9

print("Tong tien thue san la:", tong_tien, "VND")