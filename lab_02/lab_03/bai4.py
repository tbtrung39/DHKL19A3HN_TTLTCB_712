n = int(input("Nhap n: "))
for i in range(2, n + 1):
    nt = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            nt = False
            break
    if nt:
        print(i, end=" ")