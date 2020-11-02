from math import sqrt

from constants import SOLVED_PUZZLE_TILES_POSITIONS_DICT

def set_game_preconditions():
    number_of_tiles = input("Enter 8, 15 or 24 as for number of the square tiles:")
    index_of_zero_in_solved_puzzle = input("Enter index of zero in solved puzzle (-1 is for the last index):")
    
    print("Now enter the puzzle")

    number_of_rows = int(sqrt(int(number_of_tiles) + 1))

    puzzle = []
    #the puzzle is square shaped so rows = cols
    for row in range(number_of_rows):
        r = input("Enter row: ")
        puzzle.append([int(i) for i in r.split(',')])

    return (number_of_tiles, index_of_zero_in_solved_puzzle, puzzle)

def calculate_manhattan_distance_for_puzzle(puzzle):
    manhattan_distance = 0
    tile_x = 0
    for row in puzzle:
        tile_y = 0
        for tile in row:
            if tile != 0:
                manhattan_distance += abs(tile_x - SOLVED_PUZZLE_TILES_POSITIONS_DICT[tile][0]) + abs(tile_y - SOLVED_PUZZLE_TILES_POSITIONS_DICT[tile][1])
            tile_y += 1
        tile_x += 1
    return manhattan_distance

def is_puzzle_solvable(puzzle):
    return True

def print_puzzle(puzzle):
    for i in puzzle:
        print(i)

if __name__ == "__main__":
    game_attributes = set_game_preconditions()
    number_of_tiles = game_attributes[0]
    index_of_zero_in_solved_puzzle = game_attributes[1]
    puzzle = game_attributes[2]


    # puzzle = [[1, 2, 5], [7, 6, 4], [8, 0, 3]]
    puzzle2 = [[1,2,3], [4,5,6], [7,8,0]]
    assert is_puzzle_solvable, "Puzzle is not solvable!"

    print(calculate_manhattan_distance_for_puzzle(puzzle))
    print_puzzle(puzzle)
    print('\n')
    print_puzzle(puzzle2)
