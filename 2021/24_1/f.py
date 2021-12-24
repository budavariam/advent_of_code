
import math

a = [1, 1, 1, 1, 1, 26, 26, 1, 26, 1, 26, 26, 26, 26]
b = [10, 10, 14, 11, 14, -14, 0, 10, -10, 13, -12, -3, -11, -2]
c = [2, 4, 8, 7, 12, 7, 10, 14, 2, 6, 8, 11, 5, 11]

def inner(i, w, z):
    if ((z % 26) + b[i]) == w:
        z = z // a[i]
    else: 
        z = ((z // a[i]) * 26) + (w + c[i])
    return z

def monad(chknum):
    w, x, y, z = [int(0)]*4
    for i in range(14):
        w = int(chknum[i])
        z = inner(i, w, z)

        # print('---', w, x, y, z, '')
    # n = input()
    return chknum, w, x, y, z, ''

maxnum = int("".join(['9']*14))
def nextnum():
    i = maxnum
    while i != maxnum-10:
        i-=1
        yield i
for i in nextnum():
    # powa = math.pow(26, 7)
    if i % 10000 == 0:
        print(i)
    chknum = str(i)
    if '0' in chknum:
        continue
    else:
        chknum, w, x, y, z, err = monad(chknum)
        print(chknum, w, x, y, z, err)
        if z == 0 or z % 26 == 0:
            print(chknum, w, x, y, z, err)
            print(f"Found z=0: {chknum}")
            # break
