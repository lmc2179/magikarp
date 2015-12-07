from magikarp import simulated_annealing
import unittest

class SimulatedAnnealingTest(unittest.TestCase):
    def test_array_search(self):
        sa = simulated_annealing.ArraySearchSimulatedAnnealing(1.0, [0, 1, 0, -1,0, 1, -2, 0])
        solution = sa.get_approximate_solution(0, 20)