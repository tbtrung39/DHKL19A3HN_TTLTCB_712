str = input("Nhập chuỗi: ")

max_str = ""
current = str[0]

for i in range(1, len(str)):
    if str[i] == str[i-1]:
        current += str[i]
    else:
        if len(current) > len(max_str):
            max_str = current
        current = str[i]

if len(current) > len(max_str):
    max_str = current

print("Chuỗi con dài nhất:", max_str)