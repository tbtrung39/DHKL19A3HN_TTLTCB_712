def tim_nghiem(N, n, ds=[]):
    if n == 1:
        print(ds + [N])
        return

    for i in range(N + 1):
        tim_nghiem(N - i, n - 1, ds + [i])

N = int(input("Nhập N: "))
n = int(input("Nhập số biến n: "))
print("Các bộ nghiệm:")
tim_nghiem(N, n)