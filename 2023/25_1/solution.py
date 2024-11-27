""" Advent of code 2023 day 25 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler
import networkx as nx
from copy import deepcopy
import matplotlib.pyplot as plt


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def analyze_graph(self, graph, show=False):
        edges = []
        for k, connections in graph.items():
            for v in connections:
                edges.append((k, v))
        graph = nx.Graph()
        graph.add_edges_from(edges)
        pos = nx.spring_layout(graph)  # Force-directed layout
        if show:
            plt.figure(figsize=(10, 10))
            nx.draw(
                graph,
                pos,
                with_labels=True,
                node_size=500,
                node_color="lightblue",
                edge_color="gray",
            )
            plt.title("AoC 25/1", fontsize=16)
            plt.show()
        return list(nx.connected_components(graph))

    def remove_links(self, g, omit_links):
        graph = deepcopy(g)
        for n1, n2 in omit_links:
            if n1 in graph:
                graph[n1] = graph[n1].difference([n2])
            if n2 in graph:
                graph[n2] = graph[n2].difference([n1])
        return graph

    def solve(self):
        graph = self.lines
        # NOTE: lazy solution: generate plot, look into the graph and omit the edges that connect the two subgraphs...
        omit_links = [
            # test
            ("hfx", "pzl"),
            ("nvd", "jqt"),
            ("cmg", "bvb"),
            # myInput
            ("ddc", "gqm"),
            ("tnz", "dgt"),
            ("kzh", "rks"),
        ]
        graph = self.remove_links(graph, omit_links)
        connected_sets = self.analyze_graph(graph, True)

        return math.prod([len(x) for x in connected_sets])


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\w+): (.*)")
    processed_data = defaultdict(set)
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        node_name = match.group(1)
        connections = match.group(2).split(" ")
        for c in connections:
            processed_data[c].add(node_name)
    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
