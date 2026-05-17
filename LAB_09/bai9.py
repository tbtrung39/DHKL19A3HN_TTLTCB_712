# Bài 9: Đảo ngược số bằng đệ quy

def dao(n):
    if n < 10:
        print(n, end="")
    else:
        print(n % 10, end="")
        dao(n // 10)

n = int(input("Nhap n: "))
dao(n)