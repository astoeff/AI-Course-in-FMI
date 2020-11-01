from math import sqrt

def set_game_preconditions():
    number_of_tiles = input("Enter 8, 15 or 24 as for number of the square tiles:")
    index_of_zero_in_solved_puzzle = input("Enter index of zero in solved puzzle (-1 is for the last index):")
    
    print("Now enter the puzzle")

    number_of_rows = int(sqrt(number_of_tiles + 1))

    puzzle = []
    #the puzzle is square shaped so rows = cols
    for row in range(number_of_rows):
        r = input("Enter row: ")
        puzzle.append([i for i in r])

    return (number_of_tiles, index_of_zero_in_solved_puzzle, puzzle)

def is_puzzle_solvable():
    pass

def print_puzzle(puzzle):
    for i in puzzle:
        print(i)

if __name__ == "__main__":
    game_attributes = set_game_preconditions()
    number_of_tiles = game_attributes[0]
    index_of_zero_in_solved_puzzle = game_attributes[1]
    puzzle = game_attributes[2]
