s = set()

while True:
    x = input("Nhập phần tử (Enter để dừng): ")
    if x == "":
        break
    s.add(x)

print("Set ban đầu:", s)

xoa = input("Nhập phần tử cần xóa: ")
if xoa in s:
    s.remove(xoa)

print("Set sau khi xóa:", s)