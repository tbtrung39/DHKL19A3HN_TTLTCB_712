n = int(input("Nhập n: "))
A = list(map(int, input("Nhập số: ").split()))

# a
B = []
for x in A:
    if x % 3 == 0 and x % 5 != 0:
        B.append(x)
print(B)

# b
C = []
for x in A:
    C.append(x*x)
print(C)

# c
import random
D = []

for x in A:
    if x % 3 == 0:
        D.append(x)

if len(D) > 0:
    print(random.choice(D))