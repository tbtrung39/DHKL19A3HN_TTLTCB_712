bd = int(input("Nhập giờ bắt đầu: "))
kt = int(input("Nhập giờ kết thúc: "))

gio = kt - bd
tien = 0

# 3 giờ đầu
if gio <= 3:
    tien = gio * 100000
else:
    tien = 3 * 100000 + (gio - 3) * 75000

# giảm giá 10% nếu trong khoảng 11 -> 15
if 11 <= bd < 15:
    tien = tien * 0.9

print("Tiền phải trả:", int(tien), "đồng")