from collections import deque

class CombinatorialSolver(object):
    def __init__(self, frontier_structure_cls, search_strategy):
        self.frontier_structure_cls = frontier_structure_cls
        self.search_strategy = search_strategy

    def find_solution(self):
        frontier = self.frontier_structure_cls()
        initial_frontier = self.search_strategy.get_initial_frontier()
        [frontier.add_node(f) for f in initial_frontier]
        while frontier:
            next_node = frontier.pop()
            new_nodes = self.search_strategy.expand_node(next_node)
            pruned_nodes = self.search_strategy.prune_nodes(new_nodes)
            # Termination conditions? How does these vary between Point and Subset searches?
            # Two termination types: # of iterations, exhausted frontier

class AbstractSearchStrategy(object):
    def get_initial_frontier(self):
        raise NotImplementedError

    def expand_node(self, node):
        raise NotImplementedError

    def prune_nodes(self, new_nodes):
        raise NotImplementedError

class AbstractSearchStructure(object):
    def add_node(self, n):
        raise NotImplementedError

    def pop_node(self):
        raise NotImplementedError

class Stack(AbstractSearchStructure):
    def __init__(self):
        self.list = list()

    def add_node(self, n):
        self.list.append(n)

    def pop_node(self):
        return self.list.pop()

    def __bool__(self):
        return bool(self.list)

class Queue(AbstractSearchStructure):
    def __init__(self):
        self.deque = deque()

    def add_node(self, n):
        self.deque.appendleft(n)

    def pop_node(self):
        return self.deque.pop()

    def __bool__(self):
        return bool(self.deque)