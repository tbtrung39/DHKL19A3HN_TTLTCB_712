#a
def tong(n):
    if n == 1:
        return 1 / (1 * 2)
    return tong(n - 1) + 1 / (n * (n + 1))

n = int(input("Nhập n: "))

print("S =", tong(n))


#b
def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)

def tong(n):
    if n == 1:
        return 1
    return tong(n - 1) + 1 / giaithua(n)

n = int(input("Nhập n: "))

print("S =", tong(n))


#c
import math

def tinh(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tinh(n - 1))

n = int(input("Nhập n: "))

print("S =", tinh(n))


#d
import math

def tinh_s(n):

    if n == 1:
        return math.sqrt(1)

    return math.sqrt(n + tinh_s(n - 1))


n = int(input("Nhap n: "))

print("S =", tinh_s(n))