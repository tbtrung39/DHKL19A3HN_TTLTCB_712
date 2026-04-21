n = int(input("Nhập n: "))
list1 = []
list2 = []
print("Nhập số:")
for i in range(n):
    list1.append(int(input()))

print("Nhập tên:")
for i in range(n):
    list2.append(input())

d = {}
for i in range(n):
    d[list1[i]] = list2[i]
print("Dictionary:", d)