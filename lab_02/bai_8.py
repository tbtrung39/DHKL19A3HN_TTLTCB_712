tnct = int(input("Nhập số tháng công tác: "))
luong_cb = 1350000

if tnct < 12:
    heso = 2.34
elif tnct < 36:
    heso = 3.33
elif tnct < 60:
    heso = 3.66
else:
    heso = 3.99

luong = heso * luong_cb
print("Lương:", luong)