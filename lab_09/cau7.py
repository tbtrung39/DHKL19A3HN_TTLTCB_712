def tim_nghiem(n, N, a):
    if n == 1:
        a.append(N)
        print(a)
        a.pop()
    else:
        for i in range(N + 1):
            a.append(i)
            tim_nghiem(n - 1, N - i, a)
            a.pop()

n = int(input("Nhập n: "))
N = int(input("Nhập N: "))

tim_nghiem(n, N, [])