A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

tim_duoc = False

# tách A thành C + D
for i in range(1, len(A)):
    C = int(A[:i])
    D = int(A[i:])
    
    # tách B thành E + F
    for j in range(1, len(B)):
        E = int(B[:j])
        F = int(B[j:])
        
        if C + D == E + F:
            print(f"{C}+{D}={E}+{F}")
            tim_duoc = True

if not tim_duoc:
    print("Không tồn tại cách đặt!")