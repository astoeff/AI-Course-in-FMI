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

def read_input_parameters():
    n = int(input('Enter number of cities to be travelled: '))

    assert n <= 100, 'Number of cities must be <= 100!'    
    return n

def generate_initial_route(n):
    dots = generate_n_different_random_dots(n)
    #uncomment for shiwing initial dots when using solver
    #print([dot.coordinates for dot in dots])
    
    initial_route = Route(dots)
    return initial_route

def create_diverse_sample_from_random_individuals(number_of_individuals_in_sample, initial_individual):
    sample_of_individuals = []

    for i in range(number_of_individuals_in_sample):
        dots = deepcopy(initial_individual.dots)
        random.shuffle(dots)
        sample_of_individuals.append(Route(dots))

    return sample_of_individuals

def geenrate_child(first_half_parent, second_parent, number_of_genes_from_first_half_parent):
    child = first_half_parent

    first_half_second_parent = second_parent.dots[:number_of_genes_from_first_half_parent]
    second_half_second_parent = second_parent.dots[number_of_genes_from_first_half_parent:]

    for gene in second_half_second_parent:
        if gene not in child:
            child.append(gene)

    #can be optimised
    if len(child) != len(second_parent.dots):
        for gene in first_half_second_parent:
            if gene not in child:
                child.append(gene)

    return Route([dot for dot in child])

def crossover(parent_1, parent_2, n):
    '''The function creates children from 2 parents
        parameters:   parent_1, parent_2, n
        return value: [] of children (1 or 2)'''

    number_of_sequentive_genes_from_parent_for_reproduction = int(n / 2) if n % 2 == 0 else int(n / 2) + 1
    first_part_of_parent_1 = parent_1.dots[:number_of_sequentive_genes_from_parent_for_reproduction]
    first_part_of_parent_2 = parent_2.dots[:number_of_sequentive_genes_from_parent_for_reproduction]
    # print(first_part_of_parent_1)

    child_1 = geenrate_child(first_part_of_parent_1, parent_2, number_of_sequentive_genes_from_parent_for_reproduction)
    child_2 = geenrate_child(first_part_of_parent_2, parent_1, number_of_sequentive_genes_from_parent_for_reproduction)

    return child_1, child_2

def reproduce(sample_of_individuals, n):
    #get the first 25% from the sample for reproduction
    number_of_individuals_preserved = int(n/4 if n % 2 == 0 else n/4 + 1)
    individuals_preserved_for_next_generation = sample_of_individuals[:number_of_individuals_preserved]
    
    number_of_children_needed = n - number_of_individuals_preserved
    index_of_pair_of_parents = 0
    children_reproduced = []
    while number_of_children_needed > 0:
        #create 2 children from pair
        children_from_crossover = crossover(sample_of_individuals[index_of_pair_of_parents], sample_of_individuals[index_of_pair_of_parents + 1], n)
        children_reproduced.append(children_from_crossover[0])
        children_reproduced.append(children_from_crossover[1])
        
        #increase with 2 because for crossover 2 parents are needed
        index_of_pair_of_parents += 2

        #decrease with 2 because 2 children are reproduced from crossover
        number_of_children_needed -= 2

    next_generation_individuals = []
    for i in individuals_preserved_for_next_generation:
        d = [do for do in i.dots]
        r = Route(d)
        next_generation_individuals.append(r)

    for i in children_reproduced:
        next_generation_individuals.append(i)

    return next_generation_individuals

def find_best_individual(sample_of_individuals, n):
    best_individual = sample_of_individuals[0]
    best_distance = best_individual.distance

    optimisation_condition = False

    #uncomment if you want to not use genetic algorithm for n <= 8
    #optimisation_condition = n <= 8

    if optimisation_condition:
        pass
    else:
        #works best with 10
        number_of_sequentive_times_with_equal_best_distance_for_exctremum_reached = 40
        current_number_of_sequentive_times_with_equal_best_distance = 0
        count_for_execution_of_algorithm = 1000
        is_best_result_achieved = False
        while not is_best_result_achieved:
            next_generation = reproduce(sample_of_individuals, n)
            next_generation.sort(key=lambda x: x.distance)
            next_generation_best_individual = next_generation[0]
            next_generation_best_distance = next_generation_best_individual.distance

            if next_generation_best_distance == best_distance:
                current_number_of_sequentive_times_with_equal_best_distance += 1
            else:
                current_number_of_sequentive_times_with_equal_best_distance = 0

            sample_of_individuals = next_generation
            best_individual = next_generation_best_individual
            best_distance = next_generation_best_distance
            count_for_execution_of_algorithm -= 1
            is_best_result_achieved = (current_number_of_sequentive_times_with_equal_best_distance == number_of_sequentive_times_with_equal_best_distance_for_exctremum_reached)\
                              or count_for_execution_of_algorithm == 0
            #uncomment for showing best distance for each generation
            #print(best_distance)

            #step 10
            if count_for_execution_of_algorithm == 990:
                print('Step 10: ', best_distance)
            #step 20
            elif count_for_execution_of_algorithm == 980:
                print('Step 20: ', best_distance)
            #step 30
            elif count_for_execution_of_algorithm == 970:
                print('Step 30: ', best_distance)
            #step 40
            elif count_for_execution_of_algorithm == 960:
                print('Step 40: ', best_distance)

    return best_individual
    
def main():
    n = read_input_parameters()

    initial_route = generate_initial_route(n)

    #formula calculating how many individuals to be in sample
    number_of_individuals_in_sample = pow(n, 2) if n > 8 else factorial(n)

    #create diverse sample
    sample_of_individuals = create_diverse_sample_from_random_individuals(number_of_individuals_in_sample, initial_route)

    #sort the sample
    sample_of_individuals.sort(key=lambda x: x.distance)

    #execute algorithm
    best_individual = find_best_individual(sample_of_individuals, n)

    #Output
    print('Best distance', best_individual.distance)
    print([str(i) for i in best_individual.dots])


if __name__ == '__main__':
    main()