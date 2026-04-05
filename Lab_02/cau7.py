diem = float(input("Nhập điểm trung bình: "))

if diem < 0 or diem > 10:
    print("Điểm không hợp lệ")
elif diem < 3:
    print("Loại Kém")
elif diem < 5:
    print("Loại Yếu")
elif diem < 7:
    print("Loại Trung bình")
elif diem < 8:
    print("Loại Khá")
elif diem < 9:
    print("Loại Giỏi")
else:
    print("Loại Xuất sắc")