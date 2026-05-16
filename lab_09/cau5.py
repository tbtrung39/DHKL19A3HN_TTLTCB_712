def permutation(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permutation(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

n = int(input("Nhập n: "))

a = []
for i in range(1, n + 1):
    a.append(i)

permutation(a, 0, n - 1)