import itertools
from magikarp.abstract import AbstractExhaustiveSolver

class KnapsackProblem(object):
    "Represents an instance of the 0-1 knapsack problem. Solutions are the indices of the objects chosen."
    def __init__(self, weights, values, limit):
        self.weights = weights
        self.values = values
        self.limit = limit

    def evaluate_solution(self, item_indices):
        total_weight = sum([self.weights[i] for i in item_indices])
        if total_weight > self.limit:
            return 0.0
        else:
            return sum([self.values[i] for i in item_indices])

    def get_weights(self):
        return self.weights

    def get_values(self):
        return self.values

    def get_limit(self):
        return self.limit

    def get_number_items(self):
        return len(self.weights)

class ExhaustiveKnapsackSolver(AbstractExhaustiveSolver):
    def _get_potential_solutions(self, problem):
        return self._get_power_set(range(problem.get_number_items()))

    def _get_power_set(self, items):
        return itertools.chain.from_iterable(itertools.combinations(items, r) for r in range(len(items)+1))

    def _candidate_solution_is_better(self, candidate_solution_value, best_solution_value):
        return candidate_solution_value > best_solution_value

    def _get_worst_possible_solution_value(self):
        return -float('inf')