
import math


def monad(chknum):
    w, x, y, z = [int(0)]*4
    for i in range(14):
        w = int(chknum[i])
        x = int(z % 26)
        z = math.trunc(z/[1, 1, 1, 1, 1, 26, 26, 1, 26, 1, 26, 26, 26, 26][i])
        x += [10, 10, 14, 11, 14, -14, 0, 10, -10, 13, -12, -3, -11, -2][i]
        x = 1 if x != w else 0
        z = (z * (25+x)) + 1
        z += int((w + [2, 4, 8, 7, 12, 7, 10, 14, 2, 6, 8, 11, 5, 11][i]) * x)
        print(chknum, w, x, y, z, '')
    n = input()
    return chknum, w, x, y, z, ''

def nextnum():
    for i1 in range(9,0, -1):
        for i2 in range(5,0, -1):
            for i3 in range(9,0, -1):
                for i4 in range(9,0, -1):
                    for i5 in range(9,0, -1):
                        for i6 in range(9,0, -1):
                            for i7 in range(9,0, -1):
                                for i8 in range(9,0, -1):
                                    for i9 in range(9,0, -1):
                                        for i10 in range(9,0, -1):
                                            for i11 in range(9,0, -1):
                                                for i12 in range(9,0, -1):
                                                    for i13 in range(9,0, -1):
                                                        for i14 in range(9,0, -1):
                                                            yield int("".join([
                                                                str(i1),
                                                                str(i2),
                                                                str(i3),
                                                                str(i4),
                                                                str(i5),
                                                                str(i6),
                                                                str(i7),
                                                                str(i8),
                                                                str(i9),
                                                                str(i10),
                                                                str(i11),
                                                                str(i12),
                                                                str(i13),
                                                                str(i14),
                                                            ]))

maxnum = int("".join(['9']*14))
for i in nextnum():
    if i % 10000 == 0:
        print(i)
    chknum = str(i)
    if '0' in chknum:
        continue
    else:
        _, w, x, y, z, err = monad(chknum)
        if z == 0:
            print(f"Found z=0: {chknum}")
            break
