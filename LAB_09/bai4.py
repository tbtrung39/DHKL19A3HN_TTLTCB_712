# Bài 4: In tất cả hoán vị của [1..n]

def hoanvi(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            
            hoanvi(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

n = int(input("Nhap n: "))
a = list(range(1, n + 1))

hoanvi(a, 0, n - 1)