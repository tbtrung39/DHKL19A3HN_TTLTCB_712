import random
A = []
for i in range(50):
    A.append(random.randint(0,200))
B = []
for x in A:
    if x % 5 == 0 and x % 7 == 0:
        B.append(x)
print(B)