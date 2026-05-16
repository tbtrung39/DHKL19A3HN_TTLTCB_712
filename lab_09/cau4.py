def in_day(n):

    if n == 0:
        return

    in_day(n - 1)

    print(n)


n = int(input("Nhap n: "))

in_day(n)