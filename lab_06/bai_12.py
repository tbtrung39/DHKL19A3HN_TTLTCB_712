tong = 0
while True:
    s = input("nhập D và W:S")
    if s == "":
        break

    loai, tien = s.split()
    tien = int(tien)

    if loai == "D":
        tong += tien
    elif loai == "W":
        tong -= tien
print("Số tiền cuối:", tong)