def hoan_vi(q, l, r):
    if l == r:
        print(q)
        return

    for i in range(l, r + 1):
        q[l], q[i] = q[i], q[l]
        hoan_vi(q, l + 1, r)
        q[l], q[i] = q[i], q[l]

n = int(input("n = "))
q = list(range(1, n + 1))
hoan_vi(q, 0, n - 1)