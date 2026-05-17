def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * double_factorial(n - 2)

k = int(input("k = "))
S = 0
for i in range(1, k + 1):
    S += ((-1) ** (i + 1)) * double_factorial(i)

print(S)