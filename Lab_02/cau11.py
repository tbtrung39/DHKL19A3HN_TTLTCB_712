gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))

if gio_bat_dau < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    print("Thời gian không hợp lệ")
else:
    so_gio = gio_ket_thuc - gio_bat_dau
    
    # Giá 3 giờ đầu
    if so_gio <= 3:
        tien = so_gio * 100000
    else:
        tien = 3 * 100000 + (so_gio - 3) * 75000   # giảm 25%
    
    # Giảm thêm 10% nếu trong khung 11-15h
    if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
        tien = tien * 0.9
    
    print("Tiền phải trả:", int(tien), "đồng")