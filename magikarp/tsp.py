import math

class TravellingSalespersonProblem(object):
    def __init__(self, points):
        self.points = points

    def get_points(self):
        return self.points

    def _distance(self, p1, p2):
        return math.sqrt(sum([(x1-x2)**2 for x1, x2 in zip(p1, p2)]))

    def evaluate_solution(self, path_indices):
        # TODO oh my god this is a disaster
        return sum([self._distance(self.points[p_i], self.points[p_i_next])
                    for p_i, p_i_next in zip(path_indices[:-1], path_indices[1:])]) + self._distance(self.points[path_indices[-1]],
                                                                                                     self.points[path_indices[0]])