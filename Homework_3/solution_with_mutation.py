import random
from copy import deepcopy
from math import factorial

from dot import Dot
from route import Route
from constants import (MAX_N, MAX_N_TO_BE_OPTIMISED, 
                       SEQUENTIVE_EQUAL_DISTANCE_OCCURANCES_FOR_EXTREMUM_REACHED, TIMES_OF_EXECUTION_OF_ALGORITHM,
                       TENTH_STEP_OF_EXECUTION_COUNT, HUNDRED_STEP_OF_EXECUTION_COUNT,
                       TWO_HUNDRED_STEP_OF_EXECUTION_COUNT, THREE_HUNDRED_STEP_OF_EXECUTION_COUNT)

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

    print([i.coordinates for i in generated_dots])
    return generated_dots

def read_input_parameters():
    n = int(input('Enter number of cities to be travelled: '))

    assert n <= MAX_N, 'Number of cities must be <= 100!'    
    return n

def generate_initial_route(n):
    dots = generate_n_different_random_dots(n)
    #uncomment for shizwing initial dots when using solver
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
    '''The function creates 2 children from 2 parents
        parameters:   parent_1, parent_2, n
        return value: [<Route>] of children '''

    number_of_sequentive_genes_from_parent_for_reproduction = int(n / 2) if n % 2 == 0 else int(n / 2) + 1
    first_part_of_parent_1 = parent_1.dots[:number_of_sequentive_genes_from_parent_for_reproduction]
    first_part_of_parent_2 = parent_2.dots[:number_of_sequentive_genes_from_parent_for_reproduction]
    # print(first_part_of_parent_1)

    child_1 = geenrate_child(first_part_of_parent_1, parent_2, number_of_sequentive_genes_from_parent_for_reproduction)
    child_2 = geenrate_child(first_part_of_parent_2, parent_1, number_of_sequentive_genes_from_parent_for_reproduction)

    return child_1, child_2

def mutation(individual, n):
    random_gene_from_first_half_position = random.randint(0, int(n / 2))
    random_gene_from_second_half_position = random.randint(int(n / 2), n - 1)
    individual.dots[random_gene_from_first_half_position], individual.dots[random_gene_from_second_half_position] = individual.dots[random_gene_from_second_half_position], individual.dots[random_gene_from_first_half_position]

def reproduce(sample_of_individuals, number_of_individuals_in_sample, n):
    #get the first 25% from the sample for reproduction
    number_of_individuals_preserved = int(number_of_individuals_in_sample / 4 if number_of_individuals_in_sample % 2 == 0 else number_of_individuals_in_sample / 4 + 1)
    individuals_preserved_for_next_generation = sample_of_individuals[:number_of_individuals_preserved]
    
    number_of_children_needed = number_of_individuals_in_sample - number_of_individuals_preserved
    index_of_pair_of_parents = 0
    children_reproduced = []
    while number_of_children_needed > 0:
        #create 2 children from pair
        children_from_crossover = crossover(sample_of_individuals[index_of_pair_of_parents], sample_of_individuals[index_of_pair_of_parents + 1], n)

        #mutation of first child
        random_number = random.randint(1, 100)
        condition_for_mutation = random_number == 1 or random_number == 2 or random_number == 3
        if condition_for_mutation:
            mutation(children_from_crossover[0], n)

        #mutation of second child
        random_number = random.randint(1, 100)
        condition_for_mutation = random_number == 1 or random_number == 2 or random_number == 3
        if condition_for_mutation:
            mutation(children_from_crossover[1], n)

        children_reproduced.append(children_from_crossover[0])
        children_reproduced.append(children_from_crossover[1])
        
        #increase with 2 because for crossover 2 parents are needed
        index_of_pair_of_parents += 2

        #decrease with 2 because 2 children are reproduced from crossover
        number_of_children_needed -= 2

    next_generation_individuals = []
    for i in individuals_preserved_for_next_generation:
        next_generation_individuals.append(i)

    for i in children_reproduced:
        next_generation_individuals.append(i)

    return next_generation_individuals

def find_best_individual(sample_of_individuals, number_of_individuals_in_sample, n):
    best_individual = sample_of_individuals[0]
    best_distance = best_individual.distance

    optimisation_condition = False

    #uncomment if you want to NOT use genetic algorithm for n <= 8
    #optimisation_condition = n <= MAX_N_TO_BE_OPTIMISED

    if optimisation_condition:
        pass
    else:
        #works best with 10
        number_of_sequentive_times_with_equal_best_distance_for_extremum_reached = SEQUENTIVE_EQUAL_DISTANCE_OCCURANCES_FOR_EXTREMUM_REACHED
        current_number_of_sequentive_times_with_equal_best_distance = 0
        count_for_execution_of_algorithm = TIMES_OF_EXECUTION_OF_ALGORITHM
        is_best_result_achieved = False
        while not is_best_result_achieved:
            next_generation = reproduce(sample_of_individuals, number_of_individuals_in_sample, n)
            next_generation.sort(key=lambda x: x.distance)
            next_generation_best_individual = next_generation[0]
            next_generation_best_distance = next_generation_best_individual.distance

            if next_generation_best_distance == best_distance:
                current_number_of_sequentive_times_with_equal_best_distance += 1
            else:
                current_number_of_sequentive_times_with_equal_best_distance = 0

            sample_of_individuals = next_generation
            if next_generation_best_distance < best_distance:
                best_individual = next_generation_best_individual
                best_distance = next_generation_best_distance
            
            count_for_execution_of_algorithm -= 1
            is_best_result_achieved = (current_number_of_sequentive_times_with_equal_best_distance == number_of_sequentive_times_with_equal_best_distance_for_extremum_reached)\
                              or count_for_execution_of_algorithm == 0
            #uncomment for showing best distance for each generation
            # print('#' + str(1000 - count_for_execution_of_algorithm) + ' ' + str(best_distance))

            #step 10
            if count_for_execution_of_algorithm == TENTH_STEP_OF_EXECUTION_COUNT:
                print('Step 10: ', best_distance)
            #step 20
            elif count_for_execution_of_algorithm == HUNDRED_STEP_OF_EXECUTION_COUNT:
                print('Step 100: ', best_distance)
            #step 30
            elif count_for_execution_of_algorithm == TWO_HUNDRED_STEP_OF_EXECUTION_COUNT:
                print('Step 200: ', best_distance)
            #step 40
            elif count_for_execution_of_algorithm == THREE_HUNDRED_STEP_OF_EXECUTION_COUNT:
                print('Step 300: ', best_distance)

    return best_individual
    
def main():
    condition_for_tests = False
    if condition_for_tests:
        '''tes with 4'''
        # n = 4
        # initial_route = Route([Dot(i) for i in [(3, 2), (2, 0), (2, 3), (1, 1)]])

        '''tes with 5'''
        n = 5
        initial_route = Route([Dot(i) for i in [(4, 0), (1, 2), (2, 2), (0, 2), (0, 3)]])
    else:
        n = read_input_parameters()

        initial_route = generate_initial_route(n)


    #formula calculating how many individuals to be in sample
    number_of_individuals_in_sample = 100
    # if n > 50:
    #     number_of_individuals_in_sample = int(pow(n, 2) / 8)

    # elif n > 70:
    #     number_of_individuals_in_sample = n * 5

    #create diverse sample
    sample_of_individuals = create_diverse_sample_from_random_individuals(number_of_individuals_in_sample, initial_route)

    #sort the sample
    sample_of_individuals.sort(key=lambda x: x.distance)

    #execute algorithm
    best_individual = find_best_individual(sample_of_individuals, number_of_individuals_in_sample, n)

    #Output
    print('Best distance', best_individual.distance)
    print([str(i) for i in best_individual.dots])


if __name__ == '__main__':
    main()