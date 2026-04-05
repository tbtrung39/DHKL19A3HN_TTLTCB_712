import math

x = float(input("Nhập x (radian): "))
eps = 0.0001

term = 1
S = 1
n = 1
while abs(term) > eps:
    term = (-1)*term*x*x/((2*n)*(2*n-1))
    S += term
    n += 1
print("cos(x) ≈", S)
print("So với math.cos:", math.cos(x))