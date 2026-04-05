s = input("Nhập mã container: ")

tong = 0

for i in range(len(s)):
    c = s[i]

    if c >= 'A' and c <= 'Z':
        value = ord(c) - ord('A') + 10
    else:
        value = int(c)

    tong += value * (2**i)

check = tong % 11

print("Số kiểm tra =", check)