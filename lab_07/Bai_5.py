import random
ds = list(range(10))  
A = set()
while len(A) < 5:
    A.add(random.choice(ds))
print("Tập A:", A)