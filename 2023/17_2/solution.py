""" Advent of code 2023 day 17 / 2 """

from os import path
import utils
import heapq

DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}
TURNS = {
    "N": ["W", "E"],
    "S": ["E", "W"],
    "W": ["S", "N"],
    "E": ["N", "S"],
}

FOUR_NEIGHBOR = DIRECTIONS.values()

CAN_STOP_TURN = 4 - 1
MUST_TURN = 10 - 1


class Code(object):
    def __init__(self, lines):
        self.matrix = lines
        self.maxh = len(lines) - 1
        self.maxw = len(lines[0]) - 1

    def shortest_paths(self, start):
        init_heat_loss = 0
        init_y = start[0]
        init_x = start[1]
        init_dirs = ["E", "S"]
        init_dir_count = 0

        queue = [
            (
                init_heat_loss
                + self.matrix[init_y + DIRECTIONS[d][0]][init_x + DIRECTIONS[d][1]],
                (
                    init_y + DIRECTIONS[d][0],
                    init_x + DIRECTIONS[d][1],
                ),
                d,
                init_dir_count,
                d,
            )
            for d in init_dirs
        ]

        heatlosses = {}
        globalmin = 9999999999
        while queue:
            prev_state = heapq.heappop(queue)
            (
                curr_heatloss,
                curr_position,
                prev_direction,
                prev_direction_count,
                curr_route,
            ) = prev_state
            curr_y, curr_x = curr_position
            hlkey = (curr_y, curr_x, prev_direction, prev_direction_count)
            if hlkey in heatlosses:
                if curr_heatloss < heatlosses[hlkey]:
                    heatlosses[hlkey] = curr_heatloss
                    print("Priqueue is bad:", heatlosses[hlkey], curr_heatloss)
                else:
                    continue
            else:
                heatlosses[hlkey] = curr_heatloss
            # movement: can move 4 before it can turn, and have to turn after 10 movement
            new_direction_list = [prev_direction]
            if prev_direction_count >= CAN_STOP_TURN:
                new_direction_list = [prev_direction] + TURNS[prev_direction]
            if prev_direction_count >= MUST_TURN:
                # can not move straight
                new_direction_list = TURNS[prev_direction]

            for new_direction in new_direction_list:
                d_y, d_x = DIRECTIONS[new_direction]
                next_y = curr_y + d_y
                next_x = curr_x + d_x
                if not ((0 <= next_y <= self.maxh) and (0 <= next_x <= self.maxw)):
                    # do not explore out of bounds...
                    continue

                next_manhattan_distance = (self.maxh - next_y) + (self.maxw - next_x)
                next_heatloss = curr_heatloss + self.matrix[next_y][next_x]
                next_direction_count = (
                    prev_direction_count + 1 if prev_direction == new_direction else 0
                )
                if next_heatloss > globalmin:
                    # optimization: ignore if it's higher than globalmin
                    continue
                    # pass
                if next_y == self.maxh and next_x == self.maxw:
                    # exit condition
                    if next_direction_count < CAN_STOP_TURN:
                        continue
                    if next_heatloss < globalmin:
                        globalmin = next_heatloss
                        print(
                            f"{globalmin}, {len(queue)} - {curr_y}:{curr_x}:{curr_heatloss}"
                        )
                    # print(curr_route)
                    continue

                if (next_heatloss + next_manhattan_distance) > globalmin:
                    # optimization: it won't be less than the manhattan distance, assuming 1s in the route
                    continue
                new_value = (
                    next_heatloss,
                    (next_y, next_x),
                    new_direction,
                    next_direction_count,
                    "", # curr_route + new_direction,
                )
                heapq.heappush(
                    queue,
                    new_value,
                )
        return globalmin

    def solve(self):
        # pprint(self.matrix)
        result = self.shortest_paths((0, 0))
        return result


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        data = [int(x) for x in line]
        processed_data.append(data)
    return processed_data


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read()))
