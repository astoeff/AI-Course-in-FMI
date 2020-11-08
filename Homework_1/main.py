from math import sqrt
from copy import deepcopy

from puzzle_node import Puzzle_node
import time

def set_game_preconditions():
    number_of_tiles = int(input("Enter 8, 15 or 24 as for number of the square tiles:"))
    index_of_zero_in_solved_puzzle = int(input("Enter index of zero in solved puzzle (-1 is for the last index):"))
    
    print("Now enter the puzzle")

    number_of_rows = int(sqrt(number_of_tiles + 1))

    puzzle = []
    zero_position_in_input_puzzle = None
    row_count = 0
    #the puzzle is square shaped so rows = cols
    for row in range(number_of_rows):
        r = input("Enter row: ")
        row_as_list = [int(i) for i in r.split(',')]
        puzzle.append(row_as_list)
        if 0 in row_as_list:
            zero_position_in_input_puzzle = (row, row_as_list.index(0))
        row_count += 1

    return (number_of_rows, index_of_zero_in_solved_puzzle, Puzzle_node(puzzle, zero_position_in_input_puzzle))

def find_puzzle_children(puzzle):
    puzzle_children = []
    puzzle_zero_x = puzzle.zero_position[0]
    puzzle_zero_y = puzzle.zero_position[1]
    content = deepcopy(puzzle.content)

    #UP
    #otherwise if zero is first element in list with index - 1 will get the last element
    if puzzle_zero_x - 1 >= 0:
        try:
            content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x - 1][puzzle_zero_y] = content[puzzle_zero_x - 1][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y]
        except Exception as e:
            # print('UP')
            pass
        else:
            puzzle_children.append(Puzzle_node(content, (puzzle_zero_x - 1, puzzle_zero_y), puzzle.distance_from_root + 1, puzzle, movement_direction = "down"))
        finally:
            content = deepcopy(puzzle.content)

    #LEFT
    #otherwise if zero is first element in list with index - 1 will get the last element
    if puzzle_zero_y - 1 >= 0:
        try:
            content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y - 1] = content[puzzle_zero_x ][puzzle_zero_y - 1], content[puzzle_zero_x][puzzle_zero_y]
        except Exception as e:
            # print('LEFT')
            pass
        else:
            puzzle_children.append(Puzzle_node(content, (puzzle_zero_x, puzzle_zero_y - 1), puzzle.distance_from_root + 1, puzzle, movement_direction = "right"))
        finally:
            content = deepcopy(puzzle.content)

    #DOWN
    try:
        content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x + 1][puzzle_zero_y] = content[puzzle_zero_x + 1][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y]
    except Exception as e:
        # print('DOWN')
        pass
    else:
        puzzle_children.append(Puzzle_node(content, (puzzle_zero_x + 1, puzzle_zero_y), puzzle.distance_from_root + 1, puzzle, movement_direction = "up"))
    finally:
        content = deepcopy(puzzle.content)
    
    #RIGHT
    try:
        content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y + 1] = content[puzzle_zero_x][puzzle_zero_y + 1], content[puzzle_zero_x][puzzle_zero_y]
    except Exception as e:
        # print('RIGHT')
        pass
    else:
        puzzle_children.append(Puzzle_node(content, (puzzle_zero_x, puzzle_zero_y + 1), puzzle.distance_from_root + 1, puzzle, movement_direction = "left"))
    finally:
        content = deepcopy(puzzle.content)

    return puzzle_children

def iterative_deepening_a_star(root_puzzle, final_state, final_state_dict_values):
    is_solved = False
    limit = root_puzzle.calculate_heuristic(final_state_dict_values)
    # count = 0
    while not is_solved:
        # count+=1
        # if count > 10:
        #     break
        next_limit = limit + 2
        potential_limit = limit + 1
        # print("#################################### Limit: ", limit)
        stack = [root_puzzle]
        visited = [root_puzzle]
        while stack:
            current_puzzle = stack.pop()
            # print('#############')
            # current_puzzle.print_puzzle()
            # print(current_puzzle.calculate_heuristic(final_state_dict_values))
            # print('###########')
            if is_puzzle_solved(current_puzzle, final_state):
                is_solved = True
                final_state = current_puzzle
                break
            
            current_puzzle.children = find_puzzle_children(current_puzzle)
            for child in current_puzzle.children:
                if  child.calculate_heuristic(final_state_dict_values) < limit and child not in visited:
                    stack.append(child)
                    visited.append(child)
                    # break
                # if next_limit > child.heuristic and child.heuristic > limit:
                # if limit < child.heuristic:
                #     if next_limit == potential_limit:
                #         next_limit = child.heuristic + 1
                #     else:
                #         next_limit = min(next_limit, child.heuristic + 1)
        # if next_limit != potential_limit:
        #     limit = next_limit
        # else:
        #     limit = potential_limit
        limit = next_limit
    # print("-------------------------REVERSED------------------------------------------")

    father = final_state.father_node
    steps = 0
    directions = [final_state.movement_direction]
    while father:
        # print('-----------------------------')
        # father.print_puzzle()
        if father.movement_direction:
            directions.append(father.movement_direction)
        # print('-----------------------------')
        father = father.father_node
        steps += 1

    return (steps, directions)    
    

def print_puzzle_solution(steps, directions):
    print(steps)
    i = steps - 1
    while i >= 0:
        print(directions[i])
        i -= 1

# def ida_star(root_puzzle, final_state, final_state_dict_values):
#     is_solved = False
#     while not is_solved:
#         is_solved = alg(root_puzzle, final_state, final_state_dict_values, limit)

# def alg():
#     pass

def is_puzzle_solvable(puzzle):
    return True

def create_final_state_of_puzzle_from_given_size_and_zero_position(size, zero_position):
    list_of_sequentive_numbers = []
    if zero_position == -1:
        list_of_sequentive_numbers = list(range(1, size * size))
        list_of_sequentive_numbers.append(0)
    else:
        list_of_sequentive_numbers = list(range(1, zero_position + 1))
        list_of_sequentive_numbers.append(0)
        for i in range(zero_position + 1, size * size +1):
            list_of_sequentive_numbers.append(i)
    final_state_of_puzzle = [[i for i in list_of_sequentive_numbers[0 + size * j:size + size * j]] for j in range(0, size)]
    return final_state_of_puzzle

def is_puzzle_solved(puzzle, final_state):
    return puzzle == final_state

if __name__ == "__main__":
    # game_attributes = set_game_preconditions()

    #3 for 3x3, 4 for 4x4 and 5 for 5x5
    # size = game_attributes[0]
    # index_of_zero_in_solved_puzzle = game_attributes[1]
    # puzzle = game_attributes[2]
   
    # puzzle = Puzzle_node([[1, 2, 5], [7, 6, 4], [8, 0, 3]], (2,1))
    # puzzle = Puzzle_node([[0, 2, 6], [1, 5, 3], [7, 4, 8]], (0,0))
    start_time = time.time()
    final_state = create_final_state_of_puzzle_from_given_size_and_zero_position(3, -1)
    # fn = Puzzle_node(final_state, (index_of_zero_in_solved_puzzle / size, index_of_zero_in_solved_puzzle % size))
    fn = Puzzle_node(final_state, (2, 2))
    final_state_dict_values = fn.tile_number_position_dict
    puzzle = Puzzle_node([[1,2,6], [0,5,3], [4, 7, 8]], (1,0))
    #puzzle = Puzzle_node([[5, 6, 3, 4], [8, 0, 1, 15], [10, 7, 2, 11], [12, 9, 14, 13]], (1,1))


    # puzzle3 = Puzzle_node([[1,2,3], [0,5,6], [4,7,8]], (1,0))
    # puzzle4 = Puzzle_node([[1,2,3,4], [5,6,7,8], [0,10,11,12], [9,13,14,15]], (2,0))
    # puzzle5 = Puzzle_node([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [0,17,18,19,20], [16, 21, 22, 23, 24]], (3,0))
    # print(is_puzzle_solved(puzzle, fn))
    #print(puzzle.calculate_manhattan_distance(fn))
    iterative_deepening_a_star(puzzle, fn, final_state_dict_values)
    # assert puzzle.is_solvable, "Puzzle is not solvable!"
    print("--- %s seconds ---" % (time.time() - start_time))
