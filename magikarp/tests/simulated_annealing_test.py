import random

from magikarp import simulated_annealing
import unittest

from magikarp.simulated_annealing import AbstractSimulatedAnnealing


class SimulatedAnnealingTest(unittest.TestCase):
    def test_array_search(self):
        sa = magikarp.tests.simulated_annealing_test.ArraySearchSimulatedAnnealing(1.0, [0, 1, 0, -1, 0, 1, -2, 0])
        solution = sa.get_approximate_solution(0, 20)
        self.assertEqual(solution, 6)


class ArraySearchSimulatedAnnealing(AbstractSimulatedAnnealing):
    """This is a simple subclass use to test the abstract implementation above. It
    performs a search through a very large array for a minimum value."""
    def __init__(self, cooling_constant, target_array):
        super(ArraySearchSimulatedAnnealing, self).__init__(cooling_constant=cooling_constant)
        self.target_array = target_array

    def _get_neighbor(self, current_point):
        if random.random() > 0.5:
            offset = 1
        else:
            offset = -1
        return (current_point + offset) % len(self.target_array)

    def _evaluate_point(self, p):
        return self.target_array[p]