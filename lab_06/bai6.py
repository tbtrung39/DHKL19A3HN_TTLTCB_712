import random
A = []
for i in range(1000):
    A.append(random.randint(1,99999))

# Cách 1
B = sorted(A)
print(B)

# Cách 2
A.sort()
print(A)