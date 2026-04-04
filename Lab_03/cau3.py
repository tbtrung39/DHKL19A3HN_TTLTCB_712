n = int(input("Nhập n: "))

la_nt = True
if n < 2:
    la_nt = False

for i in range(2, n):
    if n % i == 0:
        la_nt = False

if la_nt:
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")