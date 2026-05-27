def loc_ky_tu(s):

    kq = ""

    for i in s:
        if i in "0123456789ABCDEF":
            kq += i

    return kq


def he_so(s):

    if "A" in s or "B" in s or "C" in s or "D" in s or "E" in s or "F" in s:
        return 16

    for i in s:
        if i == "8" or i == "9":
            return 10

    for i in s:
        if i in "234567":
            return 8

    return 2


def he2_sang10(s):
    return int(s, 2)


def he8_sang10(s):
    return int(s, 8)


def he16_sang10(s):
    return int(s, 16)