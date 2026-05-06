m = int(input("Nhập hàng: "))
n = int(input("Nhập cột: "))
A = []

for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

tong = 0
for row in A:
    for x in row:
        tong = tong + x

print("Tổng:", tong)