s = input("Nhap chuoi: ")
count = 0
for ch in s:
    if ch.isdigit():
        count += 1
print("So ky tu la so:", count)