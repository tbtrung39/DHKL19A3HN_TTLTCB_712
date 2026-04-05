A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

tim_thay = False

for i in range(1, len(A)):
    C_str = A[:i]
    D_str = A[i:]
    
    C = int(C_str)
    D = int(D_str)
    
    for j in range(1, len(B)):
        E_str = B[:j]
        F_str = B[j:]
        
        E = int(E_str)
        F = int(F_str)
        
        if C + D == E + F:
            print(f"{C_str}+{D_str}={E_str}+{F_str}")
            tim_thay = True
            break 
            
    if tim_thay == True:
        break

if tim_thay == False:
    print("Không tồn tại cách đặt!")