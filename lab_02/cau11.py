bat_dau = int(input("Nhap gio bat dau (>=5): "))
ket_thuc = int(input("Nhap gio ket thuc (<=22): "))
if bat_dau < 5 or ket_thuc > 22 or bat_dau >= ket_thuc:
    print("Gio nhap vao khong hop le!")
else:
    so_gio = ket_thuc - bat_dau
    tien = so_gio * 100000
    print("So gio thue la:", so_gio)
    print("So tien phai tra la:", tien, "VND")