""" Advent of code 2021 day 08 / 2"""

from os import path


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines, seg_nums)
        result = 0
        m = {
            1: 2,
            4: 4,
            7: 3,
            8: 7,
            2: 5,
            3: 5,
            5: 5,
            6: 6,
            0: 6,
            9: 6,
        }

        #   0:      1:      2:      3:      4:
        #  aaaa    ....    aaaa    aaaa    ....
        # b    c  .    c  .    c  .    c  b    c
        # b    c  .    c  .    c  .    c  b    c
        #  ....    ....    dddd    dddd    dddd
        # e    f  .    f  e    .  .    f  .    f
        # e    f  .    f  e    .  .    f  .    f
        #  gggg    ....    gggg    gggg    ....

        #   5:      6:      7:      8:      9:
        #  aaaa    aaaa    aaaa    aaaa    aaaa
        # b    .  b    .  .    c  b    c  b    c
        # b    .  b    .  .    c  b    c  b    c
        #  dddd    dddd    ....    dddd    dddd
        # .    f  e    f  .    f  e    f  .    f
        # .    f  e    f  .    f  e    f  .    f
        #  gggg    gggg    ....    gggg    gggg

        for [pt, o] in self.lines:
            # they shall be counted in the displays one by one not overall!!!
            mp = [None] * 10
            for [p, l] in pt:
                # calc the easy ones
                if l == m[1]:
                    mp[1] = p
                elif l == m[4]:
                    mp[4] = p
                elif l == m[7]:
                    mp[7] = p
                elif l == m[8]:
                    mp[8] = p

            for [p, l] in pt:
                if l == m[6]:
                    # we can figure out 6 from it has 1 side match with 1
                    if len(mp[1].difference(p)) == 1:
                        mp[6] = p

            for [p, l] in pt:
                if (l == m[5] or l == m[3] or l == m[2]):
                    if len(mp[1].difference(p)) == 0:
                        # 3 has one side in common with 1
                        mp[3] = p
                    elif len(p.difference(mp[6])) == 0:
                        # 5 perfectly fits into 6
                        mp[5] = p
                    else:
                        # otherwise its definitely 2
                        mp[2] = p

            for [p, l] in pt:
                if (l == m[9] or l == m[0]) and not p in mp:
                    if len(mp[5].difference(p)) == 0:
                        # 5 perfectly fits into 9, but we shall not count 6
                        mp[9] = p
                    else:
                        # otherwise 0
                        mp[0] = p

            curr_val = ""
            for [p, l] in o:
                curr_val += str(mp.index(p))
            result += int(curr_val)
        return result


def preprocess(raw_data):
    # pattern = re.compile(r'([a-z ]+) ([a-z ]+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = ["".join(["".join(sorted(z)) for z in x.strip()])
                for x in line.split("|") if x != '']
        txt = [(set(x), len(x)) for x in data[0].split(" ")]
        obs = [(set(x), len(x)) for x in data[1].split(" ")]
        processed_data.append([txt, obs])
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)

    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
