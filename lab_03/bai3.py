n = int(input("Nhập n: "))
la_snt = True
if n < 2:
    la_snt = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_snt = False
            break
if la_snt:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")
    for k in range(1, n):
        if n - k > 1:
            check1 = True
            for i in range(2, int((n - k) ** 0.5) + 1):
                if (n - k) % i == 0:
                    check1 = False
                    break
            if check1:
                print("Gần nhất là:", n - k)
                break