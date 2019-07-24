a = 1
b = 0
c = 128
d = 0
f = 836 + c #964
if a == 1:
    c = 10550400
    f = f + c #10551364
    a = 0
for b in range(1, f+1):
    if (f % b) == 0:
        a += b
print(a)