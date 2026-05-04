n = int(input("Nhập n: "))
dem = 0
so = 2
while dem < n:
    la_nt = True
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            la_nt = False
            break
    if la_nt:
        print(so, end=" ")
        dem += 1
    so += 1