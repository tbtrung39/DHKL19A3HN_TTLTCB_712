ch = input("Nhập ký tự: ")

while len(ch) != 1:
    ch = input("Nhập lại 1 ký tự: ")

print("ASCII =", ord(ch))