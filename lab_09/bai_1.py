def max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

a = int(input('nhập a:'))
b = int(input('nhập b:'))
c = int(input('nhập c:'))
print('max =', max(a,b,c))