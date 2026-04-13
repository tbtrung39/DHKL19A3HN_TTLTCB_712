s = input("Nhập password: ")
ds = s.split(",")

for pw in ds:
    if (len(pw) >= 6 and len(pw) <= 12
        and any(c.islower() for c in pw)
        and any(c.isupper() for c in pw)
        and any(c.isdigit() for c in pw)
        and any(c in "$#@" for c in pw)):
        print(pw)