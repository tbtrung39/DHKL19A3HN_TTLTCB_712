n = int(input("Nhập n: "))
if n == 0:
    nhi_phan = "0"
else:
    nhi_phan = ""
    while n > 0:
        nhi_phan = str(n % 2) + nhi_phan
        n //= 2
print("số nhị phân:", nhi_phan)