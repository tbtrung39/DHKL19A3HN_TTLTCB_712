import random
digits = list(range(10))  
A = set()
while len(A) < 5:
    A.add(random.choice(digits))
print("Tập A:", A)