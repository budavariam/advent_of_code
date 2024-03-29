""" Advent of code 2021 day 16 / 1 """

import math
from os import path, readlink
import re

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


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.bin = "".join([m[x] for x in lines[0]])

    def prnt(self, i, level, *args):
        pass
        # print(" "*level, f"{i}:", " ".join([str(x) for x in args]))

    def parse_packets(self, txt, level, p_i, stopCnt=0):
        try:
            i = 0
            res_v = 0
            read_packet = 0
            while i < len(txt):
                #c = txt[i:]
                """header"""
                pv_raw = txt[i:i+3]
                if pv_raw == '':
                    self.prnt(p_i+i, level, "pv_raw empty", pv_raw)
                    return (res_v, i)
                packet_version = int(pv_raw, base=2)
                res_v += packet_version
                self.prnt(p_i+i, level, "packet_version", packet_version)
                pt_raw = txt[i+3:i+6]
                if pt_raw == '':
                    self.prnt(p_i+i, level, "pt_raw empty", pt_raw)
                    return (res_v, i)
                packet_type_id = int(pt_raw, base=2)
                self.prnt(p_i+i, level, "packet_type_id", packet_type_id)
                i += 6
                if i == len(txt):
                    return (res_v, i)
                if packet_type_id == 4:
                    self.prnt(p_i+i, level, "TYPE: literal value: number")
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
                    self.prnt(p_i+i, level, "Read number", num)
                    # move pointer
                else:
                    self.prnt(p_i+i, level, """TYPE: operator""")
                    length_type_id = txt[i]
                    self.prnt(p_i+i, level, "length_type_id", length_type_id)
                    if length_type_id == '0':
                        """
                        then the next 15 bits are a number that represents 
                        the total length in bits of the sub-packets contained by this packet.
                        """
                        subpacket_raw = txt[i+1:i+16]
                        if subpacket_raw == '':
                            self.prnt(p_i+i, level, "subpacket_raw empty", subpacket_raw)
                            return (res_v, i)
                        if len(subpacket_raw) != 15:
                            raise(Exception("offbyone0"))
                        subpacket_len = int(subpacket_raw, base=2)
                        self.prnt(p_i+i, level, "subpacket_len", subpacket_len)
                        subp = txt[i+16:i+16+subpacket_len]
                        if len(subp) != subpacket_len:
                            raise(Exception(f"offbyone02 {len(subp)} != {subpacket_len}"))
                        subpackets, nexti = self.parse_packets(
                            subp, level + 1, i+p_i
                        )
                        res_v += subpackets
                        self.prnt(p_i+i, level, "found subpackets: ", subpackets, "res_v", res_v)
                        # move pointer
                        i += 16+subpacket_len
                        # ????
                        if subpacket_len != nexti:
                            raise(Exception(f"offbyone01 {subpacket_len} != {nexti} {p_i} len{len(txt)}"))
                    elif length_type_id == '1':
                        """
                        If the length type ID is 1, then the next 11 bits are a number that represents 
                        the number of sub-packets immediately contained by this packet.
                        """
                        subpacket_raw = txt[i+1:i+12]
                        if subpacket_raw == '':
                            self.prnt(p_i+i, level, "subpacket_raw2 empty", subpacket_raw)
                            return (res_v, i)
                        if len(subpacket_raw) != 11:
                            raise(Exception("offbyone1"))
                        subpacket_num = int(subpacket_raw, base=2)
                        self.prnt(p_i+i, level, "found subpackets2", subpacket_num, "res_v", res_v)
                        subpackets, nexti = self.parse_packets(
                            txt[i+12:], level+1, i+p_i, subpacket_num
                        )
                        res_v += subpackets
                        # move pointer
                        i += 12+nexti #+1
                    read_packet += 1
                    if read_packet == stopCnt:
                        self.prnt(p_i+i, level, "read enough packets",
                                  read_packet, stopCnt)
                        return (res_v, i)
            self.prnt(p_i+i, level, "finished", read_packet - 1, res_v, i)
            return (res_v, i)
        except Exception as e:
            self.prnt(p_i+i, level, e)
            raise(e)
        return (-99999, i)

    def solve(self):
        print(self.lines, self.bin, len(self.bin))
        res, _ = self.parse_packets(self.bin, 0, 0)
        return res


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
