import math

def chu_vi(r):
    return 2 * math.pi * r

def dien_tich(r):
    return math.pi * r * r

r = float(input("Nhap ban kinh: "))

cv = chu_vi(r)
dt = dien_tich(r)

print("Chu vi:", cv)
print("Dien tich:", dt)