import random
A = [random.randint(1, 999999) for _ in range(1000)]
#dùng sorted()
sorted_A1 = sorted(A)
#ko dùng sorted()
for i in range(len(A)):
    for j in range(len(A)-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
print("Danh sách đã sắp xếp (c1):", sorted_A1[:10])
print("Danh sách đã sắp xếp:", A[:10])