def ucln(a,b):
    while b != 0:
        a,b = b, a%b
        return a

def bcnn(a,b):
    return a * b // ucln(a,b)

def SumDivisor(n):
    tong = 0

    for i in range(1, n+1):
        if n % i == 0:
            tong += i
    return tong