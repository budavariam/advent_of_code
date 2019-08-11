# 255: '11111111'
# 65536: '10000000000000000'
# 16777215: '111111111111111111111111'

d = 0
a = 8307757
while (d != a):
    c = d | 0x10000
    d = 14070682
    while True:
        d = (((d + (c & 0xFF)) & 0xFFFFFF) * 65899) & 0xFFFFFF
        if 256 > c:
            break
        c //= 256
print("Program halts")

