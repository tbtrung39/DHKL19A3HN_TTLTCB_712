data = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    name = input("Name: ")
    age = int(input("Age: "))
    score = int(input("Score: "))
    data.append((name, age, score))
data.sort()
print(data)