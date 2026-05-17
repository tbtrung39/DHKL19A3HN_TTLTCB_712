#a
def tong_a(n):
    if n == 1:
        return 1 / (1 * 2)

    return tong_a(n - 1) + 1 / (n * (n + 1))

n = int(input("Nhập n: "))
print("S =", tong_a(n))

#b
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

def tong_b(n):
    if n == 1:
        return 1

    return tong_b(n - 1) + 1 / giai_thua(n)

n = int(input("Nhập n: "))

print("S =", tong_b(n))

#c
import math
def tong_can(n):
    if n == 1:
        return math.sqrt(3)

    return math.sqrt(3 * n + tong_can(n - 1))
n = int(input("Nhập n: "))
print("S =", tong_can(n))

#d
import math
def tinh_s(n):

    if n == 1:
        return math.sqrt(1)

    return math.sqrt(n + tinh_s(n - 1))
n = int(input("Nhap n: "))
print("S =", tinh_s(n))