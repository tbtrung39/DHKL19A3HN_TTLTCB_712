bd = int(input())  # giờ bắt đầu
kt = int(input())  # giờ kết thúc

gio = kt - bd

if gio <= 3:
    tien = gio * 100000
else:
    tien = 3*100000 + (gio-3)*75000

# giảm thêm 10% nếu trong 11-15h
if bd >= 11 and kt <= 15:
    tien = tien * 0.9

print(tien)