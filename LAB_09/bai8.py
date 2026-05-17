# Bài 8a:
# S = 1/(1*2) + 1/(2*3) + ... + 1/(n(n+1))

def tong_a(n):
    if n == 1:
        return 1 / (1 * 2)

    return tong_a(n - 1) + 1 / (n * (n + 1))

n = int(input("Nhap n: "))
print("S =", tong_a(n))
# Bài 8b:
# S = 1 + 1/1.2 + 1/1.2.3 + ... + 1/n!

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def tong_b(n):
    if n == 1:
        return 1

    return tong_b(n - 1) + 1 / fact(n)

n = int(input("Nhap n: "))
print("S =", tong_b(n))
# Bài 8c

import math

def tong_c(n):
    if n == 1:
        return math.sqrt(3)

    return math.sqrt(3 * n + tong_c(n - 1))

n = int(input("Nhap n: "))
print("S =", tong_c(n))
# Bài 8d

import math

def tong_d(n):
    if n == 1:
        return 1

    return (n + tong_d(n - 1)) ** (1 / n)

n = int(input("Nhap n: "))
print("S =", tong_d(n))