import copy
import itertools
import math
import random

from magikarp.abstract import AbstractExhaustiveSolver, AbstractProblem, MinMaxEnum
from magikarp.simulated_annealing import AbstractSimulatedAnnealingSolver


class TravellingSalespersonProblem(AbstractProblem):
    MIN_MAX_TYPE = MinMaxEnum.MIN
    def __init__(self, points):
        self.points = points
        super(TravellingSalespersonProblem, self).__init__()

    def get_points(self):
        return self.points

    def _distance(self, p1, p2):
        return math.sqrt(sum([(x1-x2)**2 for x1, x2 in zip(p1, p2)]))

    def evaluate_solution(self, path_indices):
        "Return the distance along the path and back to the initial node."
        circuit_index_pairs = [(p_i, p_i_next) for p_i, p_i_next in zip(path_indices[:-1], path_indices[1:])] + [(path_indices[-1], path_indices[0])]
        circuit_point_pairs = [(self.points[i1], self.points[i2]) for i1, i2 in circuit_index_pairs]
        return sum([self._distance(p1, p2) for p1, p2 in circuit_point_pairs])

    def better_score(self, score1, score2):
        "Return True if the first score is better than (or equal to) the second."
        return score1 <= score2

class ExhaustiveTSPSolver(AbstractExhaustiveSolver):
    def _get_potential_solutions(self):
        index_size = len(self.problem.get_points())
        all_indices = list(range(1, index_size))
        for tail_permutation in itertools.permutations(all_indices):
            yield [0] + list(tail_permutation)

    def _candidate_solution_is_better(self, candidate_solution_value, best_solution_value):
        return candidate_solution_value < best_solution_value

    def _get_worst_possible_solution_value(self):
        return float('inf')
#
class SimulatedAnnealingTSPSolver(AbstractSimulatedAnnealingSolver):
    def _get_neighbor(self, current_point):
        next_point = copy.deepcopy(current_point)
        max_index = len(next_point) - 1
        i1 = random.randint(1, max_index)
        i2 = random.randint(1, max_index)
        next_point[i1], next_point[i2] = next_point[i2], next_point[i1]
        return next_point