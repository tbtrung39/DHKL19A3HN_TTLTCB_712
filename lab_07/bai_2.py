numbers = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    x = int(input("Nhập số: "))
    numbers.append(x)
A = set(numbers)
print("Danh sách:", numbers)
print("Tập hợp A:", A)