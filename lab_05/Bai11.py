binary = input("Nhập chuỗi nhị phân: ")

decimal = 0
for ch in binary:
    decimal = decimal * 2 + int(ch)

print("Số thập phân:", decimal)