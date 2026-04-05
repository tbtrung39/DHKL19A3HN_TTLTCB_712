kw = float(input("Nhap so KW dien tieu thu: "))
if kw <= 100:
    tien = kw * 2000
elif kw <= 200:
    tien = 100 * 2000 + (kw - 100) * 2500
elif kw <= 300:
    tien = 100 * 2000 + 100 * 2500 + (kw - 200) * 3000
else:
    tien = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 5000
print("Tong tien dien la:", tien, "VND")