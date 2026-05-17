def luythua(a,n):
    if n == 0:
        return 1
    return a * luythua(a, n-1)
a = int(input('nhập a:'))
n = int(input('nhập n:'))
print(luythua(a,n))