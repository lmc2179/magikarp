import copy
import itertools
import math
import random

from magikarp.abstract import AbstractExhaustiveSolver, AbstractProblem, MinMaxEnum
from magikarp.point_search import AbstractNeighborStrategy, SimulatedAnnealingSolver, HillClimbingSolver


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
class TSP2OptNeighborStrategy(AbstractNeighborStrategy):
    def get_neighbor(self, current_point):
        next_point = copy.deepcopy(current_point)
        max_index = len(next_point) - 1
        i1, i2 = 1, 1
        while i1 == i2:
            # this loop is a little goofy looking, but it ensures that
            # we don't end up swapping an index with itself (admittedly, this is rare)
            i1 = random.randint(1, max_index)
            i2 = random.randint(1, max_index)
        next_point[i1], next_point[i2] = next_point[i2], next_point[i1]
        return next_point

    def get_neighbors(self, current_point):
        tour_swap_indices = itertools.combinations(range(1, len(current_point)), 2)
        tour_permutations = [self._apply_swap(current_point, i, j) for i, j in tour_swap_indices]
        return [list(tour) for tour in tour_permutations]

    def _apply_swap(self, city, i, j):
        new_city = copy.deepcopy(city)
        new_city[i], new_city[j] = new_city[j], new_city[i]
        return new_city

NEIGHBOR_STRATEGIES = {'2-opt': TSP2OptNeighborStrategy}

def _get_neighbor_strategy(name):
    if name not in NEIGHBOR_STRATEGIES:
        raise Exception('Invalid neighbor type - should be one of {0}'.format(NEIGHBOR_STRATEGIES.keys()))
    return NEIGHBOR_STRATEGIES[name]()

def _get_random_initial_configuration(p):
    cfg = range(len(p.get_points()))
    random.shuffle(cfg)
    return cfg

def solve_tsp_exhaustive(points):
    p = TravellingSalespersonProblem(points)
    solution = ExhaustiveTSPSolver(p).solve()
    return solution, p.evaluate_solution(solution)

def solve_tsp_simulated_annealing(points, no_iterations, cooling_constant, initial_configuration = None):
    p = TravellingSalespersonProblem(points)
    if not initial_configuration:
        initial_configuration = _get_random_initial_configuration(p)
    ns = _get_neighbor_strategy('2-opt') # This is hard-coded for now, until we have more neighborhood types
    solution = SimulatedAnnealingSolver(p, ns).solve(initial_configuration, no_iterations, cooling_constant)
    return solution, p.evaluate_solution(solution)

def solve_tsp_hill_climbing(points, no_iterations, initial_configuration = None):
    p = TravellingSalespersonProblem(points)
    if not initial_configuration:
        initial_configuration = _get_random_initial_configuration(p)
    ns = _get_neighbor_strategy('2-opt') # This is hard-coded for now, until we have more neighborhood types
    solution = HillClimbingSolver(p, ns).solve(initial_configuration, no_iterations)
    return solution, p.evaluate_solution(solution)
