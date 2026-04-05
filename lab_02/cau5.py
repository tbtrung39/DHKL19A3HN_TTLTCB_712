thang = int(input("Nhap vao mot thang (1-12): "))
if thang < 1 or thang > 12:
    print("Thang khong hop le! Vui long chay lai chuong trinh.")
else:
    if thang == 1: ten = "January"
    elif thang == 2: ten = "February"
    elif thang == 3: ten = "March"
    elif thang == 4: ten = "April"
    elif thang == 5: ten = "May"
    elif thang == 6: ten = "June"
    elif thang == 7: ten = "July"
    elif thang == 8: ten = "August"
    elif thang == 9: ten = "September"
    elif thang == 10: ten = "October"
    elif thang == 11: ten = "November"
    elif thang == 12: ten = "December"
    print("Ten thang la:", ten)
    if thang == 2:
        print("Thang nay co 28 ngay.")
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        print("Thang nay co 30 ngay.")
    else:
        print("Thang nay co 31 ngay.")