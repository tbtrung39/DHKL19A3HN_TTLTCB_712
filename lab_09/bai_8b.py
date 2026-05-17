def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def S(n):
    if n == 1:
        return 1

    return S(n - 1) + 1 / factorial(n)

n = int(input('nhập n='))
print(S(n))