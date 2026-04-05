thang = int(input("Nhap thang (1-12): "))
if thang == 2:
    print("Thang 2 co 28 ngay")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print("Thang", thang, "co 30 ngay")
else:
    print("Thang", thang, "co 31 ngay")