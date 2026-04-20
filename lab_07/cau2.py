import random

# tạo list Numbers
Numbers = []
n = int(input("Nhập số phần tử: "))

for i in range(n):
    Numbers.append(random.randint(1, 100))

print("Danh sách Numbers:", Numbers)

# tạo set A từ Numbers
A = set(Numbers)
print("Tập hợp A:", A)