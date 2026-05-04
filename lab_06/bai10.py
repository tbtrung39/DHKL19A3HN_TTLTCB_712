import random
lst = []
for x in range(201): 
    if x % 5 == 0 and x % 7 == 0:
        lst.append(x)
print("Các số chia hết cho 5 và 7:", lst)
print("Số ngẫu nhiên:", random.choice(lst))