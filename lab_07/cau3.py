A = set()
n = int(input("Nhập số phần tử: "))

for i in range(n):
    x = float(input("Nhập số thực: "))
    A.add(x)

print("Tập A:", A)
print("Min:", min(A))
print("Max:", max(A))
print("Tổng:", sum(A))