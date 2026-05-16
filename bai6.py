# Bài 6: Tạo hoán vị ngẫu nhiên

import random

n = int(input("Nhap n: "))

A = list(range(1, n + 1))
result = []

while len(A) > 0:
    x = random.choice(A)
    result.append(x)
    A.remove(x)

print(result)