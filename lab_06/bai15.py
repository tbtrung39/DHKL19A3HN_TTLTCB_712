ds = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    ten = input("Tên: ")
    tuoi = int(input("Tuổi: "))
    diem = int(input("Điểm: "))
    ds.append((ten, tuoi, diem))
ds.sort()
print("Sau khi sắp xếp:",ds)
