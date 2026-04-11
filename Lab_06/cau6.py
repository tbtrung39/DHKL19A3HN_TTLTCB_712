import random

danh_sach = [random.randint(1, 99999) for _ in range(1000)]

# Cách 1
sap_xep_1 = sorted(danh_sach)

# Cách 2 (không dùng sorted)
for i in range(len(danh_sach)):
    for j in range(i+1, len(danh_sach)):
        if danh_sach[i] > danh_sach[j]:
            danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]

print("Đã sắp xếp xong")
