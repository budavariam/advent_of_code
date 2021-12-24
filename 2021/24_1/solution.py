""" Advent of code 2021 day 24 / 1 """

from os import path
from collections import defaultdict

def all_same(lst):
    return all(x == lst[0] for x in lst)

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        # inp a - Read an input value and write it to variable a.
        # add a b - Add the value of a to the value of b, then store the result in variable a.
        # mul a b - Multiply the value of a by the value of b, then store the result in variable a.
        # div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
        # mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
        # eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
        instr = ["""
import math

def monad(chknum):
    w,x,y,z= [0]*4
        """]
        i = 0
        j = 0
        fordata = defaultdict(list)
        foroline = defaultdict(list)
        for line, oline in self.lines:
            if line[0] == 'inp':
                j=0
                # instr.append(f"    print(chknum,{i},w,x,y,z)")
                instr.append(f"    {line[1]} = int(chknum[{i}])")
                i+=1
            elif line[0] == 'add':
                instr.append(f"    {line[1]} += {line[2]}")
            elif line[0] == 'mul':
                instr.append(f"    {line[1]} *= {line[2]}")
            elif line[0] == 'div':
                instr.append(f"    if {line[2]} == 0: return [chknum,None,None,None,None, 'Failed on div instruction after num {i}'] ")
                instr.append(f"    {line[1]} = math.trunc({line[1]} / {line[2]})")
                """Program authors should be especially cautious; 
                attempting to execute div with b=0
                will cause the program to crash and might even damage the ALU."""
            elif line[0] == 'mod':
                """Program authors should be especially cautious; 
                attempting to execute mod with a<0 or b<=0
                will cause the program to crash and might even damage the ALU."""
                instr.append(f"    if {line[1]} < 0 or {line[2]} < 0: return [chknum,None,None,None,None, 'Faled on mod instruction after num {i}'] ")
                instr.append(f"    {line[1]} %= {line[2]}")
            elif line[0] == 'eql':
                instr.append(f"    {line[1]} = 1 if {line[1]} == {line[2]} else 0")
            foroline[j].append(oline)
            fordata[j].append(line)
            j+=1
            
        # instr.append(f"    print(chknum,{i},w,x,y,z)")
        instr.append(f"    return [chknum,w,x,y,z,None]")
        instr.append("""

maxnum = int("".join(['9']*14))
for i in range(maxnum, 1, -1):
    if i % 10000 == 0:
        print(i)
    chknum = str(i)
    if '0' in chknum:
        continue
    else:
        _, w, x,y,z, err = monad(chknum)
        if z == 0:
            print("Found z=0: {chknum}")
            break
    # for debug
    print(chknum, w,x,y,z) 
    if i == maxnum - 10:
        break
        """)
        resstr = "\n".join(instr)
        simplified = []
        for k in range(0, max(foroline.keys())+1):
            oline = foroline[k]
            dta = fordata[k]
            sm = all_same(oline)
            if sm:
                simplified.append(oline[0])
            else:
                simplified.append((dta[0][0],dta[0][1], [x[2] for x in dta]))
        return resstr


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line.split(" ")
        processed_data.append((data, line))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
