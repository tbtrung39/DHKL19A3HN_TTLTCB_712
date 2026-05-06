str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

kq = ""
i = 0

while i < len(str1) or i < len(str2):
    if i < len(str1):
        kq += str1[i]
    if i < len(str2):
        kq += str2[i]
    i += 1

print("Chuỗi sau khi trộn:", kq)