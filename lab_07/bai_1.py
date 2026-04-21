s = set()
while True:
    x = input("Nhập ký tự (ESC để dừng): ")
    if x == "ESC":
        break
    s.add(x)

for i in list(s):
    if i.isdigit():
        s.remove(i)
print("Tập hợp sau khi xóa số:", s)