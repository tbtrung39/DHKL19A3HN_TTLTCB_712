X = int(input("nhập giá trị X:"))
Y = int(input("nhập giá trị Y:"))
A = []

for i in range(X):
    row = []
    for j in range(Y):
        row.append(i*j)
    A.append(row)
print(A)