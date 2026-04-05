# ý a
n = int(input("Nhập n: "))
i = 1
S = 0
while i <= n:
    if i % 2 == 0:
        S -= 1/i
    else:
        S += 1/i
    i += 1
print("S =", S)


# ý b
n = int(input("Nhập n: "))
i = 2
S = 0
while i <= n:
    S += 1/(i*(i+1))
    i += 1
print("S =", S)


# ý c
import math
n = int(input("Nhập n: "))
i = 2
S = 0
while i <= n:
    S += 1/math.sqrt(i)
    i += 1
print("S =", S)