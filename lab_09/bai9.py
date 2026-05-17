def dao_nguoc(n, ket_qua=0):

    if n == 0:
        return ket_qua

    chu_so_cuoi = n % 10

    ket_qua = ket_qua * 10 + chu_so_cuoi

    return dao_nguoc(n // 10, ket_qua)

n = int(input("Nhập số: "))
print("Số đảo ngược là:", dao_nguoc(n))