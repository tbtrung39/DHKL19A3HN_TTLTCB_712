cpp = set(map(int, input("SV học C++: ").split()))
java = set(map(int, input("SV học Java: ").split()))
python = set(map(int, input("SV học Python: ").split()))
# học cả 3
all3 = cpp & java & python
# học đúng 2
two = (cpp & java) | (cpp & python) | (java & python)
two = two - all3
# học đúng 1
one = (cpp | java | python) - (two | all3)
print("Chỉ học 1:", one)
print("Học 2:", two)
print("Học 3:", all3)