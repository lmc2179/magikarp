import inspect

from magikarp import tsp, knapsack, partition
from magikarp.abstract import AbstractSolver, AbstractProblem


def generate_documentation(target_module):
    print('Generating documentation for {0}...'.format(target_module))
    for name, obj in inspect.getmembers(target_module):
        if inspect.isclass(obj):
            if issubclass(obj, AbstractSolver):
                print('Got Solver class {0}'.format(obj))
            if issubclass(obj, AbstractProblem):
                print('Got Problem class {0}'.format(obj))


if __name__ == '__main__':
    target_modules = [tsp,
                      knapsack,
                      partition]
    for module_name in target_modules:
        generate_documentation(module_name)