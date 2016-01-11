import math
import random

import numpy as np

from magikarp.abstract import AbstractSolver, MinMaxEnum


class PointSearchSolver(AbstractSolver):
    # Contains logic for using the MIN_MAX_TYPE to frame problems as a function minimization over some search space.
    # This will probably get renamed or moved higher up the chain when I write subset search methods.
    def __init__(self, problem, neighbor_strategy):
        super(PointSearchSolver, self).__init__(problem)
        self.EVALUATION_COEFF = self._get_evaluation_coeff()
        self.strategy = neighbor_strategy

    def _get_evaluation_coeff(self):
        MIN_MAX_TYPE = self.problem.MIN_MAX_TYPE
        if MIN_MAX_TYPE == MinMaxEnum.MIN:
            return 1.0 # No adjustment needed here, this is already a minimization problem
        elif MIN_MAX_TYPE == MinMaxEnum.MAX:
            return -1.0
        raise Exception('Unrecognized MIN_MAX_TYPE for class {0}: {1}'.format(self.problem.__class__,
                                                                              self.problem.MIN_MAX_TYPE))
    def _evaluate_point(self, p):
        return self.EVALUATION_COEFF * self.problem.evaluate_solution(p)

class SimulatedAnnealingSolver(PointSearchSolver):
    def solve(self, initial_point, no_iterations, cooling_constant):
        best_score = float('inf')
        best_point = None
        current_point = initial_point
        temp = cooling_constant
        for i in range(no_iterations): #TODO: Uncle bob this
            candidate_point = self.strategy.get_neighbor(current_point)
            acceptance_prob = self._get_acceptance_likelihood(current_point, candidate_point, temp)
            if acceptance_prob > random.random():
                current_point = candidate_point
                current_score = self._evaluate_point(current_point)
                if current_score < best_score:
                    best_score = current_score
                    best_point = current_point
            temp = self._get_temperature(i, cooling_constant, candidate_point, current_point)
        return best_point

    def _get_temperature(self, iteration, cooling_constant, candidate_point, current_point):
        return cooling_constant / math.log(iteration+2)

    def _get_acceptance_likelihood(self, current_point, candidate_point, temp):
        current_value = self._evaluate_point(current_point)
        candidate_value = self._evaluate_point(candidate_point)
        if candidate_value < current_value:
            return 1.0
        else:
            return math.exp(-(candidate_value - current_value) / temp)

class AbstractNeighborStrategy(object):
    def get_neighbors(self, current_point):
        raise NotImplementedError

    def get_neighbor(self, current_point):
        raise NotImplementedError

class HillClimbingSolver(PointSearchSolver):
    def solve(self, initial_point, no_iterations):
        current_score = self._evaluate_point(initial_point)
        current_point = initial_point
        for i in range(no_iterations): #TODO: Uncle bob this too
            neighbors = self.strategy.get_neighbors(current_point)
            scores = [self._evaluate_point(n) for n in neighbors]
            best_score_index = np.argmin(scores)
            if scores[best_score_index] > current_score:
                return neighbors[best_score_index]
            else:
                current_point = neighbors[best_score_index]
                current_score = scores[best_score_index]
        return current_point