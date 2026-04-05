s1 = input("Chuỗi 1: ")
s2 = input("Chuỗi 2: ")

result = ""

max_len = max(len(s1), len(s2))

for i in range(max_len):
    if i < len(s1):
        result += s1[i]
    if i < len(s2):
        result += s2[i]

print("Chuỗi sau khi trộn:", result)