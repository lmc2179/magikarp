import itertools
from magikarp.abstract import AbstractExhaustiveSolver, AbstractSolver, AbstractProblem

class KnapsackProblem(AbstractProblem):
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

    def get_weight(self, i):
        return self.weights[i]

    def get_weights(self):
        return self.weights

    def get_values(self):
        return self.values

    def get_value(self, i):
        return self.values[i]

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

class GreedyKnapsackSolver(AbstractSolver):
    def solve(self, problem):
        sorted_indices = self._get_sorted_indices(problem)
        selected_indices = self._select_indices(sorted_indices, problem)
        return selected_indices

    def _get_sorted_indices(self, problem):
        decorated_indices = [self._decorate_with_value_ratio(i, problem)
                             for i in range(problem.get_number_items())]
        sorted_decorated_indices = sorted(decorated_indices, reverse=True)
        return [index for value_ratio, index in sorted_decorated_indices]

    def _decorate_with_value_ratio(self, i, problem):
        value_ratio = 1.0 * problem.get_value(i) / problem.get_weight(i)
        return (value_ratio, i)

    def _select_indices(self, sorted_indices, problem):
        total_weight = 0
        selected_indices = []
        for index in sorted_indices:
            if total_weight + problem.get_weight(index) <= problem.get_limit():
                total_weight += problem.get_weight(index)
                selected_indices.append(index)
        return selected_indices
