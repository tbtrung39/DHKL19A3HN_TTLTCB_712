def dao_nguoc(n):

    if n < 10:
        print(n, end="")
        return

    print(n % 10, end="")

    dao_nguoc(n // 10)


n = int(input("Nhap so: "))

dao_nguoc(n)