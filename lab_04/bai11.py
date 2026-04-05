print("Menu:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")

chon = int(input("Chọn (1-5): "))

while chon < 1 or chon > 5:
    chon = int(input("Chọn lại (1-5): "))

if chon == 1:
    print("Bạn chọn Cafe")
elif chon == 2:
    print("Bạn chọn Cam vắt")
elif chon == 3:
    print("Bạn chọn Nước ép cà rốt")
elif chon == 4:
    print("Bạn chọn Nước lọc")
else:
    print("Bạn chọn Nước dừa")