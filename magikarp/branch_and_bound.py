from magikarp import abstract

class AbstractBranchAndBoundSolver(abstract.AbstractSolver): # This does combinatorial minimization via B+B
    def __init__(self, problem):
        super(AbstractBranchAndBoundSolver, self).__init__(problem)
        self.EVALUATION_COEFF = self._get_evaluation_coeff()

    def _get_evaluation_coeff(self):
        MIN_MAX_TYPE = self.problem.MIN_MAX_TYPE
        if MIN_MAX_TYPE == abstract.MinMaxEnum.MIN:
            return 1.0 # No adjustment needed here, this is already a minimization problem
        elif MIN_MAX_TYPE == abstract.MinMaxEnum.MAX:
            return -1.0
        raise Exception('Unrecognized MIN_MAX_TYPE for class {0}: {1}'.format(self.problem.__class__,
                                                                              self.problem.MIN_MAX_TYPE))
    def solve(self):
        initial_configuration = self._get_initial_configuration()
        best_score = self._evaluate_configuration(initial_configuration)
        best_configuration = None
        frontier = []
        frontier.append(initial_configuration)
        while frontier:
            configuration = frontier.pop()
            configuration_value = self._evaluate_configuration(configuration)
            if self._is_final_configuration(configuration):
                if configuration_value < best_score:
                    best_configuration = configuration
                    best_score = configuration_value
            else:
                if configuration_value <= best_score:
                    best_score = configuration_value
                    neighbors = self._get_next_configurations(configuration)
                    frontier += neighbors
        return best_configuration


    def _get_initial_configuration(self):
        raise NotImplementedError

    def _get_next_configurations(self, c):
        raise NotImplementedError

    def _evaluate_configuration(self, c):
        raise NotImplementedError

    def _is_final_configuration(self, c):
        pass