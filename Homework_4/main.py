from constants import PLAYER_IS_FIRST_VALUE, COMPUTER_IS_FIRST_VALUE, INITIAL_VERSION_OF_BOARD, EMPTY_POSITION_ON_BOARD_CHAR, PLAYER_SIGN_ON_BOARD_CHAR
from board import Board


def read_who_is_first_input_from_console():
    inputted_value = None
    is_inputted_value_valid = inputted_value == PLAYER_IS_FIRST_VALUE or inputted_value == COMPUTER_IS_FIRST_VALUE
    while not is_inputted_value_valid:
        inputted_value = str(input('Enter 1 to be first, 0 otherwize: ' ))
        is_inputted_value_valid = inputted_value == PLAYER_IS_FIRST_VALUE or inputted_value == COMPUTER_IS_FIRST_VALUE
    return inputted_value

def check_if_player_is_first(inputted_value):
    return inputted_value == PLAYER_IS_FIRST_VALUE

def read_player_position_input_from_console():
    inputted_value = str(input('Enter position in format x,y, example: 0, 2: ' ))
    position = (int(inputted_value[0]), int(inputted_value[len(inputted_value) - 1]))
    return position

def check_if_position_is_available(board, position):
    return board.board[position[0]][position[1]] == EMPTY_POSITION_ON_BOARD_CHAR

def player_moves(board):
    board.print()
    position = None
    is_position_available = False
    while not is_position_available:
        position = read_player_position_input_from_console()
        is_position_available = check_if_position_is_available(board, position)
    board.update(position, PLAYER_SIGN_ON_BOARD_CHAR)
    # board.print()

def main():
    inputted_value = read_who_is_first_input_from_console()
    is_player_first = check_if_player_is_first(inputted_value)
    initial_board_list_of_values = INITIAL_VERSION_OF_BOARD
    # board = Board(initial_board_list_of_values)
    # board = Board([['_', '_', '_'], ['X', 'X', 'O'], ['O', 'O', 'O']])
    board = Board([['X', 'X', 'X'], ['O', 'O', '_'], ['O', '_', '_']])
    # player_moves(board)
    print(board.check_if_solved_by_row())

if __name__ == '__main__':
    main()