n = int(input("Nhap n: "))
nt = True
if n < 2:
    nt = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            nt = False
            break
if nt:
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")
    
    for k in range(n - 1, 1, -1):
        nt = True
        
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                nt = False
                break
        if nt:
            print("So nguyen to gan nhat:", k)
            break