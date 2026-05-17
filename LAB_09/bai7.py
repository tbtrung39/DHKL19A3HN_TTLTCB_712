# Bài 7: Tìm các bộ nghiệm x1+x2+...+xn = N

def tim_nghiem(N, n, ds=[]):
    if n == 1:
        print(ds + [N])
        return

    for i in range(N + 1):
        tim_nghiem(N - i, n - 1, ds + [i])

N = int(input("Nhap N: "))
n = int(input("Nhap n: "))

tim_nghiem(N, n)