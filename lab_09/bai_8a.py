def s(n):
    if n ==1:
        return 1/(1*2)
    return s(n-1) + 1/(n*(n+1))
n = int(input('nhập n:'))
print(s(n))