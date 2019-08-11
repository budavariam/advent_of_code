# 255: '11111111'
# 65536: '10000000000000000'
# 16777215: '111111111111111111111111'

d = 0
a = 0
init = True

visited = set()
prev = -1
cnt = 0
while (init or d != a):
    init = False

    cnt+=1
    if cnt % 1000 == 0:
        print(cnt)

    c = d | 0x10000
    d = 14070682
    while True:
        d = (((d + (c & 0xFF)) & 0xFFFFFF) * 65899) & 0xFFFFFF
        if 256>c:
            break
        c//=256
    if not (d in visited):
        visited.add(d)
        #print(cnt, d)
        prev = d
    else:
        print(prev)
        break
print("Program halts")

