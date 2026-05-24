def loc_chuoi(s):
    hop_le = "0123456789ABCDEF"
    kq = ""
    s = s.upper()
    for ch in s:
        if ch in hop_le:
            kq += ch
    return kq

def xac_dinh_co_so(s):
    s = s.upper()
    if all(ch in "01" for ch in s):
        return 2

    elif all(ch in "01234567" for ch in s):
        return 8

    elif all(ch in "0123456789" for ch in s):
        return 10

    elif all(ch in "0123456789ABCDEF" for ch in s):
        return 16

    else:
        return "Không xác định"

def he2_sang_10(s):
    return int(s, 2)

def he8_sang_10(s):
    return int(s, 8)

def he16_sang_10(s):
    return int(s, 16)