n = int(input("Nhập n: "))
matran = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    matran.append(hang)
print("Ma trận:")
for hang in matran:
    print(hang)