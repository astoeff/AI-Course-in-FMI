import random
from math import factorial
import itertools
from route import Route
from dot import Dot
def find_best_path(dots):
    permutations = itertools.permutations(dots)
    routes = []
    for i in permutations:
        routes.append(Route(i))

    routes_sorted = sorted(routes)
    print(routes_sorted[0].distance, '---->', [i.coordinates for i in routes_sorted[0].dots])



def main():
    dots_tuples = [(0, 4), (1, 3), (3, 1), (4, 3), (5, 3), (6, 3), (6, 2), (7, 0)]
    dots = [Dot(i) for i in dots_tuples]
    # dots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    find_best_path(dots)

if __name__ == '__main__':
    main()