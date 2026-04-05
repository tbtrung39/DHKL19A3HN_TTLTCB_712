str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")

i = 0
j = 0
res = ""

while i < len(str1) and j < len(str2):
    res += str1[i]
    res += str2[j]
    i += 1
    j += 1

if i < len(str1):
    res += str1[i:]

if j < len(str2):
    res += str2[j:]

print("Chuoi tron:", res)