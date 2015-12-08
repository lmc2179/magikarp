import math
import random


class AbstractSimulatedAnnealing(object):
    def __init__(self, cooling_constant):
        self.cooling_constant = cooling_constant

    def get_approximate_solution(self, initial_point, no_iterations):
        best_score = float('inf')
        best_point = None
        current_point = initial_point
        for i in range(no_iterations):
            temp = self._get_temperature(i)
            candidate_point = self._get_neighbor(current_point)
            acceptance_prob = self._get_acceptance_likelihood(current_point, candidate_point, temp)
            if acceptance_prob > random.random():
                current_point = candidate_point
                current_score = self._evaluate_point(current_point)
                if current_score < best_score:
                    best_score = current_score
                    best_point = current_point
        return best_point

    def _get_temperature(self, iteration):
        if iteration + 1 == 1:
            return self.cooling_constant
        return self.cooling_constant / math.log(iteration+1)

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
        raise NotImplementedError # This is the function to minimize