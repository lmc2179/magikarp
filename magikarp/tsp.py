import math
import itertools

class TravellingSalespersonProblem(object):
    def __init__(self, points):
        self.points = points

    def get_points(self):
        return self.points

    def _distance(self, p1, p2):
        return math.sqrt(sum([(x1-x2)**2 for x1, x2 in zip(p1, p2)]))

    def evaluate_solution(self, path_indices):
        circuit_index_pairs = [(p_i, p_i_next) for p_i, p_i_next in zip(path_indices[:-1], path_indices[1:])] + [(path_indices[-1], path_indices[0])]
        circuit_point_pairs = [(self.points[i1], self.points[i2]) for i1, i2 in circuit_index_pairs]
        return sum([self._distance(p1, p2) for p1, p2 in circuit_point_pairs])

class ExhaustiveTSPSolver(object):
    def solve(self, problem):
        potential_solutions = self._get_potential_solutions(problem)
        best = self._get_best_solution(potential_solutions, problem)
        return best

    def _get_potential_solutions(self, problem):
        index_size = len(problem.get_points())
        all_indices = list(range(index_size))
        return itertools.permutations(all_indices)

    def _get_best_solution(self, potential_solutions, problem):
        shortest_so_far = float('inf')
        best_so_far = None
        for sol in potential_solutions:
            solution_cost = problem.evaluate_solution(sol)
            if solution_cost < shortest_so_far:
                shortest_so_far = solution_cost
                best_so_far = sol
        return best_so_far
