kw = int(input("Nhập số KW điện: "))

if kw >= 0 and kw <= 100:
    tien = kw * 2000
elif kw <= 200:
    tien = kw * 2500
elif kw <= 300:
    tien = kw * 3000
elif kw > 300:
    tien = kw * 5000
else:
    print("Số KW không hợp lệ")
    tien = 0

print("Tiền điện phải trả:", tien, "đồng")