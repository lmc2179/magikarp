import random

from matplotlib import pyplot as plt

from magikarp import tsp, point_search

NUM_CITIES = 15
city_x = [random.random() for _ in range(NUM_CITIES)]
city_y = [random.random() for _ in range(NUM_CITIES)]
city_tuples = list(zip(city_x, city_y))

p = tsp.TravellingSalespersonProblem(city_tuples)
sa_tour = point_search.SimulatedAnnealingSolver(p, tsp.TSP2OptNeighborStrategy()).solve(list(range(0, NUM_CITIES)), 100000, 50.0) + [0]
print(sa_tour)
sa_tour_x, sa_tour_y = [city_x[i] for i in sa_tour], [city_y[i] for i in sa_tour]

plt.plot(city_x, city_y, marker='o', linewidth=0.0)
plt.plot(sa_tour_x, sa_tour_y, color='r')
plt.show()