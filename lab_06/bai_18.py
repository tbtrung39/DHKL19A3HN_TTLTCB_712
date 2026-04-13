m = int(input("nhập m:"))
n = int(input("nhập n:"))
A = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input("nhập:")))
    A.append(row)
# tính tổng
tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]
print("Tổng =", tong)