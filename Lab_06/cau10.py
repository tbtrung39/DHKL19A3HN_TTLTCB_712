import random

danh_sach = [so for so in range(201) if so % 5 == 0 and so % 7 == 0]

so_ngau_nhien = random.choice(danh_sach)
print("Số ngẫu nhiên:", so_ngau_nhien)
