n = int(input("Nhập n: "))
S = 1
t = 1
for i in range(1, n + 1):
    t = t * (2 * i) / (2 * i + 1)
    S = S + t
print("Kết quả:", "{:.3f}".format(S))