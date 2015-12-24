from collections import defaultdict

from magikarp.abstract import AbstractProblem, MinMaxEnum


class MinimalColoringProblem(AbstractProblem):
    MIN_MAX_TYPE = MinMaxEnum.MIN
    def __init__(self, node_pairs):
        super(MinimalColoringProblem, self).__init__()
        self.adjacency_lookup = self._build_adjacency_lookup(node_pairs)

    def _build_adjacency_lookup(self, node_pairs):
        adjacency_lookup = defaultdict(set)
        for node1, node2 in node_pairs:
            if node1 == node2:
                raise Exception('No self edges allowed')
            adjacency_lookup[node1].add(node2)
            adjacency_lookup[node2].add(node1)
        return adjacency_lookup

    def get_neighbors(self, node):
        return list(self.adjacency_lookup[node])

    def evaluate_solution(self, node_coloring_pairs):
        unvisited_nodes = set(self.adjacency_lookup.keys())
        unique_colors = set()
        coloring_lookup = dict(node_coloring_pairs)
        for node, coloring in node_coloring_pairs:
            unvisited_nodes.remove(node)
            neighbors = self.get_neighbors(node)
            for neighbor in neighbors:
                if coloring_lookup[neighbor] == coloring_lookup[node]:
                    return float('inf') # This is an invalid coloring
            unique_colors.add(coloring)
        return len(unique_colors)