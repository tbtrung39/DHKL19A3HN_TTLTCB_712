n = int(input("Nhập n: "))

A = set()
B = set()

# tìm ước và kiểm tra nguyên tố
for i in range(2, n):
    if n % i == 0:
        # kiểm tra i có phải số nguyên tố
        la_nt = True
        for j in range(2, i):
            if i % j == 0:
                la_nt = False
                break
        if la_nt:
            A.add(i)
    else:
        B.add(i)

print("Tập A (ước nguyên tố):", A)
print("Tập B:", B)