from magikarp.abstract import AbstractProblem

class PartitionProblem(AbstractProblem):
    "Represents an instance of the partition difference optimization problem."
    def __init__(self, array):
        self.array = array

    def evaluate_solution(self, solution):
        p1_indices, p2_indices = solution
        p1_sum = sum([self.array[i] for i in p1_indices])
        p2_sum = sum([self.array[i] for i in p2_indices])
        return abs(p1_sum - p2_sum)