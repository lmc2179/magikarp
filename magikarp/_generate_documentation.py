from magikarp import tsp, knapsack, partition

def generate_documentation(target_module):
    print('Generating documentation for {0}...'.format(target_module))

if __name__ == '__main__':
    target_modules = [tsp,
                      knapsack,
                      partition]
    for module_name in target_modules:
        generate_documentation(module_name)