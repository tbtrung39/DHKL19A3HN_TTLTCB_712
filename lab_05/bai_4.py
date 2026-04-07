s1 = input("Chuỗi 1: ")
s2 = input("Chuỗi 2: ")
tron = ""
i = 0

while i < len(s1) or i < len(s2):
    if i < len(s1):
        tron += s1[i]
    if i < len(s2):
        tron += s2[i]
    i += 1
print("Chuỗi trộn:", tron)