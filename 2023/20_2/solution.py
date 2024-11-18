""" Advent of code 2023 day 20 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import deque
from utils import log, profiler


LOW = 0
HIGH = 1

OFF = 0
ON = 1


class Module:
    def __init__(self, d_name, connected, processing=False):
        if d_name[0] in ["%", "&"]:
            self.d_name = d_name[1:]
            # d_type: flip-flop:%, conjunction:&, button, broadcaster
            self.d_type = d_name[0]
        else:
            self.d_name = d_name
            self.d_type = d_name
        self.destination = [x for x in connected.split(", ") if x != ""]
        self.state = OFF
        self.processing = processing
        self.memory = {}
        self.input_modules = []
        self.incoming_pulses = deque([])
        self.outgoing_pulses = deque([])
        self.prev_pulse = None

    def add_input_module(self, module_name: str):
        self.memory[module_name] = LOW
        self.input_modules.append(module_name)

    def deliver_pulse(self, src, p):
        # self.incoming_pulses = deque([])
        self.processing = True
        # print(f"Save {p} to {self}")
        self.incoming_pulses.append(p)
        if self.d_type == "%":
            # Flip-flop modules (prefix %) are either on or off;
            # they are initially off.
            # If a flip-flop module receives a high pulse,
            #   it is ignored and nothing happens.
            # However, if a flip-flop module receives a low pulse,
            #   it flips between on and off.
            #   If it was off: it turns on and sends a high pulse.
            #   If it was on: it turns off and sends a low pulse.
            if p == LOW:
                self.state = 1 - self.state
            elif p == HIGH:
                # self.processing = False
                pass
        elif self.d_type == "&":
            # Conjunction modules (prefix &) remember the type of the most
            # recent pulse received from each of their connected input modules;
            # they initially default to remembering a low pulse for each input.
            # When a pulse is received, the conjunction module
            # first updates its memory for that input.
            # Then, if it remembers high pulses for all inputs,
            # it sends a low pulse; otherwise, it sends a high pulse.
            self.memory[src] = p
        elif self.d_type == "broadcaster":
            # There is a single broadcast module (named broadcaster).
            # When it receives a pulse, it sends the same pulse
            # to all of its destination modules.
            self.state = p
        return self.destination

    def evaluate_pulse(self):
        self.outgoing_pulses = deque([])
        # print(self, self.incoming_pulses)
        curr_pulse = (
            self.incoming_pulses.popleft() if len(self.incoming_pulses) > 0 else None
        )
        if self.processing:
            self.processing = False
        else:
            # print(f"Ignore processing... {self.d_name}")
            # return self.pulses
            pass
        if self.d_type == "button":
            self.outgoing_pulses.extend(
                [(self.d_name, "broadcaster", LOW) for d in self.destination]
            )
        elif self.d_type == "%":
            # Flip-flop modules (prefix %) are either on or off;
            # they are initially off. If a flip-flop module receives a high pulse,
            # it is ignored and nothing happens. However,
            # if a flip-flop module receives a low pulse,
            # it flips between on and off.
            # If it was off: it turns on and sends a high pulse.
            # If it was on: it turns off and sends a low puls
            if curr_pulse == LOW:
                self.outgoing_pulses.extend(
                    [(self.d_name, d, self.state) for d in self.destination]
                )
        elif self.d_type == "&":
            # Conjunction modules (prefix &) remember the type of the most
            # recent pulse received from each of their connected input modules;
            # they initially default to remembering a low pulse for each input.
            # When a pulse is received, the conjunction module
            # first updates its memory for that input.
            # Then, if it remembers high pulses for all inputs,
            # it sends a low pulse; otherwise, it sends a high pul
            res_pulse = LOW if all(self.memory.values()) else HIGH
            self.outgoing_pulses.extend(
                [(self.d_name, d, res_pulse) for d in self.destination]
            )
        elif self.d_type == "broadcaster":
            # There is a single broadcast module (named broadcaster).
            # When it receives a pulse, it sends the same pulse
            # to all of its destination modules.
            self.outgoing_pulses.extend(
                [(self.d_name, d, self.state) for d in self.destination]
            )
        return self.outgoing_pulses

    def __repr__(self):
        return f"({self.d_type},{self.d_name}: {self.destination})"


# NOTE: Shame on me, I inspected diagram.md and updated manually...
RELEVANT = ["qh", "lt", "bq", "vz"]


class Code(object):
    def __init__(self, lines):
        self.modules = lines

    def generate_diagram(self):
        data = [
            "```mermaid",
            "---",
            "title: AoC 2023/20/2",
            "---",
            "flowchart TD",
        ]
        for m in self.modules.values():
            if m.d_type == "%":
                data.append(rf"   {m.d_name}[[{m.d_type}{m.d_name}]]")
            elif m.d_type == "&":
                data.append(rf"   {m.d_name}[\{m.d_type}{m.d_name}/]")
            else:
                data.append(rf"   {m.d_name}[{m.d_name}]")

        for m in self.modules.values():
            for c in m.destination:
                data.append(f"   {m.d_name} --> {c}")
        data.append("```")

        with open("./20_2/diagram.md", "w", encoding="utf-8") as f:
            f.writelines([x + "\r\n" for x in data])

    def solve(self):
        # pprint(self.modules)
        btn_push_num = 1
        self.generate_diagram()
        conjunction_modules = {}
        try:
            conjunction_modules = {self.modules[x].d_name: -1 for x in RELEVANT}
        except:
            return -1

        while True:
            if all([x > -1 for x in conjunction_modules.values()]):
                break
            if btn_push_num % 100 == 0:
                log.info(btn_push_num)
            bc = self.modules["button"]
            bc.processing = True
            next_module = deque([bc])
            while next_module:
                curr = next_module.popleft()
                # print(f"#{btn_push_num}{curr.d_name}{[m.d_name for m in next_module]}")
                module_connections = curr.evaluate_pulse()
                for c in module_connections:
                    _, next_module_name, next_pulse = c
                    log.debug(
                        f"#{btn_push_num}: send '{curr.d_name}'--{'LOW' if next_pulse == 0 else 'HIGH'}--> '{next_module_name}'"
                    )
                    next_m = self.modules[next_module_name]
                    next_m.deliver_pulse(curr.d_name, next_pulse)
                    if (
                        next_m.d_name in RELEVANT
                        and next_m.d_type == "&"
                        and next_pulse == LOW
                    ):
                        if conjunction_modules[next_m.d_name] == -1:
                            # calculate when does it flip the first time
                            conjunction_modules[next_m.d_name] = btn_push_num
                            log.debug((next_m.d_name, btn_push_num))
                    if next_m.d_name == "rx" and next_pulse == LOW:
                        return btn_push_num
                    next_module.append(next_m)
            btn_push_num += 1
        return math.prod(conjunction_modules.values())


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"^([%&a-z]+) -> (.+)$")
    btn = Module("button", "broadcaster", processing=True)
    processed_data = {btn.d_name: btn}
    module_names = set([])
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = Module(match.group(1), match.group(2))
        processed_data[data.d_name] = data
        module_names.add(data.d_name)
        for conn in data.destination:
            module_names.add(conn)
    # add modules that are not listed as source
    for d_name in module_names:
        if d_name not in processed_data:
            # print(d_name)
            missing = Module(d_name, "")
            processed_data[d_name] = missing
    # set input module connections
    for m in processed_data.values():
        for output in m.destination:
            processed_data[output].add_input_module(m.d_name)

    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read()))

# 3738 * 3820 * 3888 * 4092
# offbyone...
# 3739 * 3821 * 3889 * 4093 = 227411378431763
