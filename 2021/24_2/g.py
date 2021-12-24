
import math

a = [1, 1, 1, 1, 1, 26, 26, 1, 26, 1, 26, 26, 26, 26]
b = [10, 10, 14, 11, 14, -14, 0, 10, -10, 13, -12, -3, -11, -2]
c = [2, 4, 8, 7, 12, 7, 10, 14, 2, 6, 8, 11, 5, 11]

stck = []
conn = {}

def monad():
    for i in range(14):
        if a[i] == 26:
            j, cj = stck.pop()
            conn[i] = (j, cj + b[i])
        else:
            stck.append((i, c[i]))
    return

monad()

print(stck, conn)
result = [0]*14
for i, (j, diff) in conn.items():
    result[i] = max(1, 1 + diff)
    result[j] = max(1, 1 - diff)
    print(conn)
    print(result)
print("".join(map(str,result)))