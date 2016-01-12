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
        sol = partition.solve_partition_exhaustive([1, -1, 2])
        p1, p2 = sol
        self.assertNotEqual(p1, p2)
        best_partitioning = [{0}, {1, 2}]
        assert set(p1) in best_partitioning
        assert set(p2) in best_partitioning

class SimulatedAnnealingSolverTest(unittest.TestCase):
    def test_optimal_solution(self):
        sol = partition.solve_tsp_simulated_annealing([1, -1, 2], 100, 5.0)
        p1, p2 = sol
        self.assertNotEqual(p1, p2)
        best_partitioning = [{0}, {1, 2}]
        assert set(p1) in best_partitioning
        assert set(p2) in best_partitioning

class GreedySolverTest(unittest.TestCase):
    def test_suboptimal_solution(self):
        sol = partition.solve_partition_greedy([4, 5, 6, 7, 8])
        p1, p2 = sol
        self.assertNotEqual(p1, p2)
        expected_partitioning = [{0, 1, 4}, {2, 3}]
        assert set(p1) in expected_partitioning
        assert set(p2) in expected_partitioning

    def test_optimal_solution(self):
        sol = partition.solve_partition_greedy([1, 2, 3, 6])
        p1, p2 = sol
        self.assertNotEqual(p1, p2)
        expected_partitioning = [{0, 1, 2}, {3}]
        assert set(p1) in expected_partitioning
        assert set(p2) in expected_partitioning

if __name__ == '__main__':
    unittest.main()