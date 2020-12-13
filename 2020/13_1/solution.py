""" Advent of code 2020 day 13/1 """

import math
from os import path


class Schedule(object):
    def __init__(self, data):
        self.start_time, self.shuttle_ids = data

    def solve(self):
        depart_times = [ {
            "id": start, 
            "closest_start": self.start_time - (self.start_time % start) + start,
            "waittime": (self.start_time - (self.start_time % start) + start) - self.start_time,
        } for start in self.shuttle_ids]
        selected_shuttle = min(depart_times, key=lambda x: x["closest_start"])
        return selected_shuttle["id"] * selected_shuttle["waittime"]


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    start_time=int(processed_data[0])
    shuttle_ids=[int(id) for id in processed_data[1].split(',') if id != 'x']
    return (start_time, shuttle_ids)


def solution(input_data):
    """ Solution to the problem """
    data = preprocess(input_data)
    solver = Schedule(data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
