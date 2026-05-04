n = int(input("Nhập n: "))
A = set()
print("Nhập các số:")
while len(A) < n:
    x = int(input())
    A.add(x)

print("Tập A:", A)
print("Phần tử nhỏ nhất:", min(A))
print("Tổng:", sum(A))