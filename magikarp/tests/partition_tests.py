import unittest
from magikarp import partition

class PartitionProblemTest(unittest.TestCase):
    def test_solution_evaluation(self):
        p = partition.PartitionProblem([1, -1, 2])
        self.assertEqual(p.evaluate_solution(((0, 1), (2,))), 2)
        self.assertEqual(p.evaluate_solution(((0,), (2, 1))), 0)
        self.assertEqual(p.evaluate_solution(((1,), (2,0))), 4)

class ExhaustiveSolverTest(unittest.TestCase):
    def test_optimal_solution(self):
        p = partition.PartitionProblem([1, -1, 2])
        sol = partition.ExhaustivePartitionSolver().solve(p)
        p1, p2 = sol
        self.assertNotEqual(p1, p2)
        best_partitioning = [{0}, {1, 2}]
        assert set(p1) in best_partitioning
        assert set(p2) in best_partitioning

if __name__ == '__main__':
    unittest.main()