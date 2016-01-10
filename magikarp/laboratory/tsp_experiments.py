import datetime
import json
import os
import random

from tqdm import tqdm

from magikarp.tsp import solve_tsp_simulated_annealing, solve_tsp_hill_climbing

DATA_ROOT = 'C:\\Users\\louis\\Desktop\\Data\\magikarp'

def generate_cities(n, x_upper=1.0, x_lower=0.0, y_upper=1.0, y_lower=0.0):
    x_size = x_upper - x_lower
    y_size = y_upper - y_lower
    return [(random.random()*x_size + x_lower, random.random()*y_size + y_lower) for i in range(n)]

def generate_cc_data(no_trials, no_cities, lower_bound, upper_bound, sa_iterations):
    random_cities = generate_cities(25)
    initial_config = list(range(len(random_cities)))
    results = []
    T_RANGE = upper_bound - lower_bound

    baseline_solution, baseline_cost = None, float('inf')

    for i in tqdm(range(no_trials)):
        random.shuffle(initial_config)
        t = random.random()*T_RANGE + lower_bound
        solution,cost = solve_tsp_simulated_annealing(random_cities, initial_config, sa_iterations, t, '2-opt')
        results.append((t, cost))
        _, new_baseline_cost = solve_tsp_hill_climbing(random_cities, initial_config, sa_iterations, '2-opt')
        baseline_cost = min(new_baseline_cost, baseline_cost)

    print('Baseline cost: ', baseline_cost)
    temps, costs = zip(*results)
    return temps, costs, baseline_cost

def write_cc_results(cooling_constants, costs, baseline_cost, filename):
    f = open(filename, 'a')
    data = {'cooling_const': cooling_constants, 'sa_costs':costs, 'baseline_cost': baseline_cost}
    json_data = json.dumps(data)
    f.write(json_data)
    f.write(',\n')
    f.close()

LOWER, UPPER = 0.0, 2.0
NO_CITIES = 25
SA_ITERATIONS = 30000
NO_TRIALS = 200
NO_SOLUTIONS = 200
timestamp = datetime.datetime.now().strftime('%a-%H-%M')
filename_stem = 'cooling_constant_test_{0}.json'.format(timestamp)
filename = os.path.join(DATA_ROOT, filename_stem)
f = open(filename, 'w')
f.write('[')
f.close()

for city in range(NO_TRIALS):
    print(city+1, '/', NO_TRIALS)
    cooling_constants, costs, baseline_cost = generate_cc_data(NO_SOLUTIONS, NO_CITIES, LOWER, UPPER, SA_ITERATIONS)
    write_cc_results(cooling_constants, costs, baseline_cost, filename)

    # plt.plot([LOWER, UPPER], [baseline_cost, baseline_cost], color='r')
    # plt.plot(cooling_constants, costs, marker='o', linewidth=0.0)
    # plt.show()

f = open(filename, 'a')
param_data = {'lower_bound': LOWER, 'upper_bound': UPPER, 'sa_iterations': SA_ITERATIONS, 'no_cities':NO_CITIES}
f.write(json.dumps(param_data))
f.write(']')
f.close()