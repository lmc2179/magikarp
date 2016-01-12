import random

from matplotlib import pyplot as plt

from magikarp import tsp, point_search

def draw_tour(tour, city_x, city_y, color, fig_no):
    plt.figure(fig_no)
    plt.plot(city_x, city_y, marker='o', linewidth=0.0)
    tour_x, tour_y = [city_x[i] for i in tour], [city_y[i] for i in tour]
    plt.plot(tour_x, tour_y, color=color)

NUM_CITIES = 100
city_x = [random.random() for _ in range(NUM_CITIES)]
city_y = [random.random() for _ in range(NUM_CITIES)]
city_tuples = list(zip(city_x, city_y))

p = tsp.TravellingSalespersonProblem(city_tuples)

solver = point_search.SimulatedAnnealingSolver(p, tsp.TSP2OptNeighborStrategy())
sa_tour = solver.solve(list(range(0, NUM_CITIES)), 30000, 150.0, 0.999)
plt.plot(solver.score_trace)
plt.show()
print("SA Tour: ", p.evaluate_solution(sa_tour))
draw_tour(sa_tour + [0], city_x, city_y, 'r', 0)

hc_tour = point_search.HillClimbingSolver(p, tsp.TSP2OptNeighborStrategy()).solve(list(range(0, NUM_CITIES)), 300000)
print("HC Tour: ", p.evaluate_solution(hc_tour))
draw_tour(hc_tour + [0], city_x, city_y, 'g', 1)

plt.show()