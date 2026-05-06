A = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    A.append(x)

A.insert(0, [1,2,3])     
A.append([1,2,3])        

if len(A) >= 5:
    A.insert(4, [1,2,3])  # vị trí 5
print(A)
k = int(input("Nhập k: "))
if 0 <= k < len(A):
    del A[k]

B = A.copy()
B.sort()
print("Tăng dần:", B)

B.sort(reverse=True)
print("Giảm dần:", B)