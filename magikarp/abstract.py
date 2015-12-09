class AbstractSolver(object):
    def __init__(self, problem):
        """
        The problem instance is part of the solver's immutable state.
        The solver should allow for as little mutable state as possible.
        """
        self.problem = problem

    def solve(self, *args, **kwargs):
        raise NotImplementedError

class AbstractExhaustiveSolver(AbstractSolver):
    def solve(self):
        potential_solutions = self._get_potential_solutions()
        best = self._get_best_solution(potential_solutions)
        return best

    def _get_potential_solutions(self):
        raise NotImplementedError

    def _get_best_solution(self, potential_solutions):
        best_solution_value = self._get_worst_possible_solution_value()
        best_solution = None
        for sol in potential_solutions:
            candidate_solution_value = self.problem.evaluate_solution(sol)
            if self.problem.better_score(candidate_solution_value, best_solution_value):
                best_solution_value = candidate_solution_value
                best_solution = sol
        return best_solution

    def _get_worst_possible_solution_value(self):
        raise NotImplementedError

    def _candidate_solution_is_better(self, candidate_solution_value, best_solution_value):
        raise NotImplementedError

class AbstractProblem(object):
    def evaluate_solution(self, solution):
        raise NotImplementedError

    def better(self, sol1, sol2):
        "Return True if the first solution is better than (or equal to) the second."
        return self.better_score(self.evaluate_solution(sol1),
                                 self.evaluate_solution(sol2))

    def better_score(self, score1, score2):
        "Return True if the first score is better than (or equal to) the second."
        raise NotImplementedError