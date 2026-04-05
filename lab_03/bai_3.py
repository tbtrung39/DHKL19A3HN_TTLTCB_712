n = int(input("Nhập n: "))

la_snt = True

if n < 2:
    la_snt = False
else:
    for i in range(2, n):
        if n % i == 0:
            la_snt = False

if la_snt:
    print("Là số nguyên tố")
else:
    print("Không phải SNT")
    
    for i in range(n-1, 1, -1):
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
        if check:
            print("SNT gần nhất là:", i)
            break