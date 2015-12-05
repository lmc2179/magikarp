class AbstractExhaustiveSolver(object):
    def solve(self, problem):
        potential_solutions = self._get_potential_solutions(problem)
        best = self._get_best_solution(potential_solutions, problem)
        return best

    def _get_potential_solutions(self, problem):
        raise NotImplementedError

    def _get_best_solution(self, potential_solutions, problem):
        best_solution_value = self._get_worst_possible_solution_value()
        best_solution = None
        for sol in potential_solutions:
            candidate_solution_value = problem.evaluate_solution(sol)
            if self._candidate_solution_is_better(candidate_solution_value, best_solution_value):
                best_solution_value = candidate_solution_value
                best_solution = sol
        return best_solution

    def _get_worst_possible_solution_value(self):
        raise NotImplementedError

    def _candidate_solution_is_better(self, candidate_solution_value, best_solution_value):
        raise NotImplementedError