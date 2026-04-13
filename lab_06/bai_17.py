n = int(input("nhập ma trận="))
A = []

for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    A.append(row)

for r in A:
    print(r)