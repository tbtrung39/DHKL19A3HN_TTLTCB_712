text = input("Nhập đoạn văn: ")
word = input("Nhập từ cần tìm: ")

words = text.split()
count = words.count(word)
print("Số lần xuất hiện:", count)