a = list(map(int, input("Nhập dãy: ").split()))
n = len(a)

dem = 0

for i in range(n):
    for j in range(i+1, n):
        if a[i] + 1 == a[j]:
            dem += 1

print("Số cặp:", dem)