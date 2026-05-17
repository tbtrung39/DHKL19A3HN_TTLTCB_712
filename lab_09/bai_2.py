def quan(a,b):
    if b == 0:
        return a
    return quan(b, a%b)
n = int(input('nhập n:'))
x = int(input('số thứ nhất:'))
for i in range(2,n+1):
    y = int(input(f'nhập số thứ {i}:'))
    x = quan(x,y)
print('UCLN =', x)