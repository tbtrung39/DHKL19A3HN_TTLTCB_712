kw = int(input("Nhập số KW: "))

if kw <= 100:
    tien = kw * 2000
elif kw <= 200:
    tien = kw * 2500
elif kw <= 300:
    tien = kw * 3000
else:
    tien = kw * 5000

print("Tiền điện:", tien)