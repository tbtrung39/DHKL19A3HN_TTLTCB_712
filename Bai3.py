def nt(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input("Nhập n: "))

if nt(n):
    print("Số nguyên tố")
else:
    duoi = n - 1
    tren = n + 1
    while True:
        if duoi >= 2 and nt(duoi):
            print(duoi)
            break
        if nt(tren):
            print(tren)
            break
        duoi -= 1
        tren += 1