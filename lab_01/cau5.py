t = float(input("Nhập thời gian sử dụng (giây): "))
u = 220
i = 2.7
gia = 7000
kwh = (u * i / 1000) * (t / 3600)
tien = kwh * gia
print("Số tiền điện phải trả là:", round(tien, 2), "đồng")