""" Advent of code 2021 day 16 / 2 """

import math
from os import path, readlink
import re
from collections import defaultdict

m = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

"""
110100101111111000101000
VVVTTTAAAAABBBBBCCCCC
"""

"""
The three bits labeled V (110) are the packet version, 6.
The three bits labeled T (100) are the packet type ID, 4, which means the packet is a literal value.
The five bits labeled A (10111) start with a 1 (not the last group, keep reading) and contain the first four bits of the number, 0111.
The five bits labeled B (11110) start with a 1 (not the last group, keep reading) and contain four more bits of the number, 1110.
The five bits labeled C (00101) start with a 0 (last group, end of packet) and contain the last four bits of the number, 0101.
The three unlabeled 0 bits at the end are extra due to the hexadecimal representation and should be ignored.
"""

res = []

lvlres = defaultdict(list)

class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.bin = "".join([m[x] for x in lines[0]]).zfill(len(lines[0]) * 4)

    def prnt(self, i, level, *args):
        # pass
        print(" "*level, f"{i}:", " ".join([str(x) for x in args]))

    def operate(self, level, vals, packet_type_id, subvals, nums):
        # print(" "*level, "OPERATE!!!!", packet_type_id)
        res.append(packet_type_id)
        if packet_type_id == 0:
            """Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet."""
            print(" "*level, "sum", vals, subvals, nums)
            return sum(nums)
        elif packet_type_id == 1:
            """Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet."""
            print(" "*level, "product", vals, subvals, nums)
            return math.prod(nums)
        elif packet_type_id == 2:
            """Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets."""
            print(" "*level, "minimum", vals, subvals, nums)
            return min(nums)
        elif packet_type_id == 3:
            """Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets."""
            print(" "*level, "maximum", vals, subvals, nums)
            return max(nums)
        elif packet_type_id == 4:
            pass 
        elif packet_type_id == 5:
            """Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets."""
            print(" "*level, "greater than", vals, subvals, nums)
            return 1 if nums[0] > nums[1] else 0
        elif packet_type_id == 6:
            """Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets."""
            print(" "*level, "less than", vals, subvals, nums)
            return 1 if nums[0] < nums[1] else 0
        elif packet_type_id == 7:
            """Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets."""
            print(" "*level, "equal to", vals, subvals, nums)
            return 1 if nums[0] == nums[1] else 0
        return vals

    def parse_packets(self, txt, level, p_i, stopCnt=0):
        # print(lvlres)
        try:
            i = 0
            res_v = 0
            read_packet = 0
            vals = 0
            nums = []
            while i < len(txt):
                #c = txt[i:]
                """header"""
                pv_raw = txt[i:i+3]
                if pv_raw == '':
                    # self.prnt(p_i+i, level, "pv_raw empty", pv_raw)
                    return (res_v, i, vals, nums)
                packet_version = int(pv_raw, base=2)
                # res_v += packet_version
                # self.prnt(p_i+i, level, "packet_version", packet_version)
                pt_raw = txt[i+3:i+6]
                if pt_raw == '':
                    # self.prnt(p_i+i, level, "pt_raw empty", pt_raw)
                    return (res_v, i, vals, nums)
                packet_type_id = int(pt_raw, base=2)
                # self.prnt(p_i+i, level, "packet_type_id", packet_type_id)
                i += 6
                if i >= len(txt):
                    return (res_v, i, vals, nums)
                if packet_type_id == 4:
                    # self.prnt(p_i+i, level, "TYPE: literal value: number")
                    should_read_packet = True
                    num = ""
                    while should_read_packet:
                        # each is prefixed with a one except the last
                        should_read_packet = True if txt[i] == '1' else False
                        n = txt[i+1:i+5]  # 4 bits of number
                        if len(n) != 4:
                            raise(Exception("offbyone0"))
                        num += n
                        i += 5
                    num = int(num, base=2)
                    nums.append(num)
                    res.append(packet_type_id)
                    self.prnt(p_i+i, level, "TYPE number", num)
                    
                    # move pointer
                else:
                    # nums = []
                    self.prnt(p_i+i, level, """TYPE: operator""")
                    if i >= len(txt):
                        # self.prnt(p_i+i, level, f"out of range {i} == {len(txt)}")
                        return (res_v, i, vals, nums)
                    length_type_id = txt[i]
                    subvals = []
                    # self.prnt(p_i+i, level, "length_type_id", length_type_id)
                    if length_type_id == '0':
                        """
                        then the next 15 bits are a number that represents 
                        the total length in bits of the sub-packets contained by this packet.
                        """
                        subpacket_raw = txt[i+1:i+16]
                        if subpacket_raw == '':
                            # self.prnt(p_i+i, level, "subpacket_raw empty", subpacket_raw)
                            return (res_v, i, vals, nums)
                        if len(subpacket_raw) != 15:
                            raise(Exception("offbyone0"))
                        subpacket_len = int(subpacket_raw, base=2)
                        # self.prnt(p_i+i, level, "subpacket_len", subpacket_len)
                        subp = txt[i+16:i+16+subpacket_len]
                        if len(subp) != subpacket_len:
                            raise(Exception(f"offbyone02 {len(subp)} != {subpacket_len}"))
                        subpackets, nexti, subvals, subnums = self.parse_packets(
                            subp, level + 1, i+p_i
                        )
                        # nums.append(subvals)
                        # res_v += subpackets
                        # self.prnt(p_i+i, level, "found subpackets: ", subpackets, "res_v", res_v)
                        # move pointer
                        i += 16+subpacket_len
                        if subpacket_len != nexti:
                            raise(Exception(f"offbyone01 {subpacket_len} != {nexti} {p_i} len{len(txt)}"))
                        print("  XXX  ",subpackets, nexti, subvals, subnums, lvlres)
                        vals = self.operate(level, vals, packet_type_id, subvals, subnums)
                        nums.append(vals)
                        res_v = vals
                        lvlres[level].append(vals)
                        # print(lvlres)
                        # nums += [vals]
                        print("OPERATION RESULT", vals)
                    elif length_type_id == '1':
                        """
                        If the length type ID is 1, then the next 11 bits are a number that represents 
                        the number of sub-packets immediately contained by this packet.
                        """
                        subpacket_raw = txt[i+1:i+12]
                        if subpacket_raw == '':
                            self.prnt(p_i+i, level, "subpacket_raw2 empty", subpacket_raw)
                            return (res_v, i, vals, nums)
                        if len(subpacket_raw) != 11:
                            raise(Exception("offbyone1"))
                        subpacket_num = int(subpacket_raw, base=2)
                        self.prnt(p_i+i, level, "found subpackets2", subpacket_num)
                        subpackets, nexti, subvals, subnums = self.parse_packets(
                            txt[i+12:], level+1, i+p_i, subpacket_num
                        )
                        # move pointer
                        i += 12+nexti #+1
                        # print("  ZZZ  ",subpackets, nexti, subvals, subnums, lvlres)
                        vals = self.operate(level, vals, packet_type_id, subvals, subnums)
                        # nums += [vals]
                        nums.append(vals)
                        res_v = vals
                        lvlres[level].append(vals)
                        # print(lvlres)
                        print("OPERATION RESULT", vals)
                read_packet += 1
                if read_packet == stopCnt:
                    self.prnt(p_i+i, level, "read enough packets",
                                read_packet, stopCnt)
                    print("RETURN WITH1: ", (res_v, i, vals, nums, read_packet, stopCnt))
                    return (res_v, i, vals, nums)
            # self.prnt(p_i+i, level, "finished", read_packet - 1, res_v, i)
            print("RETURN WITH2: ", (res_v, i, vals, nums, read_packet, stopCnt))
            return (res_v, i, vals, nums)
        except Exception as e:
            self.prnt(p_i+i, level, e)
            raise(e)
        return (-99999, i)

    def solve(self):
        print(self.lines, self.bin, len(self.bin))
        x = self.parse_packets(self.bin, 0, 0)
        print(x)
        
        return x[2]


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
