s = input("Nhập chuỗi: ")
max_str = ""
cur = s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cur += s[i]
    else:
        if len(cur) > len(max_str):
            max_str = cur
        cur = s[i]

if len(cur) > len(max_str):
    max_str = cur
print("Chuỗi con dài nhất:", max_str)