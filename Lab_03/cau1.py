n = int(input("Nhập n: "))

s = 1
tich = 1
for i in range(1, n+1):
    tich = tich * (2*i) / (2*i + 1)
    s = s + tich

print("Kết quả:", round(s, 3))