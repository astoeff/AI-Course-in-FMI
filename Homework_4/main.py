from copy import deepcopy

from board import Board
from constants import (PLAYER_IS_FIRST_VALUE, COMPUTER_IS_FIRST_VALUE, INITIAL_VERSION_OF_BOARD,
                       EMPTY_POSITION_ON_BOARD_CHAR, PLAYER_SIGN_ON_BOARD_CHAR, COMPUTER_SIGN_ON_BOARD_CHAR, 
                       PLAYER_IS_ON_TURN_STRING, COMPUTER_IS_ON_TURN_STRING)


def read_who_is_first_input_from_console():
    inputted_value = None
    is_inputted_value_valid = inputted_value == PLAYER_IS_FIRST_VALUE or inputted_value == COMPUTER_IS_FIRST_VALUE
    while not is_inputted_value_valid:
        inputted_value = str(input('Enter 1 to be first, 0 otherwize: ' ))
        is_inputted_value_valid = inputted_value == PLAYER_IS_FIRST_VALUE or inputted_value == COMPUTER_IS_FIRST_VALUE
    return inputted_value

def check_if_player_is_first(inputted_value):
    return inputted_value == PLAYER_IS_FIRST_VALUE

def select_first_on_turn():
    inputted_value = read_who_is_first_input_from_console()
    is_player_first = check_if_player_is_first(inputted_value)    
    if is_player_first:
        current_player_on_turn = PLAYER_IS_ON_TURN_STRING
    else:
        current_player_on_turn = COMPUTER_IS_ON_TURN_STRING
    return current_player_on_turn

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
    board.update(position, PLAYER_SIGN_ON_BOARD_CHAR)
    return board

def max_alpha_beta(board, alpha, beta, init_depth, best_depth):
    maxv = -2
    px = None
    py = None

    result = board.is_end()

    if result == PLAYER_SIGN_ON_BOARD_CHAR:
        return (-1, 0, 0, init_depth, best_depth)
    elif result == COMPUTER_SIGN_ON_BOARD_CHAR:
        return (1, 0, 0, init_depth, best_depth)
    elif result == EMPTY_POSITION_ON_BOARD_CHAR:
        return (0, 0, 0, init_depth, best_depth)

    for i in reversed(range(0, 3)):
        for j in reversed(range(0, 3)):
            if board.board[i][j] == EMPTY_POSITION_ON_BOARD_CHAR:
                depth = init_depth
                board.board[i][j] = COMPUTER_SIGN_ON_BOARD_CHAR
                (m, min_i, in_j, depth, best_depth) = min_alpha_beta(board, alpha, beta, depth + 1, best_depth)
                if m > maxv or (m == maxv and depth < best_depth):
                    maxv = m
                    best_depth = depth 
                    px = i
                    py = j
                board.board[i][j] = EMPTY_POSITION_ON_BOARD_CHAR

                #pruning
                if maxv >= beta:
                    return (maxv, px, py, depth, best_depth)

                if maxv > alpha:
                    alpha = maxv

    return (maxv, px, py, depth, best_depth)

def min_alpha_beta(board, alpha, beta, init_depth, best_depth):
    minv = 2
    qx = None
    qy = None

    result = board.is_end()

    if result == PLAYER_SIGN_ON_BOARD_CHAR:
        return (-1, 0, 0, init_depth, best_depth)
    elif result == COMPUTER_SIGN_ON_BOARD_CHAR:
        return (1, 0, 0, init_depth, best_depth)
    elif result == EMPTY_POSITION_ON_BOARD_CHAR:
        return (0, 0, 0, init_depth, best_depth)

    for i in (range(0, 3)):
        for j in (range(0, 3)):
            if board.board[i][j] == EMPTY_POSITION_ON_BOARD_CHAR:
                depth = init_depth
                board.board[i][j] = PLAYER_SIGN_ON_BOARD_CHAR
                (m, max_i, max_j, depth, best_depth) = max_alpha_beta(board, alpha, beta, depth + 1, best_depth)
                if m < minv or (m == minv and depth < best_depth):
                    minv = m
                    best_depth = depth
                    qx = i
                    qy = j
                board.board[i][j] = EMPTY_POSITION_ON_BOARD_CHAR

                #pruning
                if minv <= alpha:
                    return (minv, qx, qy, depth, best_depth)

                if minv < beta:
                    beta = minv

    return (minv, qx, qy, depth, best_depth)

def main():
    current_player_on_turn = select_first_on_turn()
    board = Board(INITIAL_VERSION_OF_BOARD)
    while True:
        board.print()
        result = board.is_end()

        if result != None:
            break

        if current_player_on_turn == PLAYER_IS_ON_TURN_STRING:
            player_moves(board)
            current_player_on_turn = COMPUTER_IS_ON_TURN_STRING
        else:
            (m, px, py, d, bd) = max_alpha_beta(board, -2, 2, 0, 11)
            board.update((px, py), COMPUTER_SIGN_ON_BOARD_CHAR)
            current_player_on_turn = PLAYER_IS_ON_TURN_STRING


if __name__ == '__main__':
    main()