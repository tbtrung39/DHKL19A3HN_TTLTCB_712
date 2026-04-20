import random
import string

A = set()
B = set()

# tạo A
for i in range(5):
    A.add(random.choice(string.ascii_letters + string.digits))

# tạo B
for i in range(5):
    B.add(random.choice(string.ascii_letters + string.digits))

print("A:", A)
print("B:", B)

# phần tử chung
print("Phần tử chung:", A & B)