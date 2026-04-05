s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
kq = ""
dai1 = len(s1)
dai2 = len(s2)
max_len = dai1 if dai1 > dai2 else dai2
for i in range(max_len):
    if i < dai1:
        kq += s1[i]
    if i < dai2:
        kq += s2[i]
print("Chuỗi sau khi trộn:", kq)