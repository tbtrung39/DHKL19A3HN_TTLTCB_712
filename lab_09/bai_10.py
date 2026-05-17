memo = {0: 1}
def X(n):
    if n in memo:
        return memo[n]

    s = 0

    for i in range(n):
        s += (n - i) ** 2 * X(i)

    memo[n] = s
    return s

n = int(input('nhập n='))
print(X(n))