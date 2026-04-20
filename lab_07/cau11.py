C = set(map(int, input("C++: ").split()))
J = set(map(int, input("Java: ").split()))
P = set(map(int, input("Python: ").split()))

# 3 ngôn ngữ
ca3 = C & J & P

# đúng 2 ngôn ngữ
ca2 = (C & J) | (C & P) | (J & P)
ca2 = ca2 - ca3

# chỉ 1 ngôn ngữ
ca1 = (C | J | P) - ca2 - ca3

print("Chỉ 1:", ca1)
print("2 ngôn ngữ:", ca2)
print("3 ngôn ngữ:", ca3)