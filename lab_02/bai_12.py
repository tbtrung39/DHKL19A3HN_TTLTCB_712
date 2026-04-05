ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if thang < 1 or thang > 12:
    print("Lỗi: Tháng không hợp lệ")
else:
    if thang == 2:
        max_day = 28
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        max_day = 30
    else:
        max_day = 31

    if ngay < 1 or ngay > max_day:
        print("Lỗi: Ngày không hợp lệ")
    else:
        if ngay < max_day:
            ngay += 1
        else:
            ngay = 1
            thang += 1
            if thang > 12:
                thang = 1

        print("Ngày tiếp theo là:", ngay, "/", thang)