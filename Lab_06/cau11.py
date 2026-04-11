import random

so_luong = int(input("Nhập n: "))
danh_sach_A = list(map(int, input("Nhập danh sách: ").split()))

# a
danh_sach_B = [so for so in danh_sach_A if so % 3 == 0 and so % 5 != 0]
print("Danh sách B:", danh_sach_B)

# b
danh_sach_C = [so**2 for so in danh_sach_A]
print("Danh sách C:", danh_sach_C)

# c
danh_sach_chia_3 = [so for so in danh_sach_A if so % 3 == 0]
danh_sach_D = random.sample(danh_sach_chia_3, min(3, len(danh_sach_chia_3)))
print("Danh sách D:", danh_sach_D)
