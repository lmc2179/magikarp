import inspect

from magikarp import tsp, knapsack, partition
from magikarp.abstract import AbstractSolver, AbstractProblem

class DocumentationPage(object):
    def __init__(self, module_name):
        self.module_name = module_name
        self.solver_classes = []
        self.problem_class = None
        self.validation_function = None
        self.solver_functions = []

    def set_problem_class(self, cls):
        if self.problem_class:
            raise Exception('Found multiple problem classes in {0}'.format(self.module_name))
        self.problem_class = cls

    def add_solver_class(self, cls):
        self.solver_classes.append(cls)

    def set_validation_function(self, fxn):
        if self.validation_function:
            raise Exception('Found multiple validation functions in {0}'.format(self.module_name))
        self.validation_function = fxn

    def add_solver_function(self, fxn):
        self.solver_functions.append(fxn)

    def write_markdown(self):
        markdown_sections = []
        markdown_sections.append(self.write_overview())
        markdown_sections.append(self.write_problem_function_section())
        markdown_sections += self.write_solver_function_sections()
        markdown_sections.append(self.write_class_overview_section())
        markdown_sections.append(self.write_problem_class_section())
        markdown_sections += self.write_solver_class_sections()



def generate_documentation(target_module):
    print('Generating documentation for {0}...'.format(target_module))
    doc_page = DocumentationPage(target_modules)
    for name, obj in inspect.getmembers(target_module):
        if inspect.isclass(obj):
            if issubclass(obj, AbstractSolver):
                print('Got Solver class {0}'.format(obj))
                doc_page.add_solver_class(obj)
            if issubclass(obj, AbstractProblem):
                print('Got Problem class {0}'.format(obj))
                doc_page.set_problem_class(obj)
            if inspect.isfunction(obj):
                if obj.__name__.startswith('validate_'):
                    doc_page.set_validation_function(obj)
                    print('Got validation function {0}'.format(obj))
                elif obj.__name__.startswith('solve_'):
                    doc_page.add_solver_function(obj)
                    print('Got facade function {0}'.format(obj))
    doc_page.write_markdown()



if __name__ == '__main__':
    target_modules = [tsp,
                      knapsack,
                      partition]
    for module_name in target_modules:
        generate_documentation(module_name)