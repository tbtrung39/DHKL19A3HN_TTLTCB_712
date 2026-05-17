# Bài 5: Hàm permutation(n)

def permutation(n):
    if n == 1:
        return [[1]]

    old = permutation(n - 1)
    result = []

    for p in old:
        for i in range(len(p) + 1):
            temp = p[:]
            temp.insert(i, n)
            result.append(temp)

    return result

n = int(input("Nhap n: "))
print(permutation(n))