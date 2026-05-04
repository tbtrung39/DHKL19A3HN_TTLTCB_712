import random
A = list(map(int, input("Nhập A: ").split()))
#a
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("B:", B)
#b
C = [x**2 for x in A]
print("C:", C)
#c
D = [x for x in A if x % 3 == 0]
if D:
    print("Phần tử ngẫu nhiên chia hết cho 3:", random.choice(D))
else:
    print("Không có phần tử nào chia hết cho 3")