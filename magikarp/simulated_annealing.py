import math
import random

from magikarp.abstract import AbstractSolver, MinMaxEnum


class AbstractSimulatedAnnealingSolver(AbstractSolver):
    def __init__(self, problem):
        super(AbstractSimulatedAnnealingSolver, self).__init__(problem)
        self.EVALUATION_COEFF = self._get_evaluation_coeff()

    def _get_evaluation_coeff(self):
        MIN_MAX_TYPE = self.problem.MIN_MAX_TYPE
        if MIN_MAX_TYPE == MinMaxEnum.MIN:
            return 1.0 # No adjustment needed here, this is already a minimization problem
        elif MIN_MAX_TYPE == MinMaxEnum.MAX:
            return -1.0
        raise Exception('Unrecognized MIN_MAX_TYPE for class {0}: {1}'.format(self.problem.__class__,
                                                                              self.problem.MIN_MAX_TYPE))

    def solve(self, initial_point, no_iterations, cooling_constant):
        best_score = float('inf')
        best_point = None
        current_point = initial_point
        for i in range(no_iterations): #TODO: Uncle bob this
            temp = self._get_temperature(i, cooling_constant)
            candidate_point = self._get_neighbor(current_point)
            acceptance_prob = self._get_acceptance_likelihood(current_point, candidate_point, temp)
            if acceptance_prob > random.random():
                current_point = candidate_point
                current_score = self._evaluate_point(current_point)
                if current_score < best_score:
                    best_score = current_score
                    best_point = current_point
        return best_point

    def _get_temperature(self, iteration, cooling_constant):
        if iteration == 0:
            return cooling_constant
        return cooling_constant / math.log(iteration+1)

    def _get_neighbor(self, current_point):
        raise NotImplementedError

    def _get_acceptance_likelihood(self, current_point, candidate_point, temp):
        current_value = self._evaluate_point(current_point)
        candidate_value = self._evaluate_point(candidate_point)
        if candidate_value < current_value:
            return 1.0
        else:
            return math.exp(-(candidate_value - current_value) / temp)

    def _evaluate_point(self, p):
        return self.EVALUATION_COEFF * self.problem.evaluate_solution(p)