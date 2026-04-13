import random
A = []
for i in range(1000):
    A.append(random.randint(1,99999))

# dùng sorted
B = sorted(A)
print("Sorted:", B[:10]) 
# không dùng sorted
for i in range(len(A)):
    for j in range(len(A)-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
print("Tự sắp:", A[:10])