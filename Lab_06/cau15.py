danh_sach = []

so_luong = int(input("Nhập số phần tử: "))
for i in range(so_luong):
    ten = input("Tên: ")
    tuoi = int(input("Tuổi: "))
    diem = int(input("Điểm: "))
    danh_sach.append((ten, tuoi, diem))

danh_sach.sort()

print(danh_sach)
