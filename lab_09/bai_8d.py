def s(n):
    if n == 1:
        return 1
    return (n + s(n - 1)) ** (1 / (n + 1))
n = int(input('nhập n='))
print(s(n))