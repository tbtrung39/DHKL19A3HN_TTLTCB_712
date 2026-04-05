s = input("Nhập chuỗi: ").upper()
hop_le = True
for c in s:
    if not (('0' <= c <= '9') or ('A' <= c <= 'F')):
        hop_le = False
if hop_le:
    print("Chuỗi là hệ Hex")
else:
    print("Chuỗi không hoàn toàn là Hex")

hex_str = ""
for c in s:
    if ('0' <= c <= '9') or ('A' <= c <= 'F'):
        hex_str += c

kq = 0
for c in hex_str:
    if '0' <= c <= '9':
        gia_tri = ord(c) - ord('0')
    else:
        gia_tri = ord(c) - ord('A') + 10

    kq = kq * 16 + gia_tri

print("Giá trị thập phân:", kq)