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
    '''Enter dots (list of tuples with len < 10) to calculate all permutations and find that with best distance'''
    dots_tuples = [(5, 0), (5, 2), (5, 4), (5, 1), (0, 2), (4, 3)]
    dots = [Dot(i) for i in dots_tuples]
    find_best_path(dots)

if __name__ == '__main__':
    main()