ds = []
n = int(input("nhập số lần:"))

for i in range(n):
    ten = input("nhập tên:")
    tuoi = int(input("nhập tuổi:"))
    diem = float(input("nhập điểm"))
    ds.append((ten, tuoi, diem))

# sắp theo tên -> tuổi -> điểm
ds.sort(key=lambda x: (x[0], x[1], x[2]))
print(ds)