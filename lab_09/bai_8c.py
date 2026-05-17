import math
def s(n):
    if n == 1:
        return math.sqrt(3)

    return math.sqrt(3 * n + s(n - 1))
n = int(input('nhập n='))
print(s(n))