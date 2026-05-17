def hoan_vi(a, k):
    if k == len(a):
        print(a)
        return
    for i in range(k, len(a)):
        a[k], a[i] = a[i], a[k]
        hoan_vi(a, k + 1)
        a[k], a[i] = a[i], a[k]

n = int(input("Nhập n: "))
a = list(range(1, n + 1))
print("Các hoán vị là:")
hoan_vi(a, 0)