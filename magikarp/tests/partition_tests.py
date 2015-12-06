import unittest
from magikarp import partition

class PartitionProblemTest(unittest.TestCase):
    def test_solution_evaluation(self):
        p = partition.PartitionProblem([1, -1, 2])
        self.assertEqual(p.evaluate_solution(((0, 1), (2,))), 2)
        self.assertEqual(p.evaluate_solution(((0,), (2, 1))), 0)
        self.assertEqual(p.evaluate_solution(((1,), (2,0))), 4)

if __name__ == '__main__':
    unittest.main()