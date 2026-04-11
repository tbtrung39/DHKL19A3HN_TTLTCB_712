danh_sach = []

while True:
    so = int(input("Nhập số (0 để dừng): "))
    if so == 0:
        break
    danh_sach.append(so)


danh_sach = [1,2,3] + danh_sach + [1,2,3]
danh_sach.insert(4, 1)
danh_sach.insert(5, 2)
danh_sach.insert(6, 3)

print("Sau khi chèn:", danh_sach)


vi_tri_k = int(input("Nhập vị trí k: "))
if 0 <= vi_tri_k < len(danh_sach):
    danh_sach.pop(vi_tri_k)


print("Tăng dần:", sorted(danh_sach))
print("Giảm dần:", sorted(danh_sach, reverse=True))
