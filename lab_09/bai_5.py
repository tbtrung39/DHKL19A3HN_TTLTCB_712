def permutation(n):
    if n == 1:
        return [[1]]
    kq = []
    g = permutation(n - 1)

    for p in g:
        for i in range(len(p) + 1):
            temp = p.copy()
            temp.insert(i, n)
            kq.append(temp)

    return kq
n = int(input("n = "))
print(permutation(n))