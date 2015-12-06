import itertools
from magikarp.abstract import AbstractProblem, AbstractExhaustiveSolver

class PartitionProblem(AbstractProblem):
    "Represents an instance of the partition difference optimization problem."
    def __init__(self, array):
        self.array = array

    def evaluate_solution(self, solution):
        p1_indices, p2_indices = solution
        p1_sum = sum([self.array[i] for i in p1_indices])
        p2_sum = sum([self.array[i] for i in p2_indices])
        return abs(p1_sum - p2_sum)

    def get_array(self):
        return self.array

class ExhaustivePartitionSolver(AbstractExhaustiveSolver):
    def _candidate_solution_is_better(self, candidate_solution_value, best_solution_value):
        return  candidate_solution_value < best_solution_value

    def _get_potential_solutions(self, problem):
        index_list = range(len(problem.get_array()))
        index_set = set(index_list)
        for first_partition_size in range(1, int(len(index_set) / 2) + 1):
            for first_partition in itertools.combinations(index_list, first_partition_size):
                second_partition = list(index_set - set(first_partition))
                yield first_partition, second_partition

    def _get_worst_possible_solution_value(self):
        return float('inf')