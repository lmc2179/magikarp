import random
import math

class AbstractSimulatedAnnealing(object):
    def __init__(self, cooling_constant):
        self.cooling_constant = cooling_constant

    def get_approximate_solution(self, initial_point, no_iterations):
        current_point = initial_point
        for i in range(no_iterations):
            temp = self._get_temperature(i)
            candidate_point = self._get_neighbor(current_point)
            acceptance_prob = self._get_acceptance_likelihood(current_point, candidate_point, temp)
            if acceptance_prob > random.random():
                current_point = candidate_point
        return current_point

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

class ArraySearchSimulatedAnnealing(AbstractSimulatedAnnealing):
    """This is a simple subclass use to test the abstract implementation above. It
    performs a search through a very large array for a minimum value."""
    def __init__(self, cooling_constant, target_array):
        super(ArraySearchSimulatedAnnealing, self).__init__(cooling_constant=cooling_constant)
        self.target_array = target_array

    def _get_neighbor(self, current_point):
        if random.random() > 0.5:
            offset = 1
        else:
            offset = -1
        return (current_point + offset) % len(self.target_array)

    def _evaluate_point(self, p):
        return self.target_array[p]