from copy import deepcopy
from termcolor import colored

from constants import PLAYER_IS_FIRST_VALUE, COMPUTER_IS_FIRST_VALUE, INITIAL_VERSION_OF_BOARD, EMPTY_POSITION_ON_BOARD_CHAR, PLAYER_SIGN_ON_BOARD_CHAR, BOARD_FINAL_STATE_CHAR, PLAYER_IS_ON_TURN_STRING, COMPUTER_IS_ON_TURN_STRING
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
    position = None
    is_position_available = False
    while not is_position_available:
        position = read_player_position_input_from_console()
        is_position_available = check_if_position_is_available(board, position)
    board.update(position, colored(PLAYER_SIGN_ON_BOARD_CHAR, 'green'))
    # board.print()

def max_alpha_beta(board, alpha, beta):
    maxv = -2
    px = None
    py = None

    result = board.check_if_final_state()

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    board_copy = deepcopy(board)
    for i in range(0, 3):
        for j in range(0, 3):
            if board_copy.board[i][j] == '_':
                # print('YEEEEEEEEEEEEEEYYEYYEYYEYEYEYEYEY')
                board_copy.board[i][j] = 'O'
                (m, min_i, in_j) = min_alpha_beta(board_copy, alpha, beta)
                if m > maxv:
                    maxv = m
                    px = i
                    py = j
                board_copy.board[i][j] = '_'

                # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                if maxv >= beta:
                    return (maxv, px, py)

                if maxv > alpha:
                    alpha = maxv
    # print('IN function')
    # print(px, py)
    return (maxv, px, py)

def min_alpha_beta(board, alpha, beta):
    minv = 2

    qx = None
    qy = None

    result = board.check_if_final_state()

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    board_copy = deepcopy(board)
    for i in range(0, 3):
        for j in range(0, 3):
            if board_copy.board[i][j] == '_':
                board_copy.board[i][j] = 'X'
                (m, max_i, max_j) = max_alpha_beta(board_copy, alpha, beta)
                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                board_copy.board[i][j] = '_'

                if minv <= alpha:
                    return (minv, qx, qy)

                if minv < beta:
                    beta = minv

    return (minv, qx, qy)

def main():
    # b = Board([['X', '_', '_'], ['_', 'X', '_'], ['_', '_', 'X']])
    # print(b.check_if_final_state())
    inputted_value = read_who_is_first_input_from_console()
    is_player_first = check_if_player_is_first(inputted_value)
    initial_board_list_of_values = INITIAL_VERSION_OF_BOARD
    board = Board(initial_board_list_of_values)
    # board = Board([['_', '_', '_'], ['X', 'X', 'O'], ['O', 'O', 'O']])
    # board = Board([['X', 'X', 'X'], ['O', 'O', '_'], ['O', '_', '_']])
    # board_copy = deepcopy(board)
    # board_copy.board[0][0] = 'Y'
    # board.print()
    # board_copy.print()
    current_player_on_turn = None
    if is_player_first:
        current_player_on_turn = PLAYER_IS_ON_TURN_STRING
    else:
        current_player_on_turn = COMPUTER_IS_ON_TURN_STRING

    board.print()
    while board.solved_sign == EMPTY_POSITION_ON_BOARD_CHAR:
        if current_player_on_turn == PLAYER_IS_ON_TURN_STRING:
            player_moves(board)
            current_player_on_turn = COMPUTER_IS_ON_TURN_STRING
        else:
            # print('BOARD FOR BOT')
            # board.print()
            # print('----------------------------')
            board_copy = deepcopy(board)
            (m, px, py) = max_alpha_beta(board_copy, -2, 2)
            # print(px, py)
            board.update((px, py), colored('O', 'red'))
            # board.board[px][py] = 'O'
            current_player_on_turn = PLAYER_IS_ON_TURN_STRING
        board.check_if_final_state()
        board.print()


if __name__ == '__main__':
    main()