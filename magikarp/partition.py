import itertools
import random
from copy import  deepcopy

from magikarp.abstract import AbstractProblem, AbstractExhaustiveSolver, MinMaxEnum, AbstractSolver
from magikarp.simulated_annealing import AbstractSimulatedAnnealingSolver


class PartitionProblem(AbstractProblem):
    "Represents an instance of the partition difference optimization problem."
    MIN_MAX_TYPE = MinMaxEnum.MIN
    def __init__(self, array):
        self.array = array
        super(PartitionProblem, self).__init__()

    def evaluate_solution(self, solution):
        p1_indices, p2_indices = solution
        p1_sum = sum([self.array[i] for i in p1_indices])
        p2_sum = sum([self.array[i] for i in p2_indices])
        return abs(p1_sum - p2_sum)

    def get_array(self):
        return self.array

    def better_score(self, score1, score2):
        return score1 < score2

class ExhaustivePartitionSolver(AbstractExhaustiveSolver):
    def _get_potential_solutions(self):
        index_list = range(len(self.problem.get_array()))
        index_set = set(index_list)
        for first_partition_size in range(1, int(len(index_set) / 2) + 1):
            for first_partition in itertools.combinations(index_list, first_partition_size):
                second_partition = list(index_set - set(first_partition))
                yield first_partition, second_partition

    def _get_worst_possible_solution_value(self):
        return float('inf')

class GreedyPartitionSolver(AbstractSolver):
    def solve(self):
        array_values_and_indices = [(v, i) for i, v in enumerate(self.problem.get_array())]
        sorted_values = sorted(array_values_and_indices, reverse=True)
        p1, p2 = [], []
        p1_sum, p2_sum = 0, 0
        for v, i in sorted_values:
            if p1_sum <= p2_sum:
                p1.append(i)
                p1_sum += v
            else:
                p2.append(i)
                p2_sum += v
        return p1, p2

class SimulatedAnnealingPartitionSolver(AbstractSimulatedAnnealingSolver):
    def _get_neighbor(self, current_point):
        left_partition, right_partition = deepcopy(current_point)
        if not left_partition:
            source, target = right_partition, left_partition
        elif not right_partition:
            source, target = left_partition, right_partition
        else:
            if random.random() > 0.5:
                source, target = left_partition, right_partition
            else:
                source, target = right_partition, left_partition
        source, target = self._move_element(source, target)
        return source, target

    def _move_element(self, source, target):
        i = random.randint(0, len(source) - 1)
        element = source.pop(i)
        target.append(element)
        return source, target