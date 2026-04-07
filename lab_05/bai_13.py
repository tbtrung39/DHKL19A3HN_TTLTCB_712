A = input("A: ")
B = input("B: ")
found = False
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i])
        D = int(A[i:])
        E = int(B[:j])
        F = int(B[j:])

        if C + D == E + F:
            print(f"{C}+{D}={E}+{F}")
            found = True

if not found:
    print("Không tồn tại cách đặt!")