import unittest

from magikarp import minimal_coloring


class MinimalColoringProblemTest(unittest.TestCase):
    def test_neighbors(self):
        #   A---B
        #   | \ |
        #   C---D
        graph_data = [('A', 'B'), ('A', 'D'), ('A', 'C'), ('C', 'D'), ('B', 'D')]
        p = minimal_coloring.MinimalColoringProblem(graph_data)
        self.assertEqual(set(p.get_neighbors('A')), {'B', 'C', 'D'})
        self.assertEqual(set(p.get_neighbors('B')), {'A', 'D'})
        self.assertEqual(set(p.get_neighbors('C')), {'A', 'D'})
        self.assertEqual(set(p.get_neighbors('D')), {'B', 'C', 'A'})

    def test_solution_evaluation(self):
        #   A---B
        #   | \ |
        #   C---D
        graph_data = [('A', 'B'), ('A', 'D'), ('A', 'C'), ('C', 'D'), ('B', 'D')]
        p = minimal_coloring.MinimalColoringProblem(graph_data)
        self.assertEqual(p.evaluate_solution([('A', 0), ('B', 1), ('C', 1), ('D', 2)]), 3)
        self.assertEqual(p.evaluate_solution([('A', 2), ('B', 1), ('C', 1), ('D', 0)]), 3)
        self.assertEqual(p.evaluate_solution([('A', 0), ('B', 1), ('C', 3), ('D', 2)]), 4)
        self.assertEqual(p.evaluate_solution([('A', 0), ('B', 0), ('C', 0), ('D', 0)]), float('inf'))