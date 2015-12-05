import unittest
from magikarp import knapsack

class KnapsackProblemTest(unittest.TestCase):
    def test_solution_evalution(self):
        p = knapsack.KnapsackProblem(weights=[1,2,4],
                                     values=[2, 4, 8],
                                     limit=5)
        self.assertEqual(p.evaluate_solution([0,1,2]), 0)
        self.assertEqual(p.evaluate_solution([1,2]), 0)
        self.assertEqual(p.evaluate_solution([0,2]), 10)
        self.assertEqual(p.evaluate_solution([0,1]), 6)

class ExhaustiveKnapsackTest(unittest.TestCase):
    def test_solution_evalution(self):
        p = knapsack.KnapsackProblem(weights=[1,2,4],
                                     values=[2, 4, 8],
                                     limit=5)
        solution = knapsack.ExhaustiveKnapsackSolver().solve(p)
        self.assertEqual({0, 2}, set(solution))

if __name__ == '__main__':
    unittest.main()