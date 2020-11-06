from math import sqrt
from copy import deepcopy

from puzzle import Puzzle_node
from constants import SOLVED_PUZZLE_TILES_POSITIONS_DICT


def set_game_preconditions():
    number_of_tiles = input("Enter 8, 15 or 24 as for number of the square tiles:")
    index_of_zero_in_solved_puzzle = input("Enter index of zero in solved puzzle (-1 is for the last index):")
    
    print("Now enter the puzzle")

    number_of_rows = int(sqrt(int(number_of_tiles) + 1))

    puzzle = []
    zero_position_in_input_puzzle = None
    row_count = 0
    #the puzzle is square shaped so rows = cols
    for row in range(number_of_rows):
        r = input("Enter row: ")
        row_as_list = [int(i) for i in r.split(',')]
        puzzle.append(row_as_list)
        if 0 in row_as_list:
            zero_position_in_input_puzzle = (puzzle.index(row_as_list), row_as_list.index(0))
        row_count += 1

    return (number_of_tiles, index_of_zero_in_solved_puzzle, Puzzle_node(puzzle, zero_position_in_input_puzzle))

def visit_puzzle(puzzle, stack, visited):
    stack.append(puzzle)
    visited[puzzle] = True

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
            print('UP')
        else:
            puzzle_children.append(Puzzle_node(content, (puzzle_zero_x - 1, puzzle_zero_y)))
        finally:
            content = deepcopy(puzzle.content)

    #LEFT
    #otherwise if zero is first element in list with index - 1 will get the last element
    if puzzle_zero_y - 1 >= 0:
        try:
            content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y - 1] = content[puzzle_zero_x ][puzzle_zero_y - 1], content[puzzle_zero_x][puzzle_zero_y]
        except Exception as e:
            print('LEFT')
        else:
            puzzle_children.append(Puzzle_node(content, (puzzle_zero_x, puzzle_zero_y - 1)))
        finally:
            content = deepcopy(puzzle.content)

    #DOWN
    try:
        content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x + 1][puzzle_zero_y] = content[puzzle_zero_x + 1][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y]
    except Exception as e:
        print('DOWN')
    else:
        puzzle_children.append(Puzzle_node(content, (puzzle_zero_x + 1, puzzle_zero_y)))
    finally:
        content = deepcopy(puzzle.content)
    
    #RIGHT
    try:
        content[puzzle_zero_x][puzzle_zero_y], content[puzzle_zero_x][puzzle_zero_y + 1] = content[puzzle_zero_x][puzzle_zero_y + 1], content[puzzle_zero_x][puzzle_zero_y]
    except Exception as e:
        print('RIGHT')
    else:
        puzzle_children.append(Puzzle_node(content, (puzzle_zero_x, puzzle_zero_y + 1)))
    finally:
        content = deepcopy(puzzle.content)

    return puzzle_children

def execute_iterative_deepening_a_star_with_heuristic_as_limit(root_puzzle, heuristic_as_limit, visited):
    stack = [root_puzzle]
    if not stack.empty():
        current_puzzle = stack.pop()

def is_puzzle_solvable(puzzle):
    return True


if __name__ == "__main__":
    # game_attributes = set_game_preconditions()
    # number_of_tiles = game_attributes[0]
    # index_of_zero_in_solved_puzzle = game_attributes[1]
    # puzzle = game_attributes[2]
    stack = []
    visited = {}


    # puzzle = Puzzle_node([[1, 2, 5], [7, 6, 4], [8, 0, 3]], (2,1))
    puzzle = Puzzle_node([[0, 2, 6], [1, 5, 3], [7, 4, 8]], (0,0))

    puzzle2 = [[1,2,3], [4,5,6], [7,8,0]]
    assert puzzle.is_solvable, "Puzzle is not solvable!"

    print('#############')
    puzzle.print_puzzle()
    print('###########')

    chld = find_puzzle_children(puzzle)
    for i in chld:
        print('#############')
        i.print_puzzle()
        print('###########')
