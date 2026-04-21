# a
n = int(input("Nhập n: "))
arr = []

for i in range(n):
    x = int(input("Nhập số: "))
    arr.append(x)
print("Dãy:", arr)


# b
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

count = 0
num = 2
print("Các số nguyên tố đầu tiên:")
while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1