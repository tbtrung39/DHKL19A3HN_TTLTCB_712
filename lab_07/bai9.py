n = int(input("Nhập n: "))
A = set()
B = set()
for i in range(2, n+1):
    la_nt = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            la_nt = False
            break
    
    if la_nt:
        if n % i == 0:
            A.add(i)
        else:
            B.add(i)
print("A (ước nguyên tố):", A)
print("B (không là ước):", B)