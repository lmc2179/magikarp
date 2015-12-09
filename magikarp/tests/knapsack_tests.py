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
        solution = knapsack.ExhaustiveKnapsackSolver(p).solve()
        self.assertEqual({0, 2}, set(solution))

class GreedyKnapsackTest(unittest.TestCase):
    def test_optimal_solution_evalution(self):
        p = knapsack.KnapsackProblem(weights=[1,2,4],
                                     values=[2, 4, 8],
                                     limit=5)
        solution = knapsack.GreedyKnapsackSolver(p).solve()
        self.assertEqual({0, 2}, set(solution))

    def test_suboptimal_solution_evalution(self):
        p = knapsack.KnapsackProblem(weights=[2,3,5],
                                     values=[2, 3, 5],
                                     limit=5)
        solution = knapsack.GreedyKnapsackSolver(p).solve()
        self.assertEqual({2}, set(solution))

if __name__ == '__main__':
    unittest.main()