import random
n = int(input("Nhập n: "))
A = set()
while len(A) < n:
    x = random.uniform(0, 100) 
    A.add(x)

print("Tập A:", A)
print("Min:", min(A))
print("Max:", max(A))
print("Tổng:", sum(A))