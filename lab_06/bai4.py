lst = list(map(int, input("Nhập danh sách: ").split()))
lst = [1, 2, 3] + lst
lst = lst + [1, 2, 3]
if len(lst) >= 5:
    lst[4:4] = [1, 2, 3]

print("Sau khi chèn:", lst)
k = int(input("Nhập phần tử cần xóa: "))
if k in lst:
    lst.remove(k)
print("Sau khi xóa:", lst)
print("Tăng dần:", sorted(lst))
print("Giảm dần:", sorted(lst, reverse=True))