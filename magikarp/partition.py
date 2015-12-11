import itertools
from magikarp.abstract import AbstractProblem, AbstractExhaustiveSolver, MinMaxEnum

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