import math
x = float(input("Nhập x: "))
sai_so = 1e-4
cos_x = 1
hang_tu = 1
i = 1
while abs(hang_tu) > sai_so:
    hang_tu *= -x*x / ((2*i - 1)*(2*i))
    cos_x += hang_tu
    i += 1
print("cos(x) ≈", cos_x)
print("So với math.cos:", math.cos(x))