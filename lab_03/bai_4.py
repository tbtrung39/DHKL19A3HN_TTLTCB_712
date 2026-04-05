n = int(input("Nhập n: "))

for i in range(2, n+1):
    la_snt = True
    for j in range(2, i):
        if i % j == 0:
            la_snt = False
    if la_snt:
        print(i)