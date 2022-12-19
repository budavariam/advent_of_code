""" Advent of code 2022 day 19 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils
import queue


def calc(current_resources, robot_resources, robot_num, index):
    current_resources[0] -= robot_resources[0]
    current_resources[1] -= robot_resources[1]
    current_resources[2] -= robot_resources[2]
    return current_resources, tuple(
        x + 1 if index == i else x for i, x in enumerate(robot_num)
    )


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self, blueprints, start_minutes):
        max_vals = []
        for costs in blueprints.values():
            robot_ore, robot_clay, robot_obsidian, robot_geode = costs
            robot_min = min(robot_ore[0], robot_clay[0])
            resources = [robot_min, 0, 0, 0]
            minutes = start_minutes - robot_min

            find_max = 0
            robots_num = (1, 0, 0, 0)
            visited = set()
            q = queue.Queue()
            q.put((0, (resources, minutes, robots_num)))
            
            while not q.empty():
                max_val, rest = q.get()
                current_resources, current_minutes, robots_num = rest
                visited.add(robots_num)
                if current_minutes == 0:
                    if max_val > find_max:
                        find_max = max_val
                    continue
                new_minutes = current_minutes - 1
                for ir, robot in enumerate(costs[::-1]):
                    cr = current_resources.copy()
                    eval_count = sum([1 if x[0] <= x[1] else 0 for x in zip(robot, cr[:-1])])
                    if eval_count == 3:
                        for index, r in enumerate(robots_num):
                            cr[index] += r
                        if ir == 0:
                            cr, new_robots_num = calc(cr, robot_geode, robots_num, 3)
                            if new_robots_num not in visited:
                                q.put((cr[3], (cr.copy(), new_minutes, new_robots_num)))
                            break
                        elif ir == 1:
                            cr, new_robots_num = calc(cr, robot_obsidian, robots_num, 2)
                            if new_robots_num not in visited:
                                q.put((cr[3], (cr.copy(), new_minutes, new_robots_num)))
                            break
                        elif ir == 2:
                            cr, new_robots_num = calc(cr, robot_clay, robots_num, 1)
                            if new_robots_num not in visited:
                                q.put((cr[3], (cr.copy(), new_minutes, new_robots_num)))
                        else:
                            cr, new_robots_num = calc(cr, robot_ore, robots_num, 0)
                            if new_robots_num not in visited:
                                q.put((cr[3], (cr.copy(), new_minutes, new_robots_num)))
                cr = current_resources.copy()
                for index, r in enumerate(robots_num):
                    cr[index] += r
                new_val = cr[3]
                q.put((new_val, (cr.copy(), new_minutes, robots_num)))
            max_vals.append(find_max)
        result = 0
        for i, v in enumerate(max_vals):
            result += (i + 1) * v
        return result


@utils.profiler
def preprocess(raw_data):
    processed_data = defaultdict(list)
    pattern = re.compile(
        r".*costs (?P<ore>\d* ore)?(?: and )?(?P<clay>\d* clay)?(?: and )?(?P<obsidian>\d* obsidian)?"
    )
    get_cost = lambda unit: int(unit.split(" ")[0]) if unit is not None else 0
    for v, i in enumerate(raw_data.split("\n")):
        splitted = i.split(". ")
        for bot in splitted:
            match = re.match(pattern, bot)
            processed_data[v + 1].append(
                (
                    get_cost(match.group("ore")),
                    get_cost(match.group("clay")),
                    get_cost(match.group("obsidian")),
                )
            )

    return processed_data


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve(lines, 24)


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))

#     p2 = max_vals[0]
#     for i in max_vals[1:]:
#         p2 *= i
#     print(f"Solution to Part 2 is {p2}")
