start = int(input("Giờ bắt đầu: "))
end = int(input("Giờ kết thúc: "))

gio = end - start
tien = 0

if gio <= 3:
    tien = gio * 100000
else:
    tien = 3 * 100000 + (gio - 3) * 75000

if start >= 11 and end <= 15:
    tien = tien * 0.9

print("Tiền:", tien)