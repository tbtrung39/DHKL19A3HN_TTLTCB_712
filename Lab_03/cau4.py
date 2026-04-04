n = int(input("Nhập n: "))

for i in range(2, n+1):
    la_nt = True
    for j in range(2, i):
        if i % j == 0:
            la_nt = False
    if la_nt:
        print(i)