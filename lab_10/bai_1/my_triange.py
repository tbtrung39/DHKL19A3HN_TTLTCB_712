import math
def is_TamGiac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
def chuviTamGiac(a,b,c):
    return a + b + c
def S_TamGiac(a,b,c):
    p = chuviTamGiac(a,b,c) / 2
    s = math.sqrt(p * (p-a) * (p-b) * (p-c))
    return s

