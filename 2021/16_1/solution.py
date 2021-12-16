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

    def prnt(self, level, *args):
        print(" "*level, " ".join([str(x) for x in args]))

    def parse_packets(self, txt, level, stopCnt=0):
        try:
            i = 0
            res_v = 0
            read_packet = 0
            while i < len(txt):
                #c = txt[i:]
                """header"""
                pv_raw = txt[i:i+3]
                if pv_raw == '':
                    self.prnt(level, "pv_raw empty", pv_raw)
                    return (res_v, i)
                packet_version = int(pv_raw, base=2)
                res_v += packet_version
                self.prnt(level, "packet_version", packet_version)
                pt_raw = txt[i+3:i+6]
                if pt_raw == '':
                    self.prnt(level, "pt_raw empty", pt_raw)
                    return (res_v, i)
                packet_type_id = int(pt_raw, base=2)
                self.prnt(level, "packet_type_id", packet_type_id)
                j = i+6
                if packet_type_id == 4:
                    self.prnt(level, "TYPE: literal value: number")
                    should_read_packet = True
                    num = ""
                    while should_read_packet:
                        # each is prefixed with a one except the last
                        should_read_packet = True if txt[j] == '1' else False
                        n = txt[j+1:j+5]  # 4 bits of number
                        if len(n) != 4:
                            raise(Exception("offbyone0"))
                        num += n
                        j += 5
                    num = int(num, base=2)
                    self.prnt(level, "Read number", num)
                    # move pointer
                    i += j
                else:
                    self.prnt(level, """TYPE: operator""")
                    length_type_id = txt[j]
                    self.prnt(level, "length_type_id", length_type_id)
                    if length_type_id == '0':
                        """
                        then the next 15 bits are a number that represents 
                        the total length in bits of the sub-packets contained by this packet.
                        """
                        subpacket_raw = txt[j+1:j+16]
                        if len(subpacket_raw) != 15:
                            raise(Exception("offbyone0"))
                        subpacket_len = int(subpacket_raw, base=2)
                        self.prnt(level, "subpacket_len", subpacket_len)
                        subp = txt[j+16:j+16+subpacket_len]
                        if len(subp) != subpacket_len:
                            raise(Exception("offbyone02"))
                        subpackets, nexti = self.parse_packets(
                            subp, level + 1
                        )
                        res_v += subpackets
                        self.prnt(level, "found subpackets: ", subpackets, "res_v", res_v)
                        # move pointer
                        i += 16+subpacket_len+1
                        # ????
                        if subpacket_len != nexti:
                            raise(Exception("offbyone01"))
                    elif length_type_id == '1':
                        """
                        If the length type ID is 1, then the next 11 bits are a number that represents 
                        the number of sub-packets immediately contained by this packet.
                        """
                        subpacket_raw = txt[j+1:j+12]
                        if len(subpacket_raw) != 11:
                            raise(Exception("offbyone1"))
                        subpacket_num = int(subpacket_raw, base=2)
                        self.prnt(level, "found subpackets2", subpacket_num, "res_v", res_v)
                        subpackets, nexti = self.parse_packets(
                            txt[j+12:], level+1, subpacket_num)
                        res_v += subpackets
                        # move pointer
                        i += j+12+nexti+1
                    read_packet += 1
                    if read_packet == stopCnt:
                        self.prnt(level, "read enough packets",
                                  read_packet, stopCnt)
                        return (res_v, i)
            self.prnt(level, "finished", read_packet - 1, res_v, i)
            return (res_v, i)
        except Exception as e:
            self.prnt(level, e)
        return (-99999, i)

    def solve(self):
        print(self.lines, self.bin)
        res, _ = self.parse_packets(self.bin, 0)
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
        self.prnt(level, solution(input_file.read()))
