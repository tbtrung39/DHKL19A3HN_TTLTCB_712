diem = float(input("Nhập điểm trung bình: "))

if 0 <= diem < 3:
    print("Kém")
elif diem < 5:
    print("Yếu")
elif diem < 7:
    print("Trung bình")
elif diem < 8:
    print("Khá")
elif diem < 9:
    print("Giỏi")
elif diem <= 10:
    print("Xuất sắc")
else:
    print("Điểm không hợp lệ")