n = int(input("nhập số lấn:"))
A = []
for i in range(n):
    A.append(int(input("nhập:")))
# chia hết cho 3 nhưng không chia hết cho 5
B = []
for x in A:
    if x % 3 == 0 and x % 5 != 0:
        B.append(x)
print(B)
# bình phương
C = []
for x in A:
    C.append(x*x)
print(C)
# lấy ngẫu nhiên số chia hết cho 3
import random
D = []
for x in A:
    if x % 3 == 0:
        D.append(x)
if len(D) > 0:
    print("Ngẫu nhiên:", random.choice(D))