# Reverse engineering

## annotate jumps

```bash
# a=1, b=0
1      jio a, +16 # JMP_1_FROM
2      inc a
3      inc a
4      tpl a
5      tpl a
6      tpl a
7      inc a
8      inc a
9      tpl a
10     inc a
11     inc a
12     tpl a
13     tpl a
14     tpl a
15     inc a
16     jmp +23 # JMP_2_FROM
17     tpl a # # JMP_1_TO
18     inc a
19     inc a
20     tpl a
21     inc a
22     inc a
23     tpl a
24     tpl a
25     inc a
26     inc a
27     tpl a
28     inc a
29     tpl a
30     inc a
31     tpl a
32     inc a
33     inc a
34     tpl a
35     inc a
36     tpl a
37     tpl a
38     inc a
39     jio a, +8 # JMP_2_TO, JMP_3_FROM, JMP_5_TO
40     inc b
41     jie a, +4 # JMP_4_FROM
42     tpl a
43     inc a
44     jmp +2 #JMP_6_FROM
45     hlf a # JMP_4_TO
46     jmp -7 # JMP_5_FROM, #JMP_6_TO
       # JMP_3_TO
```

## simplify

```bash
# a=1, b=0
1      jio a, +16 # JMP_1_FROM
        a = ((((((a+2)*3*3*3)+2)*3)+2)*3*3*3)+1
16     jmp +23 # JMP_2_FROM
17     # # JMP_1_TO
        a = (((((((((((((((a*3)+2)*3)+2)*3*3)+2)*3)+1)*3)+1)*3)+2)*3)+1)*3*3)+1
39     jio a, +8 # JMP_2_TO, JMP_3_FROM, JMP_5_TO
        b = b+1
41     jie a, +4 # JMP_4_FROM
        a = (a*3)+1
44     jmp +2 #JMP_6_FROM
        a = a/2 # JMP_4_TO
46     jmp -7 # JMP_5_FROM, #JMP_6_TO
       # JMP_3_TO
```

## codify

```py
if a % 2 == 0:
    # a = ((((((a+2)*3*3*3)+2)*3)+2)*3*3*3)+1
    a = ((((((a+2)*27)+2)*3)+2)*27)+1
else:
    # a = (((((((((((((((a*3)+2)*3)+2)*3*3)+2)*3)+1)*3)+1)*3)+2)*3)+1)*3*3)+1
    a = (((((((((((((((a*3)+2)*3)+2)*9)+2)*3)+1)*3)+1)*3)+2)*3)+1)*9)+1

while a != 1:
    b=b+1
    if a%2 = 1:
        a = (a*3)+1
    else:
        a = a/2

```

## finished

```py
# a = 0
a = 1
b = 0
if a % 2 == 0:

    # a = ((((((a+2)*3*3*3)+2)*3)+2)*3*3*3)+1
    # a = ((((((a + 2) * 27) + 2) * 3) + 2) * 27) + 1
    a = 2187 * a + 4591
else:
    # a = (((((((((((((((a*3)+2)*3)+2)*3*3)+2)*3)+1)*3)+1)*3)+2)*3)+1)*3*3)+1
    a = 59049 * a + 54334

while a != 1:
    b = b + 1
    if a % 2 == 1:
        a = (a * 3) + 1
    else:
        a = a / 2

print(a, b)
```