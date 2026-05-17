def permutation(lst):
    if len(lst) == 1:
        return [lst]

    kq = []

    for i in range(len(lst)):
        x = lst[i]
        con_lai = lst[:i] + lst[i+1:]

        for p in permutation(con_lai):
            kq.append([x] + p)

    return kq

n = int(input("Nhập n: "))
ds = list(range(1, n + 1))
kq = permutation(ds)
for i in kq:
    print(i)