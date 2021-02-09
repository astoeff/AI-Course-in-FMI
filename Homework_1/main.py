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
            zero_position_in_input_puzzle = (row_count, row_as_list.index(0))
        row_count += 1

    return (number_of_rows, index_of_zero_in_solved_puzzle, Puzzle_node(puzzle, zero_position_in_input_puzzle))

def find_puzzle_children(puzzle, final_state_dict_values):
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
            pass
        else:
            puzzle_children.append(Puzzle_node(content, (puzzle_zero_x, puzzle_zero_y - 1), puzzle.distance_from_root + 1, puzzle, movement_direction = "right"))
        finally:
            content = deepcopy(puzzle.content)

    #DOWN
    try:
        content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x + 1][puzzle_zero_y] = content[puzzle_zero_x + 1][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y]
    except Exception as e:
        pass
    else:
        puzzle_children.append(Puzzle_node(content, (puzzle_zero_x + 1, puzzle_zero_y), puzzle.distance_from_root + 1, puzzle, movement_direction = "up"))
    finally:
        content = deepcopy(puzzle.content)
    
    #RIGHT
    try:
        content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y + 1] = content[puzzle_zero_x][puzzle_zero_y + 1], content[puzzle_zero_x][puzzle_zero_y]
    except Exception as e:
        pass
    else:
        puzzle_children.append(Puzzle_node(content, (puzzle_zero_x, puzzle_zero_y + 1), puzzle.distance_from_root + 1, puzzle, movement_direction = "left"))
    finally:
        content = deepcopy(puzzle.content)

    return sorted(puzzle_children, key=lambda x: x.calculate_heuristic(final_state_dict_values), reverse=True)

def iterative_deepening_a_star(root_puzzle, final_state, final_state_dict_values):
    is_solved = False
    limit = root_puzzle.calculate_heuristic(final_state_dict_values)
    while not is_solved:
        next_limit = limit + 2
        stack = [root_puzzle]
        visited = [root_puzzle]
        while stack:
            current_puzzle = stack.pop()
            if is_puzzle_solved(current_puzzle, final_state):
                is_solved = True
                final_state = current_puzzle
                break
            
            current_puzzle.children = find_puzzle_children(current_puzzle, final_state_dict_values)
            for child in current_puzzle.children:
                if  child.calculate_heuristic(final_state_dict_values) < limit and child not in visited:
                    stack.append(child)
                    visited.append(child)

        limit = next_limit

    father = final_state.father_node
    steps = 0
    directions = []
    if final_state.movement_direction:
        directions.append(final_state.movement_direction)
    while father:
        if father.movement_direction:
            directions.append(father.movement_direction)
        father = father.father_node
        steps += 1

    return (steps, directions)    
    

def print_puzzle_solution(steps, directions):
    print(steps)
    i = steps - 1
    while i >= 0:
        print(directions[i])
        i -= 1

def is_puzzle_solvable(puzzle):
    #TODO: check if the puzzle is solvable
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
    game_attributes = set_game_preconditions()

    #3 for 3x3, 4 for 4x4 and 5 for 5x5
    size = game_attributes[0]
    index_of_zero_in_solved_puzzle = game_attributes[1]
    puzzle = game_attributes[2]
   
    final_state = create_final_state_of_puzzle_from_given_size_and_zero_position(size, index_of_zero_in_solved_puzzle)

    final_state_puzzle = Puzzle_node(final_state, (index_of_zero_in_solved_puzzle / size, index_of_zero_in_solved_puzzle % size))

    final_state_dict_values = final_state_puzzle.tile_number_position_dict

    steps, directions = iterative_deepening_a_star(puzzle, final_state_puzzle, final_state_dict_values)
    print_puzzle_solution(steps, directions)
    assert puzzle.is_solvable, "Puzzle is not solvable!"
