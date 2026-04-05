s = input("Nhap chuoi: ")
count = 0
for ch in s:
    if not ch.isalpha() and not ch.isdigit():
        count += 1
print("So ky tu khong phai chu cai va so:", count)