""" Advent of code 2023 day 22 / 1 """

import re
from os import path
from copy import deepcopy
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.widgets import Button
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from functools import total_ordering
from utils import log, profiler


def add(a, b):
    return tuple(map(sum, zip(a, b)))


@total_ordering
class Brick:
    def __init__(self, index, p1, p2, stopped):
        self.index = index
        self.p1 = p1
        self.p2 = p2
        self.initial_p1 = p1
        self.initial_p2 = p2
        self.stopped = stopped
        self.initial_stopped = stopped

    def reset_position(self):
        self.p1 = self.initial_p1
        self.p2 = self.initial_p2
        self.stopped = self.initial_stopped

    def __repr__(self):
        return f"{self.index}:{self.p1}~{self.p2}"

    def __lt__(self, other):
        return min(self.p1[2], self.p2[2]) < min(other.p1[2], other.p2[2])

    def get_bounds(self):
        x_min = min(self.p1[0], self.p2[0])
        y_min = min(self.p1[1], self.p2[1])
        z_min = min(self.p1[2], self.p2[2])
        x_max = max(self.p1[0], self.p2[0])
        y_max = max(self.p1[1], self.p2[1])
        z_max = max(self.p1[2], self.p2[2])
        return ((x_min, y_min, z_min), (x_max, y_max, z_max))

    def check_collision(self, other):
        (x_min1, y_min1, z_min1), (x_max1, y_max1, z_max1) = self.get_bounds()
        (x_min2, y_min2, z_min2), (x_max2, y_max2, z_max2) = other.get_bounds()

        x_overlap = x_min1 <= x_max2 and x_max1 >= x_min2
        y_overlap = y_min1 <= y_max2 and y_max1 >= y_min2
        z_overlap = z_min1 <= z_max2 and z_max1 >= z_min2

        return x_overlap and y_overlap and z_overlap

    def has_collision(self, other_rects):
        # Check collision with floor
        if min(self.p1[2], self.p2[2]) < 0:
            return True

        # Check collision with other rectangles
        for other in other_rects:
            if other != self and other.stopped:
                if self.check_collision(other):
                    # log.debug(f"{self} collides with {other}")
                    return True

        return False

    def fall(self, others) -> bool:
        if self.stopped:
            return False

        self.p1 = add(self.p1, (0, 0, -1))
        self.p2 = add(self.p2, (0, 0, -1))

        collide_with_others = self.has_collision(others)
        if collide_with_others:
            self.stopped = True
            # revert movement
            self.p1 = add(self.p1, (0, 0, 1))
            self.p2 = add(self.p2, (0, 0, 1))
            return False
        return True


class Code:
    def __init__(self, lines, visualize=False):
        self.bricks = lines
        self.visualize = visualize
        self.continue_flag = False
        self.fig = None
        self.ax = None
        self.result = None

    def visualize_bricks(self, bricks, title="Brick Positions", pause_and_wait=False):
        if not self.visualize:
            return

        # Create figure if not exists
        if self.fig is None:
            plt.ion()  # Turn on interactive mode
            self.fig = plt.figure(figsize=(12, 9))
            self.ax = self.fig.add_subplot(111, projection="3d")

            # Create a button axes and button
            button_ax = self.fig.add_axes([0.81, 0.05, 0.1, 0.075])
            self.continue_button = Button(button_ax, "Continue")
            self.continue_button.on_clicked(self.on_continue_click)

        # Clear previous plot
        self.ax.clear()

        # Set up the plot
        self.ax.set_title(title)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")

        # Plot each brick
        for brick in bricks:
            # Determine color based on stopped status
            color = "grey" if brick.stopped else "red"

            # Get brick coordinates
            x_min, y_min, z_min = (
                min(brick.p1[0], brick.p2[0]),
                min(brick.p1[1], brick.p2[1]),
                min(brick.p1[2], brick.p2[2]),
            )
            x_max, y_max, z_max = (
                max(brick.p1[0], brick.p2[0]) + 0.9,
                max(brick.p1[1], brick.p2[1]) + 0.9,
                max(brick.p1[2], brick.p2[2]) + 0.9,
            )

            # Create cuboid for each brick
            xs = [x_min, x_max, x_max, x_min, x_min, x_max, x_max, x_min]
            ys = [y_min, y_min, y_max, y_max, y_min, y_min, y_max, y_max]

            # Plot the cuboid
            for i in range(0, 4):
                # Bottom face
                self.ax.plot3D(
                    xs[i : i + 2], ys[i : i + 2], [z_min, z_min], color=color, alpha=0.6
                )
                # Top face
                self.ax.plot3D(
                    xs[i : i + 2], ys[i : i + 2], [z_max, z_max], color=color, alpha=0.6
                )
                # Vertical edges
                self.ax.plot3D(
                    [xs[i], xs[i]],
                    [ys[i], ys[i]],
                    [z_min, z_max],
                    color=color,
                    alpha=0.6,
                )

        # Adjust the plot
        self.ax.set_xlim(0, max(b.p1[0] for b in bricks) + 1)
        self.ax.set_ylim(0, max(b.p1[1] for b in bricks) + 1)
        self.ax.set_zlim(0, max(max(b.p1[2], b.p2[2]) for b in bricks) + 1)

        # Draw the plot
        plt.draw()
        plt.pause(0.1)

        # Pause and wait if requested
        if pause_and_wait:
            self.continue_flag = False
            while not self.continue_flag:
                plt.pause(0.1)

    def on_continue_click(self, event):
        """Callback for the continue button"""
        self.continue_flag = True
        if self.fig:
            plt.close(self.fig)
            self.fig = None

    def fall_bricks(self, b, fastforward=False):
        bricks = sorted(deepcopy(b))

        has_moving = True
        for x in bricks:
            x.stopped = False

        if self.visualize:
            self.visualize_bricks(bricks, "Initial State", pause_and_wait=True)

        total_falls = 0
        stepnum = 0
        while has_moving:

            fall_count = 0
            moving_bricks = 0
            for b in bricks:
                if b.stopped:
                    continue

                # others = [x for x in bricks if b != x]
                fell = b.fall(bricks)
                fall_count += 1 if fell else 0

                # Visualize each step if visualization is enabled
                if self.visualize:
                    self.visualize_bricks(bricks, f"Falling Bricks - Step {fall_count}")
                moving_bricks += 1 if not b.stopped else 0

            has_moving = moving_bricks > 0
            log.debug(
                "#%d step has %d/%d falling blocks (%d)",
                stepnum,
                moving_bricks,
                len(bricks),
                fall_count,
            )
            total_falls = max(moving_bricks, total_falls)
            stepnum += 1

        # Final visualization
        if self.visualize:
            self.visualize_bricks(bricks, "Final Settled State", pause_and_wait=True)
            plt.ioff()  # Turn off interactive mode

        return bricks, total_falls

    def solve(self):
        result = 0
        log.debug("Start")
        bricks, c = self.fall_bricks(self.bricks, fastforward=False)
        for i, probe in enumerate(bricks):
            log.debug("#%d/%d Probing %s", i, len(bricks), probe)
            filtered_list = [x for x in bricks if x.index != probe.index]

            _, c = self.fall_bricks(filtered_list, fastforward=True)
            log.debug("%d blocks fell without %s", c, probe)
            result += c
        return result


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)")
    processed_data = []
    index = 0
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        if match:
            data = Brick(
                index,
                (int(match.group(1)), int(match.group(2)), int(match.group(3))),
                (int(match.group(4)), int(match.group(5)), int(match.group(6))),
                stopped=False,
            )
            index += 1
            processed_data.append(data)
    return processed_data


@profiler
def solution(data, visualize=False):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines, visualize)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        # Set visualize=True to enable 3D visualization
        print(solution(input_file.read(), visualize=False))
