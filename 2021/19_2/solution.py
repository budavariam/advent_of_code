""" Advent of code 2021 day 19 / 2 """

from os import path
from collections import defaultdict


class Code(object):
    def __init__(self, data):
        self.raw_scanner_data = data
        self.grid = set(self.raw_scanner_data.pop(0))
        self.scanners = [(0, 0, 0)]
        self.possibles = lambda x, y, z: [
            (x, y, z),
            (x, z, -y),
            (x, -y, -z),
            (x, -z, y),
            (-x, y, -z),
            (-x, z, y),
            (-x, -y, z),
            (-x, -z, -y),
            (y, x, -z),
            (y, z, x),
            (y, -x, z),
            (y, -z, -x),
            (-y, x, z),
            (-y, z, -x),
            (-y, -x, -z),
            (-y, -z, x),
            (z, x, y),
            (z, y, -x),
            (z, -x, -y),
            (z, -y, x),
            (-z, x, -y),
            (-z, y, x),
            (-z, -x, y),
            (-z, -y, -x)
        ]

    def turn_current_and_append_to_grid(self, current, grid_xyz_shifts):
        orientations = [self.possibles(*x) for x in current]
        for e in range(len(orientations[0])):
            current_orientation = [x[e] for x in orientations]
            _, current_xyz_shifts = self.get_relative_beacon_distance(current_orientation)
            matches = {}
            for k, v in current_xyz_shifts.items():
                for ok, ov in grid_xyz_shifts.items():
                    distance_matches = [x for x in v if x in ov]
                    if len(distance_matches) >= 11:
                        matches[k] = ok
            if len(matches) >= 12:
                xyz_diff = next((tuple(v[i] - k[i] for i in range(3)) for k, v in matches.items()))
                current_grid = set()
                for k in current_orientation:
                    new_coord = tuple(k[i] + xyz_diff[i] for i in range(3))
                    self.grid.add(new_coord)
                    current_grid.add(new_coord)
                point = next((k for k, v in matches.items()))
                self.scanners.append(tuple(matches[point][i] - point[i] for i in range(3)))
                return True, current_grid
        return False, None

    def get_relative_beacon_distance(self, beacons):
        relative_distances = defaultdict(list)
        relative_xyz_shift = defaultdict(list)
        for coords in beacons:
            for other_coords in beacons:
                if coords != other_coords:
                    relative_distances[coords].append(sum([(coords[e] - other_coords[e]) ** 2 for e in range(3)]))
                    relative_xyz_shift[coords].append(tuple(other_coords[x] - coords[x] for x in range(3)))
        return relative_distances, relative_xyz_shift

    def solve(self):
        mapped = [0]
        distance_and_xyz = [self.get_relative_beacon_distance(self.grid)]
        while len(self.raw_scanner_data) > 0:
            for key, current in self.raw_scanner_data.items():
                current_distances, _ = self.get_relative_beacon_distance(current)
                for grid_distances, grid_xyz_shifts in distance_and_xyz:
                    if any(any(len([distance for distance in current_distance if distance in grid_distance]) >= 11 for grid_distance in grid_distances.values()) for current_distance in current_distances.values()):
                        success, temp_grid = self.turn_current_and_append_to_grid(current, grid_xyz_shifts)
                        if success:
                            mapped.append(key)
                            self.raw_scanner_data.pop(key)
                            grid_distances, grid_xyz_shifts = self.get_relative_beacon_distance(temp_grid)
                            distance_and_xyz.append((grid_distances, grid_xyz_shifts))
                            break
                else:
                    continue
                break
        return max(sum([abs(x[i] - y[i]) for i in range(3)]) for x in self.scanners for y in self.scanners)


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = defaultdict(list)
    for i, scanner in enumerate(raw_data.split('\n\n')):
        for scannerline in scanner.splitlines()[1:]:
            processed_data[i].append(tuple(map(int,scannerline.split(','))))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
