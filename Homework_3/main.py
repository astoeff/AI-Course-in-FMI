import random
import itertools
from copy import deepcopy
from math import factorial

from dot import Dot
from route import Route

def generate_n_different_random_dots(n):
    already_existing_dots_dict = {}
    generated_dots = []
    count = 0
    while count < n:
        dot = (random.randint(0, n - 1), random.randint(0, n - 1))
        try:
            already_existing_dots_dict[dot]
        except KeyError as e:
            count += 1
            already_existing_dots_dict[dot] = True
            generated_dots.append(Dot(dot))
        else:
            #Do not do anything, the dot is already generated
            pass

    return generated_dots

def main():
    n = int(input('Enter number of cities to be travelled: '))

    assert n <= 100, 'Number of cities must be <= 100!'
    
    dots = generate_n_different_random_dots(n)
    initial_route = Route(dots)

    number_of_individuals_in_sample = pow(n, 2) if n > 10 else factorial(n)

    sample_of_individuals = []

    for i in range(number_of_individuals_in_sample):
        dots = deepcopy(initial_route.dots)
        random.shuffle(dots)
        sample_of_individuals.append(Route(dots))

    #sort the sample
    sample_of_individuals.sort(key=lambda x: x.distance)

    if n <= 8:
        print([i.coordinates for i in sample_of_individuals[0].dots])
        print(sample_of_individuals[0].distance)

    else:

        #get the first 25% from the sample for reproduction
        number_of_individuals_preserved = int(n/4 if n % 2 == 0 else n/4 + 1)
        individuals_preserved_for_next_generation = sample_of_individuals[:number_of_individuals_preserved]
        
        number_of_children_needed = n - number_of_individuals_preserved
        number_of_pair_of_parents = 0
        while number_of_children_needed > 0:
            #create child from pair
            pass


        count_for_exctremum_reached = 5
        count_for_execution_of_algorithm = 1000
        # for i in sample_of_individuals:
        #     i.print_dots()
        #     print(i.distance)


    # permutations = itertools.permutations(dots)
    # r1 = Route((next(permutations)))
    # r2 = Route(next(permutations))
    # r3 = Route(next(permutations))
    # r4 = Route(next(permutations))

    # print('Route 1 ----------------------')
    # r1.print_dots()
    # print('Route 2 ----------------------')
    # r2.print_dots()
    # print('Route 3 ----------------------')
    # r3.print_dots()
    # print('Route 4 ----------------------')
    # r4.print_dots()



if __name__ == '__main__':
    main()