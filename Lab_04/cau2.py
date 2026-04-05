# a) S = 1 + 1/2 + ... + 1/n
n = int(input("Nhập n: "))
i = 1
S = 0
while i <= n:
    S += 1/i
    i += 1
print("S =", S)

# b) S = 1/(1*2) + 1/(2*3) + ...
i = 1
S = 0
while i <= n:
    S += 1/(i*(i+1))
    i += 1
print("S =", S)

# c) S = 1/sqrt(2) + 1/sqrt(3) + ...
import math
i = 2
S = 0
while i <= n:
    S += 1/math.sqrt(i)
    i += 1
print("S =", S)