A = input("Nhập các phần tử: ").split()
so_nguyen = 0
so_thuc = 0
chuoi = 0
for x in A:
    if x.isdigit():
        so_nguyen += 1
    else:
        try:
            float(x)
            so_thuc += 1
        except:
            chuoi += 1

print("Số nguyên:", so_nguyen)
print("Số thực:", so_thuc)
print("Chuỗi:", chuoi)