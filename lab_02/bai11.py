so_kw = float(input("Nhập số KW điện tiêu thụ: "))
if so_kw < 0:
    print("Số KW không hợp lệ!")
elif so_kw <= 100:
    tien_dien = so_kw * 2000
elif so_kw <= 200:
    tien_dien = so_kw * 2500
elif so_kw <= 300:
    tien_dien = so_kw * 3000
else:
    tien_dien = so_kw * 5000
if so_kw >= 0:
    print("Số tiền điện phải trả là:",tien_dien)