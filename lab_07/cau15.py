list1 = list(map(int, input("Nhập số: ").split()))
list2 = input("Nhập tên: ").split()

d = {}

for i in range(len(list1)):
    d[list1[i]] = list2[i]

print(d)