so_du = 0

while True:
    dong = input("Nhập (D/W số tiền, Enter để dừng): ")
    if dong == "":
        break

    loai, tien = dong.split()
    tien = int(tien)

    if loai == "D":
        so_du += tien
    elif loai == "W":
        so_du -= tien

print("Số dư:", so_du)


