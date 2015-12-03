import unittest
from magikarp.tsp import TravellingSalespersonProblem
import math

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