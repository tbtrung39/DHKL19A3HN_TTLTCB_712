n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n: "))
#a
i = 1
S4 = 0
while i <= n:
    S4 += i**2
    i += 1
print("S4 =", S4)
#b
i = 0
S5 = 0
while i <= n:
    S5 += (2*i + 1)**3
    i += 1
print("S5 =", S5)
#c
i = 1
S6 = 0
while i <= n:
    S6 += (2*i)**4
    i += 1
print("S6 =", S6)