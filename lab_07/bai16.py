n = int(input("Nhap n: "))
a = list(map(int, input("Nhap day: ").split()))
cap_chi_so = []
for i in range(n):
    for j in range(i+1, n):
        if a[i] + 1 == a[j]:
            cap_chi_so.append((i, j))
print("Cac cap (i, j):", cap_chi_so)
print("So luong cap:", len(cap_chi_so))