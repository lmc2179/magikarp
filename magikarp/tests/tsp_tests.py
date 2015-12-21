import math
import unittest

from magikarp.point_search import SimulatedAnnealingSolver, HillClimbingSolver
from magikarp.tsp import TravellingSalespersonProblem, ExhaustiveTSPSolver, TSP2OptNeighborStrategy


class MetricTSProblemTest(unittest.TestCase):
    def test_accessors(self):
        points = [(1,0), (0,1), (0,0), (1,1)]
        p = TravellingSalespersonProblem(points)
        self.assertEqual(p.get_points(), points)

    def test_solution_evaluation(self):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        p = TravellingSalespersonProblem(points)
        self.assertEqual(p.evaluate_solution([0, 1, 2, 3]), 4)
        self.assertEqual(p.evaluate_solution([0, 2, 1, 3]), 2 + 2*math.sqrt(2))

class AbstractTSPSolverTest(unittest.TestCase):
    def _assert_cyclic_equals(self, l1, l2):
        l1_canonical = self._get_canonical_cyclic_form(l1)
        l2_canonical = self._get_canonical_cyclic_form(l2)
        self.assertEqual(l1_canonical, l2_canonical)

    def _get_canonical_cyclic_form(self, l):
        edges = [(p1, p2) for p1, p2 in zip(l[:-1], l[1:])] + [(l[-1], l[0])]
        return sorted([sorted(e) for e in edges])

class ExhaustiveTSPSolverTest(AbstractTSPSolverTest):
    def test_square(self):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        p = TravellingSalespersonProblem(points)
        solution = ExhaustiveTSPSolver(p).solve()
        self._assert_cyclic_equals(solution, [0, 1, 2, 3])

class SimulatedAnnealingTSPSolverTest(AbstractTSPSolverTest):
    def test_square(self):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        p = TravellingSalespersonProblem(points)
        solution = SimulatedAnnealingSolver(p, TSP2OptNeighborStrategy()).solve([0, 1, 2, 3], 100, 10)
        self._assert_cyclic_equals(solution, [0, 1, 2, 3])

class HillClimbingTSPSolverTest(AbstractTSPSolverTest):
    def test_square(self):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        p = TravellingSalespersonProblem(points)
        solution = HillClimbingSolver(p, TSP2OptNeighborStrategy()).solve([0, 2, 1, 3], 100)
        self._assert_cyclic_equals(solution, [0, 1, 2, 3])
